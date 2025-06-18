# Graphtune：AI辅助图调度器

Graphtune 是一个基于图结构特征与机器学习模型（XGBoost）的轻量级图算法调度器 Demo。

它的目标是根据输入图的结构特征，自动选择最合适的基础图算法进行处理，如 BFS、Dijkstra 或 Greedy Coloring，具备快速、可扩展的训练与预测能力。

---

## 项目亮点

- 自动提取图结构特征（节点数、密度、连通性、环检测等）  
- 使用训练好的分类器模型，实现图→算法的智能调度  
- 支持批量图生成、实验执行、标签提取与预测测试  
- 使用 XGBoost 实现快速模型训练与预测（也可替换为其他框架）  
- 项目结构清晰，核心逻辑代码量小于 200 行  

---

## 项目结构

Graphtune/
├── core/                        # 特征提取、调度策略、算法实现  
│   ├── extractor.py  
│   ├── scheduler.py  
│   └── algorithms.py  
│  
├── experiments/                # 实验脚本、训练逻辑、数据处理  
│   ├── generate_graphs.py  
│   ├── runner.py  
│   ├── generate_dataset.py  
│   ├── train_model.py  
│   └── predict.py  
│  
├── experiments/sample_graphs/  # 自动生成的训练图样本  
├── experiments/data/           # 自动生成的训练数据集  
├── experiments/model/          # 存储训练好的模型  
└── README.md  

---

## 快速开始

1. 安装依赖（推荐使用 Poetry 管理）

poetry install

2. 生成训练图

poetry run python experiments/generate_graphs.py

3. 执行实验、生成数据集

poetry run python -m experiments.runner  
poetry run python -m experiments.generate_dataset

4. 训练模型

poetry run python experiments/train_model.py

5. 对新图进行预测

poetry run python -m experiments.predict experiments/new_graphs/test1.json

---

## 当前支持的图算法

- bfs：广度优先搜索  
- dijkstra：Dijkstra 最短路径算法  
- greedy_coloring：贪心图染色算法  

你可以在 core/algorithms.py 中添加更多算法。

---

## 灵感来源

本项目的灵感，来自于一位数学博主讲解的一道北京高考题。她用极具洞察力的方式分析了棋盘中角落点、中间点与路径结构之间的限制关系，并配合精美的 manim 动画讲解，展现出图论问题中结构约束的美感。

这种“结构分析驱动路径选择”的方式，直接启发了我对图结构调度问题的建模方法。

**如果你喜欢这个项目，不必给我 star，不如去给她的视频点一个赞，留一句 nice work（可能需要注册账号），她真的非常需要鼓励和支持。**

视频链接:[她的视频在bilibili](https://www.bilibili.com/video/BV1WsMCzeEQg/?share_source=copy_web&vd_source=85f963e4809e9f61e962ddb24223fc4d)

---

## 后续方向

- 支持 GNN 等深度模型调度器  
- 引入更多图结构特征与算法  
- 尝试集成为图平台或在线工具  

---

## 许可证

MIT License，欢迎使用与拓展。