# **Exercise 3 - Graph Algorithm In Python**
>By Itamar Kraitman & Yuval Bubnovsky

Object-Oriented Programming course @ Ariel University, exercise 3

In this assignment, we were tasked with creating a Python app which will hold a directed weighted graph, run algorithms on said graph, present the results to the user and have save/load capabilities. The interfaces were given to us and we were not allowed to alter them in any way.

Instructions regarding running the code can be found [here](https://docs.google.com/document/d/15sTWy_pa6Vg4r7phAC322vZA169V02yezjxxf4b9sJc/edit)

## How To Run
* Download the source code to your local machine
* install tkinter:
```commandline
  pip install tk
```
* install matplotlib:
```commandline
pip install matplotlib
```
* Once you have all the dependencies set up, enter either main.py and make sure all the path's within are correct, for example:
```python
def check1():
    """
       This function tests the naming (main methods of the GraphAlgo class, as defined in GraphAlgoInterface.
    :return:
    """
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = "YOUR PATH HERE.json"
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    print(g_algo.shortest_path(0, 3))
    print(g_algo.shortest_path(3, 1))
    print(g_algo.centerPoint())
    g_algo.save_to_json(file + '_saved')
    g_algo.plot_graph()
```
* alternatively, you cun run the program like so, navigate to the folder containing main.py and run:
* Windows:
```commandline
python -m main.py YOUR_FILE_PATH.json
```
* Linux:
```commandline
python3 main.py YOUR_FILE_PATH.json
```
## Overview
Our workflow on this exercise has been Test-Driven Development from day one, each class and function which had it's tests written before we implemented it - we believe it has benefited to our code reliability and development process.
<br> Work on this exercise began by examining the JSON files given to us by the course instructors and figuring out the data structures which we will be using.
<br> Our data structure of choice was using python's dictionaries since we believe it is the best way to represent the Node and Edge mapping we have established,
we use one dictionary to hold all Nodes in a given graph, and 2 dictionaries for the edges - the first one holds all the regular edges and the second one holds all the edges transposed.
<br> We were also asked to compare this assignment with our previus one - which basically the same implementation in Java, all of these comparisons can also be found
[here](https://github.com/YuvalBubnovsky/OOP_2021_Ex3/wiki/Comparison-to-Java)

## Project Structure

The workspace contains three folders by default, where:

- `graph`: all source code is here
- `data`: contains all JSON files representing directed weighted graphs
- `tests`: contains all test files

## Algorithms Implemented:
* Depth-First Search
* Dijkstra's Shortest Path
* Graph Connectivity
* Finding The Center Of The Graph
* Augmented Version Of TSP (Traveling Salesmen Problem)
<br> Analysis of these algorithm's complexity can be found [here](https://github.com/YuvalBubnovsky/OOP_2021_Ex3/wiki/Algorithm-Analysis)


