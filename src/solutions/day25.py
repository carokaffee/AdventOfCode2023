from src.tools.loader import load_data
import networkx as nx
from itertools import combinations

TESTING = False


def parse_input(data):
    edges = dict()
    for line in data:
        source = line.split(": ")[0]
        dests = list(line.split(": ")[1].split())
        edges[source] = dests
    return edges


def find_partition(edges):
    edges = parse_input(data)
    G = nx.Graph(edges)
    for edge in G.edges:
        G.edges[edge]["capacity"] = 1
    for s, t in combinations(G.nodes, 2):
        cut_value, partition = nx.minimum_cut(G, s, t)
        if cut_value == 3:
            res = len(partition[0]) * len(partition[1])
            break
    return res


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    edges = parse_input(data)

    # PART 1
    # test:       54
    # answer: 603368
    print(find_partition(edges))
