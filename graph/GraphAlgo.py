import json
from typing import List, Type

from api.GraphAlgoInterface import GraphAlgoInterface
from api.GraphInterface import GraphInterface
import graph.DiGraph
import copy


class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = graph.DiGraph.DiGraph()

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """loading graph from JSON file
            :param file_name: JSON file to read the graph from
            :return True if graph was loaded successfully, False otherwise"""
        try:
            with open(file_name, "r") as data:
                object_dada = json.load(data)
                self.graph.edges = object_dada["Edges"]
                self.graph.nodes = object_dada["Nodes"]
                return True
        except FileExistsError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """writing to JSON file
            :param file_name: The name of the file
            :return True if graph was written successfully, False otherwise"""
        try:
            data = {"Edges": [], "Nodes": []}
            data["Edges"].append(edge for edge in self.graph.get_all_e())
            data["Nodes"].append(node for node in self.graph.get_all_v())
            with open('graph.json', 'w') as outfile:
                json.dump(data, outfile, indent=4, sort_keys=True)
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
        pass
