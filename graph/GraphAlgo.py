import json
from typing import List

from api.GraphAlgoInterface import GraphAlgoInterface
from api.GraphInterface import GraphInterface
import copy


class GraphAlgo(GraphAlgoInterface):

    def get_graph(self) -> GraphInterface:
        pass

    def load_from_json(self, file_name: str) -> bool:
        """loading graph from JSON file"""
        try:
            with open(file_name, "r") as data:
                pass
        except FileExistsError as e:
            print(e)
        return True

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass
