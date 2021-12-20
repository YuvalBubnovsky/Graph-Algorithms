from api.GraphInterface import GraphInterface
from graph import Node, Edge
import copy


class diGraph(GraphInterface):

    def __init__(self, nodes: dict, edges: dict):
        """
            constructor
            :param nodes: nodes of graph- Dictionary where each key is node ID
            ":param edges: edges of graph- Dictionary where each key is src and value is the info of the edge
        """
        self.nodes = nodes
        self.edges = edges
        self.reversed_edges = {}
        self.mc = 0

    # @classmethod
    # def init_graph(self):
    #     Nodes = {}
    #     Edges = {}
    #     reversed_edges = {}
    #     edgeCounter: int
    #     modCount: int
    # TODO is needed?

    def v_size(self) -> int:
        return len(self.nodes.keys())

    def e_size(self) -> int:
        return len(self.edges.keys())

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        pass

    def all_out_edges_of_node(self, id1: int) -> dict:
        pass

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        new_edge = Edge.Edge(src=id1, dest=id2, weight=weight)
        self.edges[new_edge[new_edge.src]] = new_edge
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        new_node = Node.Node(key= node_id, position= pos)
        try:
            if new_node.key not in self.nodes.keys():
                self.nodes.update({new_node.key, new_node})
                return True
            else:
                raise ValueError("This ID Is Already Exist")
        except ValueError as e:
            print(e)
            return False

    def remove_node(self, node_id: int) -> bool:
        try:
            del self.nodes[node_id]
            return True
        except KeyError or IndexError as e:
            print("No Such ID")
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        try:
            if node_id1 in self.nodes.keys() and node_id2 in self.nodes.keys():
                del self.edges[node_id1][node_id2]
                return True
            else: raise Exception("One Or Both Those ID's Do Not Exist")
        except Exception as e:
            print(e)
            return False

    def reverse_edges(self):
        for edge in self.edges:
            edge_copy = edge.copyEdge()
            temp = edge_copy.src
            edge_copy.src = edge_copy.dest
            edge_copy.dest = temp
            reversed_edge = {edge_copy.src: edge_copy}
            self.reversed_edges.update(reversed_edge)
