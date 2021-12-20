from api.GraphInterface import GraphInterface
import copy


class diGraph(GraphInterface):

    def __init__(self, nodes : dict, edges: dict):
        """
            constructor
            :param nodes: nodes of graph
            ":param edges: edges of graph
        """
        self.nodes = nodes
        self.edges = edges
        self.mc = 0

    @classmethod
    def init_graph(self):
        pass
    # TODO is needed?

    def v_size(self) -> int:
        return len(self.nodes.keys())

    def e_size(self) -> int:
        return len(self.edges.keys())

    def get_all_v(self) -> dict:
        pass

    def all_in_edges_of_node(self, id1: int) -> dict:
        pass

    def all_out_edges_of_node(self, id1: int) -> dict:
        pass

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        pass

    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass