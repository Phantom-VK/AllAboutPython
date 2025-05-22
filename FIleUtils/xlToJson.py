import json
import pandas as pd

# Load Excel file
df = pd.read_excel("PLX-DAQ_R2.xlsm")

# Convert all columns (except Time) to numbers (if possible)
for col in df.columns:
    if col != "Time":
        df[col] = pd.to_numeric(df[col], errors='coerce')  # will convert to float or int

        # Convert 'Time' column to string format (HH:MM:SS)
df['Time'] = df['Time'].astype(str)

        # Convert other columns to numeric if needed
for col in df.columns:
    if col != 'Time':
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Optional: Fill NaNs if needed
df = df.fillna(0)

# Convert to list of dicts
data = df.to_dict(orient="records")

# Write to clean JSON file
with open("gas_readings_clean.json", "w") as f:
    json.dump(data, f, indent=2)
