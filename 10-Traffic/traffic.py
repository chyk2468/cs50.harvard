# chyk2468
import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    images = []
    labels = []

    for entry in sorted(os.listdir(data_dir)):
        cat_dir = os.path.join(data_dir, entry)
        if not os.path.isdir(cat_dir):
            continue

        try:
            category = int(entry)
        except ValueError:
            continue

        for filename in sorted(os.listdir(cat_dir)):
            filepath = os.path.join(cat_dir, filename)
            img = cv2.imread(filepath)
            if img is None:
                continue

            resized = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
            rgb_img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

            images.append(rgb_img)
            labels.append(category)

    return images, labels


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = tf.keras.models.Sequential([
        # Input layer specification
        tf.keras.layers.Input(shape=(IMG_WIDTH, IMG_HEIGHT, 3)),

        # Normalize pixel values from [0, 255] to [0.0, 1.0]
        tf.keras.layers.Rescaling(1.0 / 255),

        # First convolutional layer (32 filters, 3x3 kernel, ReLU) + max pooling (2x2)
        tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # Second convolutional layer (64 filters, 3x3 kernel, ReLU) + max pooling (2x2)
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # Flatten layer
        tf.keras.layers.Flatten(),

        # Dense hidden layer with 128 units and ReLU activation
        tf.keras.layers.Dense(128, activation="relu"),

        # Dropout layer to mitigate overfitting (rate = 0.5)
        tf.keras.layers.Dropout(0.5),

        # Output layer with NUM_CATEGORIES units and softmax activation
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


if __name__ == "__main__":
    main()
