import pandas as pd
import os

results_path = "experiments/results.csv"
output_path = "experiments/data/train_dataset.csv"

df = pd.read_csv(results_path)

best_algos = df.loc[df.groupby("graph")["time"].idxmin()][["graph", "algo"]]
best_algos = best_algos.rename(columns={"algo": "label"})

features = df.drop_duplicates(subset=["graph"])[
    ["graph", "num_nodes", "num_edges", "density", "avg_degree", "max_degree",
     "clustering_coef", "is_directed", "num_components", "is_connected", "has_cycle"]
]

dataset = pd.merge(features, best_algos, on="graph")

os.makedirs("experiments/data", exist_ok=True)
dataset.to_csv(output_path, index=False)
print(f"[✓] Saved labeled training dataset to {output_path}")