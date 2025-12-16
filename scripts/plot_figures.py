import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/processed/fused_dataset.csv")

# UCS vs CBR plot
plt.figure(figsize=(6,4))
sns.scatterplot(x="CBR", y="UCS", data=df)
plt.xlabel("CBR (%)")
plt.ylabel("UCS (kPa)")
plt.title("UCS vs CBR for Stabilized Soil")
plt.savefig("../main_paper/figures/Figure1_UCS_CBR.png", dpi=300)
plt.close()
