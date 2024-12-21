# Store Sales Time Series Forecasting

## Overview
This repository contains implementations of various methods used for time series forecasting in the [Kaggle Store Sales Time Series Forecasting competition](https://www.kaggle.com/competitions/store-sales-time-series-forecasting). These methods aim to predict store sales efficiently and accurately, leveraging both statistical and machine learning techniques.

### Included Methods
The following methods are implemented and evaluated in this repository:
1. **Adaboost**: A boosting algorithm that combines weak learners to form a strong learner.
2. **Random-Patches based RandomForest**: A variant of Random Forest that samples both features and data.
3. **Statistics-based Approach**: Classical statistical methods for time series forecasting.
4. **XGBoost**: Gradient boosting using the default objective function.
5. **XGBoost (Poisson Objective)**: Gradient boosting tailored with a Poisson objective function.

---

## Performance Evaluation
The performance of these methods is evaluated using the metric **Root Mean Squared Logarithmic Error (RMSLE)**. Below is the comparative analysis:

![Performance Comparison](https://github.com/user-attachments/assets/3ade69a6-1250-478b-ade1-24f6ba563594)

---
## Usage
1. Install all the dependencies using ***requirements.txt***
2. Create a **data** directory under the root directory. 
3. Import the datasets **train.csv, test.csv, and sample_submission.csv** into the **data** direcotry
4. Check the ***config.py*** file under folder experiment
5. Head to any jupter notebook to get started
---
## Installation
To set up the project and install dependencies, run the following command:

```bash
pip install -r requirements.txt
```


---

## Acknowledgments
Special thanks to the Kaggle community for providing the competition and inspiring data.
Cite the dataset with the following statement
## Citation
If you use the dataset in your project, please ensure proper attribution. Cite the dataset as follows:
```bash
@misc{store-sales-time-series-forecasting,
    author = {Alexis Cook and DanB and inversion and Ryan Holbrook},
    title = {Store Sales - Time Series Forecasting},
    year = {2021},
    howpublished = {\url{https://kaggle.com/competitions/store-sales-time-series-forecasting}},
    note = {Kaggle}
}
```
