# chyk2468
import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    months = {
        "jan": 0, "january": 0,
        "feb": 1, "february": 1,
        "mar": 2, "march": 2,
        "apr": 3, "april": 3,
        "may": 4,
        "jun": 5, "june": 5,
        "jul": 6, "july": 6,
        "aug": 7, "august": 7,
        "sep": 8, "september": 8,
        "oct": 9, "october": 9,
        "nov": 10, "november": 10,
        "dec": 11, "december": 11
    }

    evidence = []
    labels = []

    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            month_key = row["Month"].strip().lower()
            month_num = months[month_key]

            visitor_type = (
                1 if row["VisitorType"].strip() == "Returning_Visitor" else 0
            )
            weekend = 1 if row["Weekend"].strip().upper() == "TRUE" else 0
            revenue = 1 if row["Revenue"].strip().upper() == "TRUE" else 0

            row_evidence = [
                int(row["Administrative"]),
                float(row["Administrative_Duration"]),
                int(row["Informational"]),
                float(row["Informational_Duration"]),
                int(row["ProductRelated"]),
                float(row["ProductRelated_Duration"]),
                float(row["BounceRates"]),
                float(row["ExitRates"]),
                float(row["PageValues"]),
                float(row["SpecialDay"]),
                month_num,
                int(row["OperatingSystems"]),
                int(row["Browser"]),
                int(row["Region"]),
                int(row["TrafficType"]),
                visitor_type,
                weekend
            ]
            evidence.append(row_evidence)
            labels.append(revenue)

    return evidence, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    actual_positives = 0
    actual_negatives = 0
    true_positives = 0
    true_negatives = 0

    for actual, predicted in zip(labels, predictions):
        if actual == 1:
            actual_positives += 1
            if predicted == 1:
                true_positives += 1
        else:
            actual_negatives += 1
            if predicted == 0:
                true_negatives += 1

    sensitivity = (
        true_positives / actual_positives if actual_positives > 0 else 0.0
    )
    specificity = (
        true_negatives / actual_negatives if actual_negatives > 0 else 0.0
    )

    return sensitivity, specificity


if __name__ == "__main__":
    main()
