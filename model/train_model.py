import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

TARGET_COL = "fail"

def train_model(baseline_df):
    X = baseline_df.drop(columns=[TARGET_COL])
    y = baseline_df[TARGET_COL]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_scaled, y)

    return model, scaler