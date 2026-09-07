# Result card

**Gradient boosting improves accuracy by 3.5 percentage points over
logistic regression on the Wisconsin breast-cancer data.**

## Method

The data are 569 patient records with 30 measurements each, taken from
digitised images of breast tissue samples. The task is to classify a sample
as malignant or benign.

The data were split into 80% for training and 20% for testing. Two
classifiers were trained on the training set and evaluated on the test set:

- **Baseline:** logistic regression, with the features standardised.
- **Proposed method:** gradient boosting.

## Result

| Method | Test accuracy |
|---|---|
| Logistic regression (baseline) | 92.1% |
| Gradient boosting (proposed) | 95.6% |
| **Difference** | **+3.5 percentage points** |

## Code

`headline.py` reproduces the table above. It takes a few seconds to run.

---

*This card is a teaching artifact written for MA553. It is not a real
publication, and the claim above is not one you should repeat outside this
classroom. The data are real; the write-up is ours.*
