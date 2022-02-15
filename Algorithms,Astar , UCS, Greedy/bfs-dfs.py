# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:45:46 2021

@author: SP19-BCS-089
         MOHAMMAD ABUZAR
         SECTION B
"""

graph2 = {
            "Arua": ["Gulu", "Nimule","Masindi"],
            "Gulu": ["Arua", "Ogur"],
            "Nimule": ["Arua", "Acholibur"],
            "Acholibur": ["kaabong", "Nimule"],
            "kaabong": ["Acholibur"],
            "Ogur": ["Gulu","Soroti","Naga"],
             "Soroti": ["Ogur","Kotido","Mbale"],
            "Kotido": ["Soroti"],
            "Mbale":["Soroti","Torror"],
            "Torror":["Mbale","Jinja"],
            "Jinja":["Torror","Kampala"],
            "Kampala":["Naga","Jinja","Mubende"],
            "Naga":["Ogur","Masindi","Kampala"],
            "Mubende":["Kampala","Kasese"],
            "Kasese":["Mubende","Mbara"],
            "Mbara":["Kasese","Biwindi NP"],
            "Biwindi NP" :["Mbara"],
            "Masindi":["Arua","Naga"]
            
            
}
# visits all the nodes of a graph using DFS
def dfs(graph, start):
    # keep track of all visited nodes
    explored = []
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
        # print("queue : ", queue)
        # pop Top node (first node) from stack
      
        node = queue.pop(0)
        # print('node being explored: ',node)
        # print("explored : ", explored)
        
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
            # add reversed neighbours of node to stack so they could pop in actual order.
            neighbours.reverse()
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


print("--------------------------------------")

print("Following is the Depth-First Search") 

print("--------------------------------------")
print(dfs(graph, "Arua"))
print("--------------------------------------")
print("Following is the Breathe-First Search") 
print("--------------------------------------")
print(bfs(graph, "Arua"))