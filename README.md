# Prioritizing Customer Accounts for Manual Review Using Credit Default Risk

This project uses machine-learning models to help a bank decide and rank which 1,000 of 30,000 customer accounts should be prioritized for manual review before the next payment cycle. Rather than simply predicting default, the goal is to rank accounts by default risk under the bank’s fixed 3.33\% review capacity.

## Headline Result

Models are evaluated on a held-out test set of 6,000 customers with a review capacity of 200 accounts.

| Model | Defaulters Identified | Test Recall |
|---|---:|---:|
| Baseline | 138 | 10.4% |
| **Logistic Regression** | **157** | **11.8%** |
| Random Forest | 155 | 11.7% |

**Recommended model: Logistic Regression**

Logistic regression achieves the highest held-out test recall while remaining simpler and more interpretable than the random forest.

## Reproduce the Headline Result

All code is contained in `Credit_Default_Risk_Manual_Review.ipynb`. The notebook automatically fetches the UCI Default of Credit Card Clients dataset using `ucimlrepo` and uses the fixed random seed:

```text
SEED = 5622
```

From the repository root, run:

```bash
python -m jupyter nbconvert --to notebook --execute Credit_Default_Risk_Manual_Review.ipynb --output executed_notebook.ipynb
```

The expected final held-out result is:

```text
Baseline             10.4% recall   138 defaulters identified
Logistic Regression  11.8% recall   157 defaulters identified
Random Forest        11.7% recall   155 defaulters identified
```
The recommended logistic regression model has **11.8% recall**, identifying **157 of 1,327 defaulters** within the 200-account review capacity.

Google Colab: 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/baovrnguyen/Credit-Default-Risk-Manual-Review/blob/main/Credit_Default_Risk_Manual_Review.ipynb)

## Dataset

This project uses the **UCI Default of Credit Card Clients** dataset with 30,000 customer accounts.

The dataset contains information on credit limits, repayment history, bill balances, previous payments, customer characteristics, and next-month default.

The data is split using a stratified 80/20 train-test split:

```text
Training set: 24,000 customers
Test set:      6,000 customers
```

## Modeling Approach

The project compares a repayment-history baseline, logistic regression with regularization, and random forest. 

Model selection uses **Recall at 3.33% Review Capacity** with 5-fold stratified cross-validation.

All preprocessing is fit within each cross-validation training fold to avoid data leakage.

K-means features are added to both logistic regression and random forest to test whether they improved recall, but does not meaningfully improve performance and are excluded from the final modeling decision.

## Failure Analysis

The final logistic regression model is evaluated across age groups and credit-limit quartiles.

The weakest segment is the highest credit-limit quartile in Q4:

```text
Customers:              1,437
Actual defaulters:        199
Defaulters identified:      7
Recall:                    3.5%
95% CI:                1.7%–7.1%
```

This group shows weaker repayment-delay and credit-utilization signals, causing many eventual defaulters to receive lower risk rankings.

## Limitations

The dataset represents a historical population of credit-card customers from Taiwan, so the results may not directly generalize to a current U.S. bank and its customer population.

Future work could evaluate the models using more recent U.S. banking data and richer customer information such as assets under management and transaction patterns.
