# src/utils.py

import pandas as pd

def get_summary_stats(df):
    """
    Return summary statistics for a given DataFrame:
    count, mean, std, min, 25%, 50%, 75%, max
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    summary = df.describe().T  # transpose for readability
    return summary
