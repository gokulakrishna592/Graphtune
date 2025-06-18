import time
import networkx as nx

def dijkstra_algorithm(G, source=0):
    start_time = time.time()
    try:
        lengths = nx.single_source_dijkstra_path_length(G, source)
    except Exception as e:
        return {"error": str(e), "time": 0}
    duration = time.time() - start_time
    return {"result": lengths, "time": duration}

def bfs_algorithm(G, source=0):
    start_time = time.time()
    try:
        bfs_tree = list(nx.bfs_edges(G, source))
    except Exception as e:
        return {"error": str(e), "time": 0}
    duration = time.time() - start_time
    return {"result": bfs_tree, "time": duration}

def greedy_coloring_algorithm(G):
    start_time = time.time()
    try:
        coloring = nx.coloring.greedy_color(G, strategy="largest_first")
    except Exception as e:
        return {"error": str(e), "time": 0}
    duration = time.time() - start_time
    return {"result": coloring, "time": duration}

def run_algorithm(G, algo_name, **kwargs):
    if algo_name == "dijkstra":
        return dijkstra_algorithm(G, **kwargs)
    elif algo_name == "bfs":
        return bfs_algorithm(G, **kwargs)
    elif algo_name == "greedy_coloring":
        return greedy_coloring_algorithm(G)
    else:
        return {"error": f"Unknown algorithm '{algo_name}'"}