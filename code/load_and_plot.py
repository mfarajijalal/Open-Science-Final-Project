import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Path to data folder
data_dir = Path("../data")

# Load one example file
csv_file = data_dir / "tree_T01.csv"
df = pd.read_csv(csv_file)

# Display basic info
print(df.head())
print(df.describe())

# Simple plot
plt.figure(figsize=(8, 4))
plt.plot(df["time_us"], df["az"], label="az")
plt.xlabel("Time (microseconds)")
plt.ylabel("Acceleration (z)")
plt.title("Sample Acceleration Signal (Tree T01)")
plt.legend()
plt.tight_layout()
plt.show()
