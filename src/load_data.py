import pandas as pd
from src.config import DATA_PATH, BASELINE_RATIO

def load_dataset():
    df = pd.read_csv(DATA_PATH)
    return df

def split_baseline_monitoring(df):
    split_index = int(len(df) * BASELINE_RATIO)
    
    baseline_df = df.iloc[:split_index].reset_index(drop=True)
    monitoring_df = df.iloc[split_index:].reset_index(drop=True)

    return baseline_df, monitoring_df
    