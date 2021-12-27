import heapq
import json
import math
import tkinter
from typing import List
from collections import defaultdict
from collections import deque
import sys
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter.simpledialog import askstring, askinteger
from tkinter.messagebox import showinfo

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from graph.DiGraph import DiGraph
from graph.GraphInterface import GraphInterface
from graph.GraphAlgoInterface import GraphAlgoInterface


# from graph import GUI

class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = DiGraph()
        self.root = tk.Tk()

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

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if node_lst is None or len(node_lst) == 0:
            return None

        nextcity = node_lst[0]  # the closest next city, starting with the first city in the list
        path = []  # the total path
        overAllLength = 0  # the length of the total path (weight)
        while len(node_lst) - 1 > 0:
            node_lst.remove(nextcity)  # removing the first city in the current list
            minlength = math.inf
            currpath = []  # temp path
            for city in range(len(node_lst)):
                temp = self.shortest_path(nextcity, node_lst[
                    city])  # temp is a tuple that contains the length and list of the path
                if temp[0] == math.inf:
                    break
                if temp[0] < minlength:
                    minlength = temp[0]
                    currpath = temp[1]
                    currcity = node_lst[city]

            if len(path) == 0:
                path.extend(currpath)  # adding the path to the end of the list
            else:
                currpath.pop(0)
                path.extend(
                    currpath)  # adding the path to the end of the list without the first one in order to avoid duplicates

            overAllLength = overAllLength + minlength  # adding the length of current path to the total path length
            nextcity = currcity

        return path, overAllLength

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

        figure = plt.figure(figsize=(7.5, 6))
        # # plot = figure.subplots()
        # # canvas = FigureCanvasTkAgg(figure, master=self.root)
        # # canvas.get_tk_widget().pack()
        # ax = figure.add_subplot(111)
        # canvas = FigureCanvasTkAgg(figure, master=self.root)
        # canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        canvas = FigureCanvasTkAgg(figure=figure, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().place(x=0, y=23)
        min_x, min_y, max_x, max_y = self.min_max_calculate()
        x_pos, y_pos = self.scaling_positions(min_x, min_y, max_x, max_y)

        # plot nodes
        i = 0
        for curr in x_pos:
            plt.plot(x_pos.get(curr), y_pos.get(curr), markersize=10, marker='o', color='red')
            plt.text(x=x_pos.get(curr) - 1.5, y=y_pos.get(curr) - 3.5, s=str(i), color='black')
            i += 1

        # plot edges
        for node in self.graph.get_all_v().keys():
            # curr_edge = self.graph.get_edge(edge, s)
            # x_src = self.graph.get_node(edge.getSrc()).get_x()
            # y_src = self.graph.get_node(edge.getSrc()).get_y()
            # x_dest = self.graph.get_node(edge.getDest()).get_x()
            # y_dest = self.graph.get_node(edge.getDest()).get_y()
            # x_points, y_points = self.draw_arrow(edge.weight, x_src, y_src, x_dest, y_dest)
            all_out_edges = self.graph.all_out_edges_of_node(node)
            x_src = x_pos.get(node)
            y_src = y_pos.get(node)
            for edge in all_out_edges:
                x_dest = x_pos.get(edge)
                y_dest = y_pos.get(edge)
                plt.annotate("", xy=(x_dest, y_dest), xytext=(x_src, y_src),
                             arrowprops=dict(arrowstyle="->"))
                # TODO: plot weights

                # weight = all_out_edges.get(edge)
                # weight = '{0:.4f}'.format(weight)
                # plt.text(x=abs(x_dest - x_src), y=max(x_dest, x_src), s=str(weight).format())
                # plt.text(x=x_dest, y=y_dest, s=str(weight))

        plt.show()

        self.root.mainloop()

    # the following methods are responsible to handle clicks on buttons
    def load_graph(self):
        file_name = filedialog.askopenfilename(title="Open file", initialdir='/../../PycharmProjects',
                                               filetypes=(('json files', '*.json'), ('All files', '*.*')))
        self.load_from_json(file_name)
        self.root.withdraw()
        self.plot_graph()

    def save_graph(self):
        file_name = filedialog.asksaveasfile(title="Save file", initialdir='/../../PycharmProjects', filetypes=(('json files', '*.json'), ('All files', '*.*')))
        self.save_to_json(file_name.name)

    def short_path(self):
        src = askinteger(title="Source", prompt="Enter Source Node")
        dest = askinteger("Destination", "Enter Destination Node")
        dist = self.shortest_path(src, dest)[0]
        path = self.shortest_path(src, dest)[1]
        path_str = ""
        for node in path:
            path_str += str(node)
            path_str += "->"
        path_str = path_str[:-2]
        showinfo(title="shortest path",message="Shortest Path Dist Is: {dist}, Path is: {path} ".format(dist=dist, path=path_str))

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
                showinfo(title="Error",message="invalid id, whether id does not exist or negative ID was entered")
                node = askinteger(title="enter node", prompt="Enter Another Node ID, to finish press -1")
        tsp_result = self.TSP(node_lst=node_list)
        path = tsp_result[0]
        dist = tsp_result[1]
        path_str = ""
        for node in path:
            path_str += str(node)
            path_str += "->"
        path_str = path_str[:-2]
        showinfo(title="TSP",message="TSP Dist Is: {dist}, Path is: {path} ".format(dist=dist, path=path_str))

    def center(self):
        result = self.centerPoint()
        center_node = result[0]
        min_distance = result[1]
        showinfo(title="center", message="Center Vertex is: {vertex}, minimum distance is {dis}".format(vertex=center_node,dis=min_distance))

    def connected(self):
        result = self.is_connected()
        if result:
            showinfo(title="Is Connected", message="The Graph Is Connected")
        else:
            showinfo(title="Is Connected", message="The Graph Is Not Connected")


    def min_max_calculate(self):
        min_x = float('inf')
        min_y = float('inf')
        max_x = -float('inf')
        max_y = -float('inf')

        for node in self.graph.get_all_v().keys():
            # min_x
            if self.graph.get_node(node).getPosition().get_x() < min_x:
                min_x = self.graph.get_node(node).getPosition().get_x()
            # min_y
            if self.graph.get_node(node).getPosition().get_y() < min_y:
                min_y = self.graph.get_node(node).getPosition().get_y()
            # max_x
            if self.graph.get_node(node).getPosition().get_x() > max_x:
                max_x = self.graph.get_node(node).getPosition().get_x()
            # max_y
            if self.graph.get_node(node).getPosition().get_y() > max_y:
                max_y = self.graph.get_node(node).getPosition().get_y()

        return [min_x, min_y, max_x, max_y]

    def scaling_positions(self, min_x, min_y, max_x, max_y):
        x_pos = {}
        y_pos = {}
        all_nodes = self.graph.get_all_v()

        scale_x = 1000 / (max_x - min_x) * 0.9
        scale_y = 1000 / (max_y - min_y) * 0.9
        for node in all_nodes.keys():
            x = (self.graph.get_node(node).get_x() - min_x) * scale_x + 30
            y = (self.graph.get_node(node).get_y() - min_y) * scale_y + 90
            x_pos[node] = int(x)
            y_pos[node] = int(y)

        return x_pos, y_pos

    # def draw_arrow(self, weight, x_src, y_src, x_dest, y_dest):
    #     width = 8.0
    #     height = 4.0
    #     x_value = (x_dest - x_src)
    #     y_value = (y_dest - y_src)
    #     dist_between_nodes = math.sqrt(x_value * x_value + y_value * y_value)
    #     sin_val = y_value / dist_between_nodes
    #     cos_val = x_value / dist_between_nodes
    #
    #     y_head1 = (dist_between_nodes - width) * sin_val + height * cos_val + y_src
    #     x_head1 = (dist_between_nodes - width) * cos_val + height * sin_val + y_src
    #     y_head2 = (dist_between_nodes - width) * sin_val - 1 * height * cos_val + y_src
    #     x_head2 = (dist_between_nodes - width) * cos_val + 1 * height * sin_val + y_src
    #
    #     x_points = [int(x_dest), int(x_head1), int(x_head2)]
    #     y_points = [int(y_dest), int(y_head1), int(y_head2)]
    #
    #     return x_points, y_points


if __name__ == '__main__':
    graph = GraphAlgo()
    graph.load_from_json(r"C:\Users\itama\PycharmProjects\OOP_2021_Ex3\data\A0.json")
    graph.plot_graph()
