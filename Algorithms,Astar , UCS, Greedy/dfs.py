# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:45:46 2021

@author: S.R
"""

graph = {
            0: [1, 2, 3, 4],
            1: [0, 5],
            2: [0, 5],
            3: [0, 6],
            4: [0, 6],
            5: [1, 2, 7],
            6: [3, 4, 7],
            7: [5, 6],
}
# visits all the nodes of a graph using DFS
def dfs(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        print("queue : ", queue)
        # pop Top node (first node) from stack
        node = queue.pop()
       # node = queue.pop(0)
        print('node being explored: ',node)
        print("explored : ", explored)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
            # add reversed neighbours of node to stack so they could pop in actual order.
            neighbours.reverse()
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


def bfs(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]
    # keep looping until there are nodes still to be checked
    while queue:
        print("queue : ", queue)
        # pop Top node (first node) from stack
      
        node = queue.pop(0)
        print('node being explored: ',node)
        print("explored : ", explored)
        
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    return explored
# Driver Code
print("--------------------------------------")
print("Following is the Depth-First Search") 
print("--------------------------------------")
print(dfs(graph, 4))
print("--------------------------------------")
print("Following is the Breadth-First Search")
print("--------------------------------------")
bfs(graph, 4)  




