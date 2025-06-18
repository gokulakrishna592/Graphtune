import json
import networkx as nx
import joblib
import os
import sys
from core.extractor import extract_features

MODEL_PATH = "experiments/model/model.pkl"
ENCODER_PATH = "experiments/model/label_encoder.pkl"

def load_graph_from_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    G = nx.DiGraph() if data.get("directed", False) else nx.Graph()
    G.add_edges_from(data["edges"])
    return G

def predict_algorithm(graph_path):
    if not os.path.exists(MODEL_PATH):
        print("Model not found. Train the model first.")
        return
    if not os.path.exists(ENCODER_PATH):
        print("Label encoder not found. Make sure you saved it.")
        return

    clf = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)

    G = load_graph_from_json(graph_path)
    features = extract_features(G)
    feature_vector = [[
        features["num_nodes"],
        features["num_edges"],
        features["density"],
        features["avg_degree"],
        features["max_degree"],
        features["clustering_coef"],
        int(features["is_directed"]),
        features["num_components"],
        int(features["is_connected"]),
        int(features["has_cycle"]),
    ]]

    pred = clf.predict(feature_vector)
    algo = label_encoder.inverse_transform(pred)[0]
    print(f"Predicted Best Algorithm: **{algo}**")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python predict.py <graph_json_path>")
    else:
        predict_algorithm(sys.argv[1])