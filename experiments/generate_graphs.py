import os
import json
import random
import networkx as nx
from tqdm import tqdm

OUTPUT_DIR = "experiments/sample_graphs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_erdos_graph(i):
    n = random.randint(10, 50)
    p = round(random.uniform(0.1, 0.3), 2)
    G = nx.erdos_renyi_graph(n, p)
    return G

def generate_barabasi_graph(i):
    n = random.randint(10, 50)
    m = random.randint(1, min(5, n - 1))
    G = nx.barabasi_albert_graph(n, m)
    return G

def generate_watts_graph(i):
    n = random.randint(10, 50)
    k = random.randint(2, 6)
    p = round(random.uniform(0.1, 0.3), 2)
    G = nx.watts_strogatz_graph(n, k, p)
    return G

def generate_grid_graph(i):
    rows = random.randint(3, 8)
    cols = random.randint(3, 8)
    G = nx.grid_2d_graph(rows, cols)
    G = nx.convert_node_labels_to_integers(G)
    return G

def generate_tree_graph(i):
    r = random.randint(2, 4)
    h = random.randint(3, 6)
    G = nx.balanced_tree(r, h)
    return G

def save_graph(i, G):
    data = {
        "directed": G.is_directed(),
        "edges": list(G.edges())
    }
    with open(os.path.join(OUTPUT_DIR, f"g{i}.json"), "w") as f:
        json.dump(data, f)

def main():
    generators = [
        generate_erdos_graph,
        generate_barabasi_graph,
        generate_watts_graph,
        generate_grid_graph,
        generate_tree_graph
    ]
    count_per_type = 2000
    total = count_per_type * len(generators)
    idx = 0
    for gen in generators:
        for _ in tqdm(range(count_per_type), desc=f"Generating {gen.__name__}"):
            G = gen(idx)
            if len(G.edges) > 0:
                save_graph(idx, G)
                idx += 1
    print(f"[✓] Generated {idx} graphs to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()