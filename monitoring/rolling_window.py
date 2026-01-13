def get_time_windows(df, time_col):
    return {
        "1h": df[df[time_col] >= df[time_col].max() - pd.Timedelta(hours=1)],
        "1d": df[df[time_col] >= df[time_col].max() - pd.Timedelta(days=1)],
        "7d": df[df[time_col] >= df[time_col].max() - pd.Timedelta(days=7)],
    }