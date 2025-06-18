import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
import joblib
import os

df = pd.read_csv("experiments/data/train_dataset.csv")

X = df.drop(columns=["graph", "label"])
y = df["label"]

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

clf = xgb.XGBClassifier(n_estimators=100, use_label_encoder=False, eval_metric="mlogloss")
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("\n[✓] Classification Report:\n")
print(classification_report(y_test, y_pred))

os.makedirs("experiments/model", exist_ok=True)
joblib.dump(clf, "experiments/model/model.pkl")
joblib.dump(label_encoder, "experiments/model/label_encoder.pkl")
print("\n[✓] Trained XGBoost model saved to experiments/model/model.pkl")
print("[✓] Label encoder saved to experiments/model/label_encoder.pkl")