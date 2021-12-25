import collections
import random

from graph.Node import Node
from graph.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        """
            constructor
            :param nodes: nodes of graph- Dictionary where each key is node ID
            ":param edges: edges of graph- Dictionary where each key is src and value is the info of the edge
        """
        self.nodes = {}
        self.edges = {}
        self.edges = collections.defaultdict(dict)
        self.edge_counter = 0
        self.node_counter = 0
        self.mc = 0

    @classmethod
    def init_graph(cls, nodes: dict, edges: dict):
        cls.nodes = nodes
        cls.edges = edges
        cls.edge_counter = len(edges)
        cls.node_counter = len(nodes)
        cls.mc = 0

    def v_size(self) -> int:
        return self.node_counter

    def e_size(self) -> int:
        return self.edge_counter

    def get_all_v(self) -> dict:
        return self.nodes

    def get_all_e(self) -> dict:
        return self.edges

    def get_node(self, n: int) -> Node:
        if self.nodes.get(n):
            return self.nodes.get(n)
        else:
            print("No such node in graph")

    def all_in_edges_of_node(self, id1: int) -> dict:
        id_in_edges = {}
        for edge_src in self.edges.keys():
            if id1 in self.edges[edge_src]:
                id_in_edges.update({edge_src: self.edges[edge_src][id1]})
        return id_in_edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges[id1]

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.nodes.keys() or id2 not in self.nodes.keys() or id1 == id2 or weight <=0 or id1<0 or id2<0:
            return False
        if id1 in self.edges and id2 in self.edges[id1]:
            return False
        if id1 in self.edges:
            self.edges.get(id1).update({id2: weight})
        else:
            self.edges.update({id1: {id2: weight}})
        self.edge_counter += 1
        self.mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if pos is None:
            loc_x = random.randrange(0, 10)
            loc_y = random.randrange(0, 10)
            pos_loc = (loc_x, loc_y, 0)
            new_node = Node(key=node_id, position=pos_loc)
        else:
            new_node = Node(key=node_id, position=pos)
        if new_node.key not in self.nodes.keys():
            self.nodes[new_node.key] = new_node
            self.mc += 1
            self.node_counter += 1
            return True
        else:
            print("This ID Is Already Exist")
            return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes.keys():
            del self.nodes[node_id]
            self.mc += 1
            self.node_counter -= 1
            # delete all edges related to this node
            self.remove_in_edges(node_id)
            self.remove_out_edges(node_id)
            return True
        else:
            print("No Such ID")
            return False

    def remove_in_edges(self, id: int):
        for edge_src in self.edges.keys():
            if id in self.edges[edge_src]:
                del self.edges[edge_src][id]
                self.edge_counter -= 1
                self.mc -= 1

    def remove_out_edges(self, id: int):
        out_edges_len = len(self.edges[id])
        del self.edges[id]
        self.edge_counter -= out_edges_len
        self.mc -= out_edges_len

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.edges.keys() and node_id2 in self.edges.keys():
            del self.edges[node_id1][node_id2]
            self.mc += 1
            self.edge_counter -= 1
            return True
        else:
            print("One Or Both Those ID's Do Not Exist")
            return False

    def reset_tags(self):
        for node in self.nodes:
            node.setTag(0)

    # TODO move this method to be help method of algorithms methods
    # def reverse_edges(self, edges: dict):
    #     reversed_edges = {}
    #     for edge_src in edges.keys():
    #         # edge_copy = copy.copy(edge)
    #         # temp = edge_copy.src
    #         # edge_copy.src = edge_copy.dest
    #         # edge_copy.dest = temp
    #         for edge_dest in edges.get(edge_src):
    #             reversed_edge = {edge_src: self.edges[edge_src][edge_dest]}
    #             reversed_edges.update({edge_dest: reversed_edge})
    #     return reversed_edges
