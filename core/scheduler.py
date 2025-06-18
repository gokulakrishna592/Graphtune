def schedule_algorithm(features):
    if features["num_components"] > 1 or not features["is_connected"]:
        return "greedy_coloring"

    elif features["density"] > 0.4 and features["has_cycle"]:
        return "dijkstra"

    elif features["density"] <= 0.4 and not features["has_cycle"]:
        return "bfs"

    else:
        return "bfs"