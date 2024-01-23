#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


class Node:
    def __init__(self,value = 0,row = None,column = None):
        self.value = value
        self.row = row
        self.column = column
        
    def __repr__(self):
        return str(self.value)
    
    def __str__(self):
        return str(self.value)
        
import numpy as np
import random
def matrix_creating():
    
    x = np.array([[Node() for j in range(10)] for i in range(10)])
    for column in range(len(x)):
        for row in range(len(x[0])):
            x[row][column] = Node(random.randint(0,15),row,column)
    for i in range(0,30):
        x[random.randint(0,9)][random.randint(0,9)].value = 99

    return x
maze = matrix_creating()

print(maze)


def g_cost(start,end):
    distance = 0
    intersect_point = maze[start.row][end.column]
    # print(intersect_point.value,intersect_point.row,intersect_point.column)
    for i in range(start.column, intersect_point.column+1):
        distance += maze[start.row][i].value
    for a in range(intersect_point.row, end.row+1):
        distance += maze[a][intersect_point.column].value
    return distance

def connected_points(node):
    row = 10
    column = 10
    l1 = []
    if (node.row - 1) >= 0:
        l1.append(maze[node.row-1][node.column])
    if (node.column - 1) >= 0:
        l1.append(maze[node.row][node.column - 1])
    if (node.row + 1) < row:
        l1.append(maze[node.row+1][node.column])
    if (node.column + 1) < column:
        l1.append(maze[node.row][node.column + 1])
    return l1
        
    

def A_star(start,end):
    open_list = [start]
    closed_list = []
    while len(open_list) != 0:
        current = open_list[0]
        for i in open_list:
            if i.value < current.value:
                current = i
        open_list.remove(current)
#         closed_list.append([current.row,current.column])
        closed_list.append(current)
        if current == end:
            return closed_list
        for i in connected_points(current):
            if i in closed_list:
                continue
            if i not in open_list:
                open_list.append(i)
            else:
                if g_cost(start,end) < g_cost(start,i):
                    i = current
    return closed_list
    
    
    
result = A_star(maze[0][0],maze[-1][-1])
path = []
for i in result:
#     print(f"[{i.row},{i.column}]")
    path.append([i.row,i.column])
print(path)


# In[ ]:




