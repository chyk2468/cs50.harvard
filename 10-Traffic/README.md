# CS50 AI Project 5: Traffic Sign Classification

## Author
`chyk2468`

---

## 1. Project Overview
This project focuses on building and training a deep Convolutional Neural Network (CNN) to classify images of German road signs using TensorFlow and Keras. Recognizing traffic signs from camera feeds is an essential component of autonomous driving systems and advanced driver assistance systems (ADAS), where images vary widely in resolution, illumination, viewpoint angle, motion blur, and background clutter.

The project uses the **German Traffic Sign Recognition Benchmark (GTSRB)** dataset to train a multiclass classifier across 43 distinct traffic sign classes (such as speed limits, yield signs, stop signs, pedestrian crossings, and hazard warnings).

---

## 2. Technologies Used
- **Python 3.11 / 3.12**
- **TensorFlow 2.x & Keras**: Model construction, layer sequencing, optimization, and training.
- **OpenCV (`cv2`)**: Image loading from filesystem, resizing, and BGR-to-RGB color channel conversion.
- **NumPy**: Multidimensional array manipulation, tensor conversion, and array slicing.
- **Scikit-learn**: Stratified data partitioning into training (60%) and testing (40%) splits (`train_test_split`).

---

## 3. Dataset & Preprocessing Pipeline
The GTSRB dataset consists of 26,640 images organized into 43 numbered subdirectories (`0` through `42`):
1. **Directory Iteration**: `load_data(data_dir)` scans all category folders from `0` to `42`.
2. **Image Ingestion**: Each image is read via `cv2.imread(filepath)`. Unreadable or missing files are safely bypassed.
3. **Resizing**: Each variable-dimension traffic sign image is resized to standard dimensions of $30 \times 30$ pixels (`IMG_WIDTH = 30`, `IMG_HEIGHT = 30`).
4. **Color Conversion**: OpenCV loads images in BGR format; these are converted to standard RGB via `cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)`.
5. **Labels**: Assigned integer category labels matching the folder name.
6. **One-Hot Encoding**: Labels are encoded as 43-dimensional binary vectors via `tf.keras.utils.to_categorical(labels)`.

---

## 4. Final Selected Model Architecture
The final selected model is a balanced 2-stage Convolutional Neural Network with input rescaling and dropout regularization:

1. **Input Specification**: `Input(shape=(30, 30, 3))` accepting RGB images.
2. **Pixel Normalization**: `Rescaling(1.0 / 255)` mapping 8-bit integer pixel values $[0, 255]$ into floating-point range $[0.0, 1.0]$.
3. **First Convolutional Layer**: `Conv2D(32, kernel_size=(3, 3), activation="relu")` extracting 32 local spatial feature maps.
4. **First Pooling Layer**: `MaxPooling2D(pool_size=(2, 2))` reducing spatial dimensions from $28 \times 28$ to $14 \times 14$.
5. **Second Convolutional Layer**: `Conv2D(64, kernel_size=(3, 3), activation="relu")` learning 64 higher-level shape and pattern representations.
6. **Second Pooling Layer**: `MaxPooling2D(pool_size=(2, 2))` reducing spatial dimensions from $12 \times 12$ to $6 \times 6$.
7. **Flattening**: `Flatten()` transforming $6 \times 6 \times 64$ tensor into a 2,304-dimensional feature vector.
8. **Dense Hidden Layer**: `Dense(128, activation="relu")` performing non-linear feature integration.
9. **Dropout Layer**: `Dropout(rate=0.5)` randomly deactivating 50% of hidden neurons during training to prevent co-adaptation and overfitting.
10. **Output Layer**: `Dense(43, activation="softmax")` outputting a probability distribution across all 43 classes.

- **Compilation**:
  - **Optimizer**: Adam (`learning_rate=0.001`)
  - **Loss**: Categorical Crossentropy (`categorical_crossentropy`)
  - **Metrics**: Accuracy (`accuracy`)
- **Total Parameters**: 319,979 trainable parameters (~1.22 MB).

---

## 5. Experimentation & Architectural Comparison

To determine the most effective architecture, systematic experiments were conducted across the full dataset under identical train/test splits (15,984 training images, 10,656 test images, random state 42, 10 epochs):

| Experiment | Architecture Description | Parameters | Train Loss | Train Acc | Test Loss | Test Acc | Epoch Time |
|---|---|---|---|---|---|---|---|
| **Exp 1: Baseline** | 1x Conv2D(32) + MaxPool(2x2) + Dense(128) + Dropout(0.5) + Dense(43) | 809,387 | 0.2871 | 90.84% | 0.1163 | 97.36% | ~1.8s |
| **Exp 2: Selected** | 2x Conv2D(32, 64) + 2x MaxPool(2x2) + Dense(128) + Dropout(0.5) + Dense(43) | 319,979 | 0.1732 | 94.46% | 0.0586 | **98.64%** | ~1.8s |
| **Exp 3: Wider Dense** | 2x Conv2D(32, 64) + 2x MaxPool(2x2) + Dense(256) + Dropout(0.5) + Dense(43) | 620,523 | 0.0743 | 97.65% | 0.0530 | 98.82% | ~2.1s |

### Key Observations & Findings:
1. **Single vs. Hierarchical Convolutional Layers**:
   - Experiment 1 (single Conv layer) resulted in 809,387 parameters because the feature map before flattening remained large ($14 \times 14 \times 32 = 6,272$). Despite having more parameters, it achieved a lower test accuracy (97.36%) and higher test loss (0.1163).
   - Adding a second convolutional layer with max pooling (Experiment 2) reduced spatial dimensions to $6 \times 6 \times 64 = 2,304$ units prior to the Dense layer, cutting total parameters by over **60%** (to 319,979) while significantly improving feature representation and boosting test accuracy to **98.64%**.
2. **Impact of Dropout**:
   - Applying `Dropout(0.5)` was critical. Without dropout in early prototyping, the network quickly achieved near 100% training accuracy while test accuracy stagnated around 92-93% (a classic overfitting gap). With dropout at 0.5, test accuracy consistently exceeded training accuracy during initial epochs, demonstrating robust generalization.
3. **Wider Dense Layer Trade-off**:
   - Expanding the dense hidden layer from 128 to 256 units (Experiment 3) almost doubled parameters to 620,523. While it yielded a marginal gain in accuracy (98.82% vs 98.64%), it required 18% longer training time with slightly elevated risk of memorization.
   - Therefore, **Architecture 2** was selected as the optimal production choice for its balance of high accuracy (98.64%), low parameter footprint (319K), and fast inference.

---

## 6. How to Run

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Model Training and Evaluation
```bash
python traffic.py gtsrb
```

### Optional: Save Trained Model to Disk
```bash
python traffic.py gtsrb model.h5
```
