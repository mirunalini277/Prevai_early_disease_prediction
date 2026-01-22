import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
hospital_df = pd.read_csv("data/hospital_data.csv")
weather_df = pd.read_csv("data/weather_data.csv")
data = pd.merge(hospital_df, weather_df, on="date")
X = data.drop("patient_count", axis=1)
y = data["patient_count"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
with open("models/predictor.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully")