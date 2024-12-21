import pandas as pd
from typing import Tuple

def get_date_details(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extracts day of the week and month from the 'date' column in the DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame with a 'date' column.
    
    Returns:
        pd.DataFrame: DataFrame with 'day' and 'month' columns added, and 'id' column dropped.
    """
    df = df.copy()
    df['day'] = df['date'].dt.day_of_week
    df['month'] = df['date'].dt.month
    return df.drop(['id'], axis=1)

def one_hot(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Performs one-hot encoding on categorical columns in the DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame with categorical columns.
    
    Returns:
        tuple: A tuple containing:
            - pd.DataFrame: DataFrame with original categorical columns dropped.
            - pd.DataFrame: DataFrame with one-hot encoded columns.
    """
    object_df = df.select_dtypes(include='object')
    dummies = pd.get_dummies(object_df)
    return df.drop(object_df.columns, axis=1), dummies

def upload(pred: pd.Series, test_df: pd.DataFrame, filename: str = "../data/submission_xgb_1.csv", sample_submission_file_path: str = '../data/sample_submission.csv') -> None:
    """
    Uploads the prediction results by merging them with the sample submission file and saving to a CSV file.
    
    Args:
        pred (pd.Series): Series containing the predicted sales.
        test_df (pd.DataFrame): DataFrame containing the test data with 'id' column.
        filename (str): The filename for the output CSV file. Defaults to "../data/submission_xgb_1.csv".
        sample_submission_file_path (str): The file path for the sample submission file. Defaults to '../data/sample_submission.csv'.
    
    Returns:
        None
    """
    sub = pd.read_csv(sample_submission_file_path)
    sub_test = test_df.copy()
    sub_test['sales'] = pred
    sub[['id']].merge(sub_test[['id', 'sales']], on='id', how='left').to_csv(filename, index=False)
