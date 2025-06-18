# Graphtune: AI-Assisted Graph Algorithm Scheduler

Graphtune is a lightweight demo of a graph algorithm scheduler based on graph structural features and a machine learning model (XGBoost).

Its goal is to automatically select the most suitable basic graph algorithm—such as BFS, Dijkstra, or Greedy Coloring—based on the structural properties of the input graph, with fast and scalable training and prediction capabilities.

---

## Project Highlights

- Automatically extracts structural features of graphs (number of nodes, density, connectivity, cycle detection, etc.)  
- Uses a trained classifier model to enable intelligent graph→algorithm scheduling  
- Supports batch graph generation, experiment execution, label extraction, and prediction testing  
- Fast model training and prediction using XGBoost (can be replaced with other frameworks)  
- Clear project structure with less than 200 lines of core logic code  

---

## Project Structure

Graphtune/  
├── core/                        # Feature extraction, scheduling strategy, algorithm implementation  
│   ├── extractor.py  
│   ├── scheduler.py  
│   └── algorithms.py  
│  
├── experiments/                # Experiment scripts, training logic, data processing  
│   ├── generate_graphs.py  
│   ├── runner.py  
│   ├── generate_dataset.py  
│   ├── train_model.py  
│   └── predict.py  
│  
├── experiments/sample_graphs/  # Auto-generated training graph samples  
├── experiments/data/           # Auto-generated training datasets  
├── experiments/model/          # Trained model storage  
└── README.md  

---

## Quick Start

1. Install dependencies (recommended: Poetry)

poetry install

2. Generate training graphs

poetry run python experiments/generate_graphs.py

3. Run experiments and generate dataset

poetry run python -m experiments.runner  
poetry run python -m experiments.generate_dataset

4. Train the model

poetry run python experiments/train_model.py

5. Predict on a new graph

poetry run python -m experiments.predict experiments/new_graphs/test1.json

---

## Currently Supported Algorithms

- bfs: Breadth-First Search  
- dijkstra: Dijkstra's Shortest Path Algorithm  
- greedy_coloring: Greedy Graph Coloring Algorithm  

You can add more algorithms in core/algorithms.py.

---

## Inspiration

This project was inspired by a math video from a creator who analyzed a Beijing entrance exam problem using graph theory.

She insightfully examined the structural constraints of corner points, central points, and valid paths on a chessboard, and visualized it with beautifully crafted manim animations—highlighting the elegance of structure-driven reasoning in graph problems.

This kind of “structure analysis drives path selection” perspective directly inspired my approach to modeling graph scheduling problems.

**If you like this project, you don’t need to give me a star—go give her video a like and a comment such as "nice work" (you may need to register an account). She truly needs and deserves the support.**

Video link: [Her video on Bilibili](https://www.bilibili.com/video/BV1WsMCzeEQg/?share_source=copy_web&vd_source=85f963e4809e9f61e962ddb24223fc4d)

---

## Future Directions

- Add GNN-based deep model schedulers  
- Introduce more graph features and algorithms  
- Try integrating into a graph platform or online tool  

---

## License

MIT License. Feel free to use and extend.