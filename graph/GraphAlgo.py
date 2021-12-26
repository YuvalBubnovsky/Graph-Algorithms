import heapq
import json
import math
from typing import List
from collections import defaultdict
from collections import deque
import sys

from graph.DiGraph import DiGraph
from graph.GraphInterface import GraphInterface
from graph.GraphAlgoInterface import GraphAlgoInterface

import matplotlib.pyplot as plt
import pygame


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = DiGraph()

    @classmethod
    def init_graph(cls, graph: DiGraph):
        DiGraph.init_graph(graph.nodes, graph.edges)

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """loading graph from JSON file
            :param file_name: JSON file to read the graph from
            :return True if graph was loaded successfully, False otherwise"""
        try:
            with open(file_name, "r") as incoming:
                data = json.load(incoming)
                node_data = data.get("Nodes")
                edge_data = data.get("Edges")
                graph = DiGraph()
                for node in node_data:
                    if len(node) == 1:
                        graph.add_node(node.get("id"), (None, None, None))
                    elif len(node) == 2:
                        key = node.get("id")
                        pos = str(node.get("pos"))
                        split_pos = pos.split(',')
                        x = float(split_pos[0])
                        y = float(split_pos[1])
                        z = float(split_pos[2])
                        graph.add_node(key, (x, y, z))
                    for edge in edge_data:
                        src = edge.get("src")
                        weight = edge.get("w")
                        dest = edge.get("dest")
                        graph.add_edge(src, dest, weight)
                        graph.add_rev_edge(dest, src, weight)
                    self.graph = graph
                return True
        except FileExistsError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """writing to JSON file
            :param file_name: The name of the file
            :return True if graph was written successfully, False otherwise"""
        try:
            data = dict()
            nodes = list()
            edges = list()
            curr_nodes = self.graph.get_all_v()
            for node in curr_nodes.values():
                if node.getPosition() != (None, None, None):
                    position = str(node.get_x()) + "," + str(node.get_y()) + "," + str(node.get_z())
                    nodes.append({'id': node.getKey(), 'pos': position})
                else:
                    nodes.append({'id': node.getKey()})
                outgoing_edges = self.graph.all_out_edges_of_node(node.getKey())
                for dest in outgoing_edges.keys():
                    src = node.getKey()
                    weight = outgoing_edges.get(dest)
                    edges.append({'src': src, 'w': weight, 'dest': dest})
            data["Nodes"] = nodes
            data["Edges"] = edges
            with open(file_name, 'w') as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        dijkstra = self.dijkstra(id1)
        dist = dijkstra[0]
        pointers = dijkstra[1]
        temp = id2
        ans = []
        node_id2 = self.graph.nodes.get(id2)

        if node_id2.weight == (float(math.inf)):
            return float(math.inf), []

        while temp != id1:  # inserting the nodes in the correct order
            ans.insert(0, temp)
            temp = pointers.get(temp)

        ans.insert(0, id1)  # adding the first node to the list
        return dist.get(id2), ans

    def dijkstra(self, src):
        self.reset()  # resetting the values of the node's tag and weight before applying a new Dijkstra
        dist = {}  # a dictionary of distance from src to the nodeid in the dictionary
        prev = {}
        visited = {}
        neighbours = [(0, src)]
        dist[src] = 0  # distance from node to itself = 0
        prev[src] = None  # there is no pointer to the node
        visited[src] = True
        self.get_graph().get_all_v().get(src).weight = 0
        while not len(neighbours) == 0:
            temp = heapq.heappop(neighbours)  # temp value - int
            for nodeid in self.graph.all_out_edges_of_node(temp[1]).keys():
                if self.relax(temp[1], nodeid):
                    dist[nodeid] = self.get_graph().get_all_v().get(
                        nodeid).weight  # if we could update - updating the weight of the node int the dict
                    prev[nodeid] = temp[1]  # temp pointing to nodeid
                if nodeid not in visited.keys():
                    visited[nodeid] = True  # marked as visited
                    heapq.heappush(neighbours,
                                   (self.get_graph().get_all_v().get(nodeid).weight, nodeid))  # adding it to the queue

        return dist, prev

    def relax(self, src: int, dest: int) -> bool:
        srcweight = self.get_graph().get_all_v().get(src).weight
        edgeweight = self.get_graph().all_out_edges_of_node(src).get(dest)

        if self.get_graph().get_all_v().get(dest).weight <= srcweight + edgeweight:
            return False

        self.get_graph().get_all_v().get(dest).weight = srcweight + edgeweight
        return True

    def reset(self):
        for node in self.get_graph().get_all_v().values():
            node.weight = math.inf

    def plot_graph(self) -> None:
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        if self.is_connected():
            infinite = float("inf")
            min_distance = sys.float_info.max
            node_id = -1
            for vertex in self.get_graph().get_all_v():
                curr_node = vertex
                max_distance = sys.float_info.min
                for node in self.get_graph().get_all_v():
                    if node == vertex:
                        continue
                    next_node = node
                    dijkstra = self.shortest_path(curr_node, next_node)
                    tmp = dijkstra[0]
                    if dijkstra[0] is not infinite:
                        if tmp > max_distance:
                            max_distance = tmp
                        if tmp > min_distance:
                            break

                if min_distance > max_distance:
                    min_distance = max_distance
                    node_id = vertex

            return node_id, min_distance
        else:
            return None, float('inf')

    def DFS(self, v: int, b: bool):
        stack = deque()
        stack.append(self.graph.nodes.get(v))
        flag = True
        while flag:
            if stack:
                v = stack.pop()
                if self.graph.get_node(v.getKey()).getTag() == 1:
                    continue
                self.graph.get_node(v.getKey()).setTag(1)

                if b:
                    u = self.graph.all_out_edges_of_node(v.getKey())
                else:
                    u = self.graph.all_out_edges_of_rev_node(v.getKey())
                for e in u.keys():
                    if self.graph.get_node(e).getTag() == 0:
                        stack.append(self.graph.get_node(e))
            else:
                flag = False

    def is_connected(self) -> bool:
        self.graph.reset_tags()
        it = iter(self.graph.nodes)
        v = next(it)
        self.DFS(v, True)
        for node in it:
            if self.graph.get_node(node).getTag() == 0:
                return False

        it2 = iter(self.graph.nodes)
        self.DFS(v, False)
        for node2 in it2:
            if self.graph.get_node(node2).getTag() == 0:
                return False

            return True
