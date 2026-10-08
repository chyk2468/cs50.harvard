# CS50 AI Project 4A: Shopping

## Author
`chyk2468`

## Overview
This project implements a machine learning nearest-neighbor classifier to predict whether online shopping users will complete a purchase (`Revenue` is true) based on a dataset of user session attributes. The project covers data preprocessing, feature engineering, categorical encoding, model training with scikit-learn, and evaluation using Sensitivity (True Positive Rate) and Specificity (True Negative Rate).

---

## Dataset Schema & Preprocessing

The dataset `shopping.csv` contains 12,330 user session records. `load_data(filename)` reads and converts each row into a 17-element numerical feature vector (`evidence`) and a binary target label (`labels`):

| Index | Feature | Type | Description |
|---|---|---|---|
| 0 | `Administrative` | `int` | Number of administrative pages visited |
| 1 | `Administrative_Duration` | `float` | Total time spent on administrative pages (seconds) |
| 2 | `Informational` | `int` | Number of informational pages visited |
| 3 | `Informational_Duration` | `float` | Total time spent on informational pages (seconds) |
| 4 | `ProductRelated` | `int` | Number of product-related pages visited |
| 5 | `ProductRelated_Duration` | `float` | Total time spent on product-related pages (seconds) |
| 6 | `BounceRates` | `float` | Percentage of visitors entering and exiting from page |
| 7 | `ExitRates` | `float` | Percentage of all pageviews ending on this page |
| 8 | `PageValues` | `float` | Average value of page visited before transaction |
| 9 | `SpecialDay` | `float` | Closeness of site visiting time to a special day |
| 10 | `Month` | `int` | Month index (`Jan=0` through `Dec=11`) |
| 11 | `OperatingSystems` | `int` | Operating system identifier |
| 12 | `Browser` | `int` | Web browser identifier |
| 13 | `Region` | `int` | Geographic region identifier |
| 14 | `TrafficType` | `int` | Traffic source identifier |
| 15 | `VisitorType` | `int` | `1` for `Returning_Visitor`, else `0` |
| 16 | `Weekend` | `int` | `1` if weekend session (`TRUE`), else `0` |
| Target | `Revenue` | `int` | `1` if completed transaction (`TRUE`), else `0` |

---

## Model Training

`train_model(evidence, labels)` fits a $k$-nearest-neighbor classifier using `sklearn.neighbors.KNeighborsClassifier` with $k = 1$ (`n_neighbors=1`) on the training data split.

---

## Evaluation Metrics

`evaluate(labels, predictions)` computes the classification performance across positive and negative classes:

- **Sensitivity (True Positive Rate)**: Proportion of actual buyers accurately classified:
  $$\text{Sensitivity} = \frac{\text{True Positives}}{\text{Actual Positives}}$$

- **Specificity (True Negative Rate)**: Proportion of non-buyers accurately classified:
  $$\text{Specificity} = \frac{\text{True Negatives}}{\text{Actual Negatives}}$$

---

## Running the Project

```bash
python shopping.py shopping.csv
```

### Typical Output:
```text
Correct: 4052
Incorrect: 880
True Positive Rate: 35.83%
True Negative Rate: 90.44%
```
