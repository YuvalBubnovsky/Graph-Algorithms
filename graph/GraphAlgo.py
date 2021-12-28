import heapq
import json
import math
import random
import sys
from collections import deque
from typing import List

import matplotlib.pyplot as plt
import tkinter
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askinteger, askfloat

from graph.DiGraph import DiGraph
from graph.GraphAlgoInterface import GraphAlgoInterface
from graph.GraphInterface import GraphInterface

'''
This class is used to perform various algorithms on the underlying directed weighted graph.
It supports these algorithms:
    * Depth-First Search
    * Dijkstr'a Shortest Path
    * Determining if a graph is strongly connected
    * Finding the center of the graph
    * Augmented TSP 

This class also plots the graph and displays it to the user using tkinter
'''


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, *args):
        if len(args) == 1:
            self.graph = args[0]
        else:
            self.graph = DiGraph()
        self.root = tk.Tk()
        self.min_x = float('inf')
        self.min_y = float('inf')
        self.max_x = -float('inf')
        self.max_y = -float('inf')

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
                graph_load = DiGraph()
                for node in node_data:
                    # If no position is given, set it to None
                    if len(node) == 1:
                        graph_load.add_node(node.get("id"), (None, None, None))

                    elif len(node) == 2:
                        key = node.get("id")
                        pos = str(node.get("pos"))
                        split_pos = pos.split(',')
                        x = float(split_pos[0])
                        y = float(split_pos[1])
                        z = float(split_pos[2])
                        graph_load.add_node(key, (x, y, z))

                    for edge in edge_data:
                        src = edge.get("src")
                        weight = edge.get("w")
                        dest = edge.get("dest")
                        graph_load.add_edge(src, dest, weight)
                        graph_load.add_rev_edge(dest, src, weight)

                    self.graph = graph_load
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
        # Running dijkstr'a algorithm to get all weights of paths from the source node and also the parent dictionary
        # to reconstruct the shortest path
        dijkstraResult = self.dijkstra(id1)
        dist = dijkstraResult[0]
        pointers = dijkstraResult[1]
        temp = id2
        path = []
        node = self.graph.nodes.get(id2)

        if node.weight == (float(math.inf)):
            return float(math.inf), []

        # We insert all nodes in the correct order
        while temp != id1:
            path.insert(0, temp)
            temp = pointers.get(temp)

        # inserting the source node to the list and return the result
        path.insert(0, id1)
        return dist.get(id2), path

    # Dijkstra's shortest path algorithm, we
    def dijkstra(self, src):
        # we introduce a new attribute to the nodes - weight, we will use this attribute to run Dijkstr'a algorithm
        # the reset function sets all the weight of the nodes in the graph to positive infinity
        self.d_prepare()

        # initializing dictionaries & lists
        distances = {}
        parents = {}
        visited = {}
        neighbours = [(0, src)]

        # a distance from the node to itself is 0
        distances[src] = 0

        # the source pointer has no "parent"
        parents[src] = None
        visited[src] = True

        # setting the source node's weight to 0
        self.graph.get_node(src).weight = 0

        """
        The "classic" dijkstra implementation using python's built in priority queue library Dijkstra's algorithm 
        will initially start with infinite distances and will try to improve them step by step. Mark all nodes 
        unvisited. Create a set of all the unvisited nodes called the unvisited set. Assign to every node a distance 
        value: set it to zero for our initial node and to infinity for all other nodes. For the current node, 
        consider all of its unvisited neighbors and calculate their distances through the current node. Compare the 
        newly calculated distance to the current assigned value and assign the smaller one. When we are done 
        considering all of the unvisited neighbors of the current node, mark the current node as visited and remove 
        it from the unvisited set. A visited node will never be checked again. If the destination has been marked 
        visited, we are done, otherwise, keep going. 
        """

        while not len(neighbours) == 0:
            temp = heapq.heappop(neighbours)
            for source_id in self.graph.all_out_edges_of_node(temp[1]).keys():
                if self.relax(temp[1], source_id):
                    distances[source_id] = self.get_graph().get_all_v().get(source_id).weight
                    parents[source_id] = temp[1]
                if source_id not in visited.keys():
                    visited[source_id] = True
                    heapq.heappush(neighbours,
                                   (self.get_graph().get_all_v().get(source_id).weight, source_id))

        return distances, parents

    # helper relax function for dijkstr'a algorithm,
    # For the edge from the vertex u to the vertex v, if d[u]+w(u,v)<d[v] is satisfied, update d[v] to d[u]+w(u,v)
    def relax(self, src: int, dest: int) -> bool:
        src_weight = self.get_graph().get_all_v().get(src).weight
        destination_weight = self.get_graph().all_out_edges_of_node(src).get(dest)

        if self.graph.get_node(dest).weight <= src_weight + destination_weight:
            return False

        self.graph.get_node(dest).weight = src_weight + destination_weight
        return True

    # preparation function, sets all node weight to infinity
    def d_prepare(self):
        for node in self.get_graph().get_all_v().values():
            node.weight = math.inf

    """
    Augmented TSP algorithm, given a list of nodes in the graph, calculate
    a path which visits all nodes - we can visit each node more than once and also
    travel through other nodes in the graph which are not in the list
    We use nearest neighbour approximation algorithm here
    """
    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if node_lst is None or len(node_lst) == 0:
            return None

        nearest_neighbour = node_lst[0]
        path = []
        total_path_weight = 0

        # We keep going as long as there's more than 1 node in our list
        # One node is not enough to calculate TSP solution
        while len(node_lst) > 1:
            node_lst.remove(nearest_neighbour)
            min_length = math.inf
            temp_path = []
            for city in range(len(node_lst)):
                temp = self.shortest_path(nearest_neighbour, node_lst[city])
                if temp[0] == math.inf:
                    break
                if temp[0] < min_length:
                    min_length = temp[0]
                    temp_path = temp[1]
                    current_node = node_lst[city]

            if len(path) == 0:
                path.extend(temp_path)
            else:
                temp_path.pop(0)
                path.extend(temp_path)

            total_path_weight = total_path_weight + min_length
            nearest_neighbour = current_node

        return path, total_path_weight

    """
    This algorithm returns the center point of the graph, first we check if the graph is even strongly connected -
    otherwise it has no center node ( We do this by running DFS twice from the same node while transposing the graph )
    Then, we run dijkstr'a algorithm for each node to determine it's maximum distance and then return the minimum
    value related to said node - that is the center.
    """
    def centerPoint(self) -> (int, float):
        # first, we make sure the graph is strongly connected
        if self.is_connected():
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

                    if dijkstra[0] is not float('inf'):
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

    # A simple DFS implementation using a double-edged queue acting as a stack
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

    """
    All functions below this point are used to plot the graph using python's tkinter
    """

    def plot_graph(self) -> None:

        self.root.geometry("750x650")
        self.root.title("Graph App")
        self.root.eval('tk::PlaceWindow . center')
        self.root.resizable(False, False)
        # self.plot_graph()
        load_button = tkinter.Button(self.root, text="load graph", command=self.load_graph, fg='red')
        load_button.place(x=0, y=0)
        save_button = tkinter.Button(self.root, text="save graph", command=self.save_graph, fg='red')
        save_button.place(x=68, y=0)
        short_path_button = tkinter.Button(self.root, text="shortest path", command=self.short_path, fg='red')
        short_path_button.place(x=136, y=0)
        tsp_button = tkinter.Button(self.root, text="TSP", command=self.tsp, fg='red')
        tsp_button.place(x=216, y=0)
        center_button = tkinter.Button(self.root, text="center point", command=self.center, fg='red')
        center_button.place(x=248, y=0)
        connected_button = tkinter.Button(self.root, text="is connected", command=self.connected, fg='red')
        connected_button.place(x=322, y=0)
        add_node_button = tkinter.Button(self.root, text="add vertex", command=self.add_node, fg='red')
        add_node_button.place(x=397, y=0)
        add_edge_button = tkinter.Button(self.root, text="add edge", command=self.add_edge, fg='red')
        add_edge_button.place(x=462, y=0)
        remove_node_button = tkinter.Button(self.root, text="remove vertex", command=self.remove_node, fg='red')
        remove_node_button.place(x=522, y=0)
        remove_edge_button = tkinter.Button(self.root, text="remove edge", command=self.remove_edge, fg='red')
        remove_edge_button.place(x=606, y=0)

        self.refresh()
        self.root.mainloop()

    def refresh(self):
        """
        This method responsibility is to plot the graph on the tkinter window.
        This method is called each time a vertex or edge are added
        """
        figure = plt.figure(figsize=(7.5, 6))
        canvas = FigureCanvasTkAgg(figure=figure, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=23)
        self.min_max_calculate()
        x_pos, y_pos = self.scaling_positions(self.min_x, self.min_y, self.max_x, self.max_y)

        # adding random positions if nodes have no positions (like in T0)
        if not bool(x_pos) and not bool(y_pos):
            for node in self.graph.get_all_v():
                current = self.graph.get_node(node)
                current.setPosition([random.randrange(0, 30), random.randrange(0, 30), 0])
            self.min_max_calculate()
            x_pos, y_pos = self.scaling_positions(self.min_x, self.min_y, self.max_x, self.max_y)

        # plot nodes
        i = 0
        for curr in x_pos:
            plt.plot(x_pos.get(curr), y_pos.get(curr), markersize=10, marker='o', color='red')
            plt.text(x=x_pos.get(curr) - 1.5, y=y_pos.get(curr) - 3.5, s=str(i), color='black')
            i += 1

            # plot edges
            # if len(x_pos) == 0 and len(y_pos) == 0:
            for node in self.graph.get_all_v().keys():
                all_out_edges = self.graph.all_out_edges_of_node(node)
                x_src = x_pos.get(node)
                y_src = y_pos.get(node)
                for edge in all_out_edges:
                    x_dest = x_pos.get(edge)
                    y_dest = y_pos.get(edge)
                    plt.annotate("", xy=(x_dest, y_dest), xytext=(x_src, y_src),
                                 arrowprops=dict(arrowstyle="->"))
                    # plot weights
                    weight = all_out_edges.get(edge)
                    weight = '{0:.4f}'.format(weight)
                    plt.text(x=x_src * 0.7 + x_dest * 0.3, y=y_src * 0.72 + y_dest * 0.32, s=str(weight))

        plt.show()

    # the following methods are responsible to handle clicks on buttons
    def load_graph(self):
        file_name = filedialog.askopenfilename(title="Open file", initialdir='/../../PycharmProjects',
                                               filetypes=(('json files', '*.json'), ('All files', '*.*')))
        self.load_from_json(file_name)
        self.refresh()

    def save_graph(self):
        file_name = filedialog.asksaveasfile(title="Save file", initialdir='/../../PycharmProjects',
                                             filetypes=(('json files', '*.json'), ('All files', '*.*')))
        result = self.save_to_json(file_name.name)
        if result:
            showinfo(title="message", message="Graph was saved successfully")
        else:
            showinfo(title="message", message="Graph was not saved successfully")

    def short_path(self):
        src = askinteger(title="Source", prompt="Enter Source Node")
        dest = askinteger(title="Destination", prompt="Enter Destination Node")
        dist = self.shortest_path(src, dest)[0]
        path = self.shortest_path(src, dest)[1]
        path_str = ""
        for node in path:
            path_str += str(node)
            path_str += "->"
        path_str = path_str[:-2]
        showinfo(title="shortest path",
                 message="Shortest Path Dist Is: {dist}, Path is: {path} ".format(dist=dist, path=path_str))

    def tsp(self):
        node_list = []
        node = askinteger(title="enter node", prompt="Enter Node ID, to finish press -1")
        while node != -1:
            if node > 0 and node in self.graph.nodes.keys():
                node_list.append(node)
                node = askinteger(title="enter node", prompt="Enter Another Node ID, to finish press -1")
            # elif node not in self.graph.nodes.keys():
            #     showinfo(title="Error", message="No Such ID")
            #     node = askinteger(title="enter node", prompt="Enter Another Node ID, to finish press -1")
            else:
                showinfo(title="Error", message="invalid id, whether id does not exist or negative ID was entered")
                node = askinteger(title="enter node", prompt="Enter Another Node ID, to finish press -1")
        tsp_result = self.TSP(node_lst=node_list)
        path = tsp_result[0]
        dist = tsp_result[1]
        if len(path) == 0:
            showinfo(title="TSP", message="There is no path between those nodes")
        path_str = ""
        for node in path:
            path_str += str(node)
            path_str += "->"
        path_str = path_str[:-2]
        showinfo(title="TSP", message="TSP Dist Is: {dist}, Path is: {path} ".format(dist=dist, path=path_str))

    def center(self):
        result = self.centerPoint()
        center_node = result[0]
        min_distance = result[1]
        showinfo(title="center",
                 message="Center Vertex is: {vertex}, minimum distance is {dis}".format(vertex=center_node,
                                                                                        dis=min_distance))

    def connected(self):
        result = self.is_connected()
        if result:
            showinfo(title="Is Connected", message="The Graph Is Connected")
        else:
            showinfo(title="Is Connected", message="The Graph Is Not Connected")

    def add_node(self):
        key = self.graph.node_counter
        showinfo(title="key", message="the key of the new vertex is: {key}".format(key=key))
        x = askfloat(title="X", prompt="Enter X position")
        y = askfloat(title="Y", prompt="Enter Y position")

        # x, y = self.linear_transform(x, y)

        self.graph.add_node(key, (x, y, 0))

        self.refresh()

    def add_edge(self):
        src = askinteger(title="Source", prompt="Enter Source node ID")
        dest = askinteger(title="Destination", prompt="Enter destination node ID")
        weight = askfloat(title="Weight", prompt="Enter Weight")
        self.graph.add_edge(src, dest, weight)

        self.refresh()

    def remove_node(self):
        key = askinteger(title="ID", prompt="Enter ID")
        self.graph.remove_node(key)

        self.refresh()

    def remove_edge(self):
        src = askinteger(title="Source", prompt="Enter Source node ID")
        dest = askinteger(title="Destination", prompt="Enter destination node ID")

        self.graph.remove_edge(src, dest)

        self.refresh()

    def min_max_calculate(self):
        for node in self.graph.get_all_v().keys():
            # min_x
            if self.graph.get_node(node).getPosition().get_x() is not None:
                if self.graph.get_node(node).getPosition().get_x() < self.min_x:
                    self.min_x = self.graph.get_node(node).getPosition().get_x()
            # min_y
            if self.graph.get_node(node).getPosition().get_y() is not None:
                if self.graph.get_node(node).getPosition().get_y() < self.min_y:
                    self.min_y = self.graph.get_node(node).getPosition().get_y()
            # max_x
            if self.graph.get_node(node).getPosition().get_x() is not None:
                if self.graph.get_node(node).getPosition().get_x() > self.max_x:
                    self.max_x = self.graph.get_node(node).getPosition().get_x()
            # max_y
            if self.graph.get_node(node).getPosition().get_y() is not None:
                if self.graph.get_node(node).getPosition().get_y() > self.max_y:
                    self.max_y = self.graph.get_node(node).getPosition().get_y()

        # return [min_x, min_y, max_x, max_y]

    def scaling_positions(self, min_x, min_y, max_x, max_y):
        x_pos = {}
        y_pos = {}
        all_nodes = self.graph.get_all_v()

        scale_x = 1000 / (max_x - min_x) * 0.9
        scale_y = 1000 / (max_y - min_y) * 0.9
        for node in all_nodes.keys():
            if self.graph.get_node(node).get_x() is not None:
                x = (self.graph.get_node(node).get_x() - min_x) * scale_x + 30
                x_pos[node] = int(x)
            if self.graph.get_node(node).get_y() is not None:
                y = (self.graph.get_node(node).get_y() - min_y) * scale_y + 90
                y_pos[node] = int(y)
            # x_pos[node] = int(x)
            # y_pos[node] = int(y)

        return x_pos, y_pos

    def linear_transform(self, x, y):
        x_value = self.max_x - x
        calculated_x = self.max_x - self.min_x
        y_value = self.max_y - y
        calculated_y = self.max_y - self.min_y
        final_x = x_value / calculated_x * 0.68
        final_y = y_value / calculated_y * 0.68
        return final_x, final_y


if __name__ == '__main__':
    graph = GraphAlgo()
    graph.load_from_json(r"C:\Users\yuval\PycharmProjects\OOP_2021_Ex3\data\A0.json")
    graph.plot_graph()
