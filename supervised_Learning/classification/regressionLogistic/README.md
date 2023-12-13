# Logistic regression

Logistic regression is a method used for binary classification problems, where there are only two possible values. Its main objective is to predict a dependent variable from an independent variable, identifying whether an event or category occurs.

## Characteristics:

- It can only have 2 possible values.
- Predict a dependent variable from an independent variable.
- Main objective is to identify if an event occurs.

## Applications:

- Detect spam.
- Detect diseases.

## Formula:

The logistics function is expressed as:

\[ f(x) = \frac{1}{1 + e^{-x}} \]

Where:
- Returns 1 if it tends to \(+\infty\).
- Returns 0 if it tends to \(-\infty\).

## Linear Regression vs Logistic Regression:

Linear regression is not suitable for binary classes, so logistic regression is used.

## Transformation to Classification:

Logistic regression can be transformed into classification when working within a range. Examples include predicting the number of children, height, whether a client will default on a loan, or whether a student will pass or fail.

## Limitation on Classification:

It is essential to set clear limits on classification to avoid overfitting and ensure accurate results. Logistic regression is used for independent variables with a binary dependent variable.

## Regression in Classification through Logistics:

- Define thresholds between 0 and 1.
- Values ​​below the threshold are classified as one class.
- Values ​​above the threshold are classified in another class.

## Choice of Thresholds:

The choice of thresholds is based on metrics such as true positives, optimizing precision or area under the curve (AUC).

## Observations:

- The hyperparameter is not alpha as in linear regressions.
- It can be regularized with L1 and L2 penalties (L2 by default).