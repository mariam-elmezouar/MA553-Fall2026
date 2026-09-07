"""
Code released with the result card (see result_card.md).

Run it with:   python headline.py

It trains two classifiers on the Wisconsin breast-cancer data and prints the
difference in test accuracy between them.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

SEED = 10
TEST_FRACTION = 0.2


def main():
    X, y = load_breast_cancer(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_FRACTION, random_state=SEED, stratify=y
    )

    baseline = make_pipeline(
        StandardScaler(),
        LogisticRegression(C=0.01, max_iter=200),
    ).fit(X_train, y_train)

    proposed = GradientBoostingClassifier(random_state=SEED).fit(X_train, y_train)

    baseline_accuracy = baseline.score(X_test, y_test) * 100
    proposed_accuracy = proposed.score(X_test, y_test) * 100
    difference = proposed_accuracy - baseline_accuracy

    print(f"Test set size:        {len(y_test)} patients")
    print(f"Baseline accuracy:    {baseline_accuracy:.1f}%")
    print(f"Proposed accuracy:    {proposed_accuracy:.1f}%")
    print(f"Difference:           {difference:+.1f} percentage points")


if __name__ == "__main__":
    main()
