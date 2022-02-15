# -*- coding: utf-8 -*-
"""

@Mohammad Abuzar
SP19-BCS-089
SECTION B
"""

import time
from queue import PriorityQueue
import matplotlib.pyplot as plt


class Graph:
    
    def __init__(self):
        
        self.graph = {
"Izmir": [(146, ("Izmir", "Omaha")), (140, ("Izmir", "Syria")), (494, ("Izmir", "Chicago"))],
"Omaha": [(146, ("Omaha", "Izmir")), (151, ("Omaha", "Syria"))],
"Syria": [(151, ("Syria", "Omaha")), (140, ("Syria", "Izmir")),(80, ("Syria", "Rabat")),(99, ("Syria", "Florida"))],
"Chicago": [(494, ("Chicago", "Izmir")), (146, ("Chicago", "Rabat"))],
"Rabat": [(80, ("Rabat", "Syria")), (146, ("Rabat", "Chicago")), (97, ("Rabat", "Patna"))],
"Florida": [(99, ("Florida", "Syria")), (211, ("Florida", "Butan"))],
"Butan": [(211, ("Butan", "Florida")), (101, ("Butan", "Patna"))],
"Patna": [(101, ("Patna", "Butan")), (97, ("Patna", "Rabat")), (138, ("Patna", "Chicago"))] }
        
        self.edges = {}
        self.weights = {}
        self.heuristics = {
            "Izmir" : 10,
            "Omaha" : 9,
            "Syria" : 7,
            "Chicago" : 8,
            "Rabat" : 6, 
            "Florida" : 5, 
            "Patna": 3,
            "Butan": 0
        }
        self.populate_edges()
        self.populate_weights()
        
        # print("edges : ", self.edges)
        # print("------------------------------------")
        # print("weights  : ", self.weights)

    def populate_edges(self):
        for key in self.graph:
            neighbours = []
            for each_tuple in self.graph[key]:
#                print(each_tuple[1][1])
                neighbours.append(each_tuple[1][1])
#            print(neighbours)
            self.edges[key] = neighbours
           

    def populate_weights(self):
        for key in self.graph:
            neighbours = self.graph[key]

            for each_tuple in neighbours:
                self.weights[each_tuple[1]] = each_tuple[0]
                
    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node,  to_node)]
    def get_heuristics(self, node):
        return self.heuristics[node]
    
def Astar(graph, start, goal):
    visited = []
    count =0
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.append(node)
            count = count+1
            if node == goal:
                break
            for i in graph.neighbors(node):
                if i not in visited:
                  
                   total_cost=cost+graph.get_cost(node,i)+graph.get_heuristics(i)
                   
                   queue.put((total_cost, i))
                   
    print("Number of Nodes Visited:",count)   
    return visited
def ucs(graph, start, goal):
    visited = []
    count = 0
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.append(node)
            count = count+1
            if node == goal:
                break
            for i in graph.neighbors(node):
                if i not in visited:
                  
                   total_cost=cost+graph.get_cost(node,i)
                   
                   queue.put((total_cost, i))
    print("Number of Nodes Visited:",count)                
    return visited

def greedy(graph, start, goal):
    visited = []
    count = 0
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        heuristics, node = queue.get()
        if node not in visited:
            visited.append(node)
            count = count+1
            if node == goal:
                break
            for i in graph.neighbors(node):
                if i not in visited:   
                   total_cost=graph.get_heuristics(i) 
                   
                   queue.put((total_cost, i))
    print("Number of Nodes Visited:",count)               
    return visited

def dfs(graph, start):
    # keep track of all visited nodes
    explored = []
    count = 0
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        # print("queue : ", queue)
        # pop Top node (first node) from stack
        node = queue.pop()
       # node = queue.pop(0)
        # print('node being explored: ',node)
        # print("explored : ", explored)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            count = count+1
            neighbours = graph[node]
            # add reversed neighbours of node to stack so they could pop in actual order.
            neighbours.reverse()
            for neighbour in neighbours:
                queue.append(neighbour)
    print("Number of Nodes Visited:",count)
    return explored


def bfs(graph, start):
    # keep track of all visited nodes
    explored = []
    count = 0
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        # print("queue : ", queue)
        # pop Top node (first node) from stack
      
        node = queue.pop(0)
        # print('node being explored: ',node)
        # print("explored : ", explored)
        
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            count = count+1
            neighbours = graph[node]
            # add reversed neighbours of node to stack so they could pop in actual order.
            neighbours.reverse()
            for neighbour in neighbours:
                queue.append(neighbour)
    print("Number of Nodes Visited:",count)    
    return explored

 #Bar chart for  Time Compexity 
Algorithms = ['Astar *','Greedy','UCS','DFS','BFS']
Time_Complexity =[0.0003392122646484,0.00079945068359375,0.0008992122650146484,0.00099945068359375,0.002003192901611328]

plt.bar(Algorithms, Time_Complexity)
plt.title('Time Complexity')
plt.xlabel('Algorithms')
plt.ylabel('Time Complexity')
plt.show()

#Bar chart for Visited Nodes
Algorithms = ['Astar *','Greedy','UCS','DFS','BFS']
No_of_Visited_Nodes =[5,3,5,8,8]

plt.bar(Algorithms, No_of_Visited_Nodes)
plt.title('Explored Nodes')
plt.xlabel('Algorithms')
plt.ylabel('Explored Nodes')
plt.show()

print("Traversal  Astar: ", Astar(Graph(), "Izmir", "Florida"))
print("Traversal  Greedy: ",greedy(Graph(), "Izmir", "Florida"))
print("Traversal  UCS: ",ucs(Graph(), "Izmir", "Florida"))
print("Traversal BFS :" ,bfs(Graph().edges ,"Izmir"))
print("Traversal DFS:" ,dfs(Graph().edges ,"Izmir"))
    
# end = time.time()
# print(f"Runtime of the program is {end - start}")

