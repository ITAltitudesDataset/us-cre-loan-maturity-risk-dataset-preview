"""Educational US CRE anomaly detection demo. Install: pip install pandas scikit-learn matplotlib numpy"""
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).resolve().parent
df = pd.read_csv(HERE / "us_cre_preview_50.csv")
df["Original Loan (USD)"] = pd.to_numeric(df["Original Loan (USD)"], errors="coerce")
df["Interest Rate (%)"] = pd.to_numeric(df["Interest Rate (%)"], errors="coerce")
# Source preview uses DD-MM-YYYY dates.
maturity = pd.to_datetime(df["Maturity Date"], format="%d-%m-%Y", errors="coerce")
report = pd.to_datetime(df["Reporting Period End"], format="%d-%m-%Y", errors="coerce")
df["Years to Maturity"] = (maturity - report).dt.days / 365.25
df = df.dropna(subset=["Original Loan (USD)", "Interest Rate (%)", "Years to Maturity"]).copy()
features = np.column_stack([np.log1p(df["Original Loan (USD)"]), df["Interest Rate (%)"], df["Years to Maturity"]])
features = StandardScaler().fit_transform(features)
model = IsolationForest(n_estimators=200, contamination=0.10, random_state=42)
df["Anomaly Score"] = model.fit(features).decision_function(features)
df["Anomaly Flag"] = np.where(model.predict(features) == -1, "Flagged", "Not flagged")
cols = ["Property / Portfolio", "State(s)", "Original Loan (USD)", "Interest Rate (%)", "Years to Maturity", "Anomaly Score", "Anomaly Flag"]
df[cols].to_csv(HERE / "us_cre_ml_results.csv", index=False)
flagged = df["Anomaly Flag"] == "Flagged"
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.scatter(df.loc[~flagged, "Original Loan (USD)"] / 1e6, df.loc[~flagged, "Interest Rate (%)"], label="Not flagged", alpha=.75)
ax.scatter(df.loc[flagged, "Original Loan (USD)"] / 1e6, df.loc[flagged, "Interest Rate (%)"], label="Statistical anomaly", marker="X", s=100)
ax.set(xlabel="Original loan amount (USD millions)", ylabel="Interest rate (%)", title="US CRE preview: Isolation Forest anomaly flags")
ax.legend(); ax.grid(alpha=.18); fig.tight_layout(); fig.savefig(HERE / "us_cre_ml_chart.png", dpi=180)
print(f"Analyzed {len(df)} records; flagged {flagged.sum()} statistical anomalies")
