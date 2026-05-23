import networkx as nx

def generate_sparse_graph(n):
    return nx.erdos_renyi_graph(n, 0.01)

def generate_dense_graph(n):
    return nx.erdos_renyi_graph(n, 0.5)

def generate_tree(n):
    return nx.random_labeled_tree(n)