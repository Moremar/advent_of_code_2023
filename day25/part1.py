#!/usr/bin/env python3
import os.path
import time
import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Component:
    def __init__(self, name, connected):
        self.name = name
        self.connected = connected


def parse(input_path):
    with open(input_path, 'r') as f:
        components, edges = {}, []
        for line in [l.strip() for l in f.readlines()]:
            tokens = re.findall(r'(\w+)', line)
            name, connected = tokens[0], set(tokens[1:])
            if name not in components:
                components[name] = Component(name, set())
            for adj_name in connected:
                components[name].connected.add(adj_name)
                if adj_name not in components:
                    components[adj_name] = Component(adj_name, set())
                components[adj_name].connected.add(name)
                edges.append((tokens[0], adj_name))
        return components, edges


def get_all_reachable_nodes(start_node, components, edges_to_cut):
    reachable = {start_node}
    to_check = deque([start_node])
    while len(to_check):
        curr = to_check.popleft()
        for adj in components[curr].connected:
            if (adj, curr) in edges_to_cut or (curr, adj) in edges_to_cut:
                continue
            if adj not in reachable:
                reachable.add(adj)
                to_check.append(adj)
    return reachable


def compute(components, edges_to_cut):
    # find all nodes reachable from an arbitrary start node
    start_node = list(components.keys())[0]
    reachable_from_start = get_all_reachable_nodes(start_node, components, edges_to_cut)
    if len(reachable_from_start) == len(components):
        return -1  # all nodes are connected
    # pick a node outside the previous graph, and find all nodes reachable from it
    out_node = None
    for curr in components:
        if curr not in reachable_from_start:
            out_node = curr
            break
    reachable_from_out = get_all_reachable_nodes(out_node, components, edges_to_cut)
    if len(reachable_from_start) + len(reachable_from_out) == len(components):
        return len(reachable_from_start) * len(reachable_from_out)
    return 0  # more than 2 separate sub-graphs


def generate_graph(edges, graph_file):
    graph = nx.Graph()
    graph.add_edges_from(edges)
    figsize = (10, 10) if 'sample' in graph_file else (100, 100)
    plt.figure(figsize=figsize)  # big graph size, so we can zoom on the PNG file
    nx.draw_networkx(graph)
    plt.savefig(graph_file)


def solve(components, edges):
    graph_file = input_file.split('.')[0] + '_graph.png'
    if not os.path.exists(graph_file):
        generate_graph(edges, graph_file)
        print('Created graph', graph_file)
    else:
        # we observe from the graph the edges to cut to create 2 separate connected sub-graphs
        edges_to_cut = {('rtt', 'zcj'), ('tpn', 'gxv'), ('hxq', 'txl')}
        return compute(components, edges_to_cut)


if __name__ == "__main__":
    start = time.time()
    input_file = 'data.txt'
    components, edges = parse(input_file)
    result = solve(components, edges)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
