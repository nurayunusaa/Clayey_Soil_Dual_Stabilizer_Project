import pandas as pd

# Load raw datasets
ucs = pd.read_csv("../data/raw/UCS_CBR_data.csv")
stab = pd.read_csv("../data/raw/stabilizer_properties.csv")

# Example: merge datasets
merged = pd.merge(ucs, stab, on="Sample_ID")
merged.to_csv("../data/processed/fused_dataset.csv", index=False)
print("Fused dataset saved.")
