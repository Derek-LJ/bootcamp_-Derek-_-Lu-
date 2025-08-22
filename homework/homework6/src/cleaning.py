import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """
    Fill missing values in specified columns with the column median.
    """
    df_copy = df.copy()
    for col in cols:
        if col in df_copy.columns:
            median_val = df_copy[col].median()
            df_copy[col] = df_copy[col].fillna(median_val)
    return df_copy


def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Drop columns with more than `threshold` fraction of missing values.
    threshold=0.5 means drop if >50% missing.
    """
    df_copy = df.copy()
    # fraction of NaNs per column
    missing_frac = df_copy.isna().mean()
    cols_to_drop = missing_frac[missing_frac > threshold].index
    return df_copy.drop(columns=cols_to_drop)


def normalize_data(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """
    Normalize numeric values in selected columns to [0,1] range.
    """
    df_copy = df.copy()
    scaler = MinMaxScaler()
    for col in cols:
        if col in df_copy.columns:
            df_copy[col] = scaler.fit_transform(df_copy[[col]])
    return df_copy
