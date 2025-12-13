import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Path to data folder (relative to code/ directory)
data_dir = Path(__file__).resolve().parent.parent / "data"

# Load all matching CSV files
csv_files = sorted(data_dir.glob("tree_T*.csv"))

for csv_file in csv_files:
    df = pd.read_csv(csv_file)

    # Display basic info
    print(f"\n=== {csv_file.name} ===")
    print(df.head())
    print(df.describe())

    # Simple plot
    plt.figure(figsize=(8, 4))
    plt.plot(df["time_us"], df["az"], label="az")
    plt.xlabel("Time (microseconds)")
    plt.ylabel("Acceleration (z)")
    plt.title(f"Sample Acceleration Signal ({csv_file.stem})")
    plt.legend()
    plt.tight_layout()
    plt.show()
