import os
import json
import networkx as nx
import csv
from core.extractor import extract_features
from core.scheduler import schedule_algorithm
from core.algorithms import run_algorithm

GRAPH_DIR = "experiments/sample_graphs/"
OUTPUT_FILE = "experiments/results.csv"

def load_graph_from_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    G = nx.Graph()
    G.add_edges_from(data["edges"])
    return G

def run_experiments():
    results = []
    for filename in os.listdir(GRAPH_DIR):
        if filename.endswith(".json"):
            path = os.path.join(GRAPH_DIR, filename)
            G = load_graph_from_json(path)
            features = extract_features(G)
            algo = schedule_algorithm(features)
            result = run_algorithm(G, algo, source=0)

            results.append({
                "graph": filename,
                "algo": algo,
                "num_nodes": features["num_nodes"],
                "num_edges": features["num_edges"],
                "density": round(features["density"], 3),
                "avg_degree": features["avg_degree"],
                "max_degree": features["max_degree"],
                "clustering_coef": features["clustering_coef"],
                "is_directed": features["is_directed"],
                "num_components": features["num_components"],
                "is_connected": features["is_connected"],
                "has_cycle": features["has_cycle"],
                "time": round(result["time"], 6)
            })

    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    run_experiments()