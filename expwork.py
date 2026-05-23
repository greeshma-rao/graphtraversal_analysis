import time
import tracemalloc
import csv
from bfs import bfs
from dfs import dfs
from graph_generator import generate_sparse_graph, generate_dense_graph, generate_tree

def measure_performance(graph, algorithm):
    adj = {node: list(graph.neighbors(node)) for node in graph.nodes()}

    start_node = list(adj.keys())[0]

    tracemalloc.start()
    start_time = time.time()

    algorithm(adj, start_node)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return end_time - start_time, peak

def run_experiment():
    sizes = [100, 1000, 3000]
    
    with open("/results/raw_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Nodes", "Algorithm", "Time", "Memory"])

        for n in sizes:
            for graph_type, generator in [
                ("Sparse", generate_sparse_graph),
                ("Dense", generate_dense_graph),
                ("Tree", generate_tree)
            ]:
                graph = generator(n)

                bfs_time, bfs_mem = measure_performance(graph, bfs)
                dfs_time, dfs_mem = measure_performance(graph, dfs)

                writer.writerow([graph_type, n, "BFS", bfs_time, bfs_mem])
                writer.writerow([graph_type, n, "DFS", dfs_time, dfs_mem])

if __name__ == "__main__":
    run_experiment()