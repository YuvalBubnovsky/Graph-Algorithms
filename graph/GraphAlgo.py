import json
from typing import List
from collections import defaultdict
from collections import deque

from graph.DiGraph import DiGraph
from graph.GraphInterface import GraphInterface
from graph.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = DiGraph()

    def init_graph(self, graph: DiGraph):
        self.graph = graph

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
        pass

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

    def transpose(self) -> dict:
        graph_inv = defaultdict(list)

        for src in self.graph.get_all_e():
            for dest in self.graph.edges.get(src).keys():
                graph_inv[dest].append({src: self.graph.edges.get(src).get(dest)})

        return graph_inv

    def DFS(self, v: int):
        stack = deque()
        stack.append(self.graph.nodes.get(v))
        flag = True
        while flag:
            if stack:
                v = stack.pop()
                if self.graph.get_node(v.getKey()).getTag() == 1:
                    continue
                self.graph.get_node(v.getKey()).setTag(1)
                for edge in self.graph.edges:
                    if self.graph.get_node(self.graph.get_node(edge).getTag()) == 0:
                        stack.append(self.graph.get_node(edge.getDest()))
            else:
                flag = False

    def is_connected(self) -> bool:
        self.graph.reset_tags()
        it = iter(self.graph.nodes)
        v = next(it)
        self.DFS(v)
        for node in it:
            if self.graph.get_node(node).getTag() == 0:
                return False

        self.graph.reset_tags()
        rev_edge = self.transpose()
        self.graph.edges = rev_edge

        it2 = iter(self.graph.nodes)
        z = next(it2)
        self.DFS(z)
        for node2 in it2:
            if node2.getTag == 0:
                return False

        rerev_edges = self.transpose()
        self.graph.edges = rerev_edges
        return True

    # TODO: add dijkstra as a seperate file/function

