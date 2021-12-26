import json
from asyncio import PriorityQueue
from typing import List
from collections import defaultdict
from collections import deque

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
        parents = []
        if id1 == id2:
            weight = self.graph.edges.get(id1).get(id2)
            return weight, [id1, id2]
        else:
            weights = self.dijkstra(id1, parents)
            path = self.shortest_path_nodes(id1, id2, parents)
            return weights[id2], path

    def plot_graph(self) -> None:
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        if self.is_connected():
            pass
        else:
            return None, float('inf')
        pass

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


    # TODO: add dijkstra as a separate file/function
    def dijkstra(self, start_node, parents):
        weights = {node : float('inf') for node in range(len(self.graph.nodes))}
        weights[start_node] = 0
        visited = []

        pq = PriorityQueue()
        pq.put((0,start_node))

        while not pq.empty():
            (weight, current) = pq.get()
            visited.append(current.getKey)
            for neighbor in range(len(self.graph.nodes)):
                if self.graph.edges[current.getKey].get(neighbor) != -1:
                    distance = self.graph.edges[current.getKey].get(neighbor)
                    if neighbor not in visited:
                     current_weight = weights[neighbor]
                     new_weight = weights[current] + distance
                     if new_weight < current_weight:
                         pq.put((new_weight, neighbor))
                         weights[neighbor] = new_weight
                         parents.append(neighbor)
        return weights, parents

    def shortest_path_nodes(self ,src, dest, parents):
        path_list = []
        pointer = dest

        while parents[pointer] != -1:
            path_list.insert(0, self.graph.get_node(pointer))
            pointer = parents[pointer]
        if pointer == src:
            path_list.insert(0, src)
        if path_list.pop(0) != src:
            return  None
        else:
            return path_list


    # TODO: add dijkstra as a seperate file/function
