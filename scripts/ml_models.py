import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load fused dataset
df = pd.read_csv("../data/processed/fused_dataset.csv")
X = df.drop(columns=["UCS"])
y = df["UCS"]

# Gradient Boosting
gb = GradientBoostingRegressor()
gb.fit(X, y)
preds = gb.predict(X)
print("GB R²:", r2_score(y, preds))

# Random Forest
rf = RandomForestRegressor()
rf.fit(X, y)
preds_rf = rf.predict(X)
print("RF R²:", r2_score(y, preds_rf))
