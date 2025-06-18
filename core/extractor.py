import networkx as nx

def build_graph(graph_json):
    G = nx.DiGraph() if graph_json.get("directed", False) else nx.Graph()
    G.add_edges_from(graph_json["edges"])
    return G

def extract_features(G):
    features = {}

    features["num_nodes"] = G.number_of_nodes()
    features["num_edges"] = G.number_of_edges()

    if features["num_nodes"] > 1:
        features["density"] = nx.density(G)
    else:
        features["density"] = 0

    degrees = [d for _, d in G.degree()]
    features["avg_degree"] = sum(degrees) / len(degrees) if degrees else 0
    features["max_degree"] = max(degrees) if degrees else 0

    try:
        features["clustering_coef"] = nx.average_clustering(G)
    except:
        features["clustering_coef"] = 0

    if G.is_directed():
        features["is_directed"] = True
        components = list(nx.strongly_connected_components(G))
    else:
        features["is_directed"] = False
        components = list(nx.connected_components(G))

    features["num_components"] = len(components)
    features["is_connected"] = (len(components) == 1)

    try:
        cycles = list(nx.find_cycle(G, orientation="ignore"))
        features["has_cycle"] = True if cycles else False
    except:
        features["has_cycle"] = False

    return features