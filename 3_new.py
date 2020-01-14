__author__ = 'Yijie Dong'

import numpy as np
from collections import defaultdict

n = 8 #The dimension of the chessboard
# chessboard = np.random.randint(0,2,(n,n))#Get a random array with only 0 and 1
# chessboard[0][0] = chessboard[n-1][n-1] = 0#Both upper left corner and bottom right corner are available. equal to 0


chessboard = [
    [0,0,0,0,0,1,1,0],
    [1,1,0,0,1,1,1,1],
    [0,0,0,1,1,1,1,0],
    [0,1,1,0,0,0,0,1],
    [0,0,0,0,0,1,0,1],
    [1,1,0,1,1,0,0,1],
    [1,1,0,0,1,0,1,0],
    [0,1,0,0,1,0,0,0]
    ]
print (chessboard)

graph = defaultdict(list)


for i in range(0,n):
    for j in range(0,n-1):
        if chessboard[i][j]==chessboard[i][j+1]==0:
            graph[int(n*i+j+1)].append(int(n*i+j+2))
            graph[int(n*i+j+2)].append(int(n*i+j+1))

for j in range(0,n):
    for i in range(0,n-1):
        if chessboard[i][j]==chessboard[i+1][j]==0:
            graph[int(n*i+j+1)].append(int(n*i+j+1+n))
            graph[int(n*i+j+1+n)].append(int(n*i+j+1))



# print(graph)

# Find only one path
def findPath(graph,start,end,path=[]):   
    path = path + [start]
    if start == end:
        return path 
    for node in graph[start]:
        if node not in path:
            newpath = findPath(graph,node,end,path)
            if newpath:
                return newpath
    return None
 
# Find all the paths from 'Start point' to the 'End Point'
def findAllPath(graph,start,end,path=[]):
    path = path +[start]
    if start == end:
        return [path]
 
    paths = [] #Save all the paths    
    for node in graph[start]:
        if node not in path:
            newpaths = findAllPath(graph,node,end,path) 
            for newpath in newpaths:
                paths.append(newpath)
    return paths
 
# Find the shortest path
def findShortestPath(graph,start,end,path=[]):
    path = path +[start]
    if start == end:
        return path
    
    shortestPath = []
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph,node,end,path)
            if newpath:
                if not shortestPath or len(newpath)<len(shortestPath):
                    shortestPath = newpath
    return shortestPath
 

 
onepath = findPath(graph,1,n*n)
print('\none of all paths:',onepath)
 
allpath = findAllPath(graph,1,n*n)
print('\nall the paths：',allpath)
 
shortpath = findShortestPath(graph,1,n*n)#I want to find the shortest path from upper left point to bottom right point. So i set 1 and n*n
print('\nthe shortest path：',shortpath)
print('\nsteps:', len(shortpath)-1)

# One example for finding a path
# [[0 0 0 0 0 1 1 0]
#  [1 1 0 0 1 1 1 1]
#  [0 0 0 1 1 1 1 0]
#  [0 1 1 0 0 0 0 1]
#  [0 0 0 0 0 1 0 1]
#  [1 1 0 1 1 0 0 1]
#  [1 1 0 0 1 0 1 0]
#  [0 1 0 0 1 0 0 0]]

# defaultdict(<class 'list'>, {1: [2], 2: [1, 3, 10], 3: [2, 4], 4: [3, 5, 12], 5: [4], 20: [21, 12, 28], 21: [20, 29], 27: [28], 28: [27, 29, 20, 36], 29: [28, 21, 37], 36: [37, 28], 37: [36, 38, 29], 38: [37, 39, 46], 39: [38, 31, 47], 46: [47, 38, 54], 47: [46, 39, 55], 51: [52, 43, 59], 52: [51, 60], 54: [55, 46, 62], 55: [54, 56, 47, 63], 56: [55, 64], 59: [60, 51], 60: [59, 52], 62: [63, 54], 63: [62, 64, 55], 64: [63, 56], 10: [2], 43: [51], 12: [4, 20], 31: [39]})

# one of all paths: [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 39, 47, 46, 54, 55, 56, 64]

# all the paths： [[1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 39, 47, 46, 54, 55, 56, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 39, 47, 46, 54, 55, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 39, 47, 46, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 39, 47, 46, 54, 62, 63, 55, 56, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 39, 47, 55, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 39, 47, 55, 56, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 39, 47, 55, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 46, 47, 55, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 46, 47, 55, 56, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 46, 47, 55, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 46, 54, 55, 56, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 46, 54, 55, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 46, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 28, 36, 37, 38, 46, 54, 62, 63, 55, 56, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 39, 47, 46, 54, 55, 56, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 39, 47, 46, 54, 55, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 39, 47, 46, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 39, 47, 46, 54, 62, 63, 55, 56, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 39, 47, 55, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 39, 47, 55, 56, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 39, 47, 55, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 46, 47, 55, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 46, 47, 55, 56, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 46, 47, 55, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 46, 54, 55, 56, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 46, 54, 55, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 46, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 46, 54, 62, 63, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 39, 47, 46, 54, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 39, 47, 46, 54, 55, 63, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 39, 47, 46, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 39, 47, 46, 54, 62, 63, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 39, 47, 55, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 39, 47, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 39, 47, 55, 63, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 46, 47, 55, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 46, 47, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 46, 47, 55, 63, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 46, 54, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 46, 54, 55, 63, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 46, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 28, 29, 37, 38, 46, 54, 62, 63, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 39, 47, 46, 54, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 39, 47, 46, 54, 55, 63, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 39, 47, 46, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 39, 47, 46, 54, 62, 63, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 39, 47, 55, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 39, 47, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 39, 47, 55, 63, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 46, 47, 55, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 46, 47, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 46, 47, 55, 63, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 46, 54, 55, 56, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 46, 54, 55, 63, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 46, 54, 62, 63, 64], [1, 2, 3, 4, 12, 20, 28, 36, 37, 38, 46, 54, 62, 63, 55, 56, 64]]

# the shortest path： [1, 2, 3, 4, 12, 20, 21, 29, 37, 38, 39, 47, 55, 56, 64]

# steps: 14





# One example for no path 
# [[0 0 1 0 0 0 0 0]
#  [1 1 0 1 0 1 1 0]
#  [1 1 0 1 1 1 0 0]
#  [1 1 0 0 1 1 0 1]
#  [1 0 1 0 1 0 1 1]
#  [0 1 1 1 0 1 0 0]
#  [1 1 0 1 1 1 0 1]
#  [1 1 1 1 0 1 1 0]]

# defaultdict(<class 'list'>, {1: [2], 2: [1], 4: [5], 5: [4, 6, 13], 6: [5, 7], 7: [6, 8], 8: [7, 16], 23: [24, 31], 24: [23, 16], 27: [28, 19], 28: [27, 36], 47: [48, 55], 48: [47], 11: [19], 19: [11, 27], 36: [28], 13: [5], 31: [23], 55: [47], 16: [8, 24]})

# one of all paths: None

# all the paths： []

# the shortest path： []

# steps: -1







# chessboard = [
#     [0,0,0,0,0,1,1,0],
#     [1,1,0,0,1,1,1,1],
#     [0,0,0,1,1,1,1,0],
#     [0,1,1,0,0,0,0,1],
#     [0,0,0,0,0,1,0,1],
#     [1,1,0,1,1,0,0,1],
#     [1,1,0,0,1,0,1,0],
#     [0,1,0,0,1,0,0,0]
#     ]

# one of all paths: [1, 2, 3, 4, 12, 11, 19, 18, 17, 25, 33, 34, 35, 36, 37, 29, 30, 31, 39, 47, 46, 54, 62, 63, 64]

# all the paths： [
#     [1, 2, 3, 4, 12, 11, 19, 18, 17, 25, 33, 34, 35, 36, 37, 29, 30, 31, 39, 47, 46, 54, 62, 63, 64], 
#     [1, 2, 3, 4, 12, 11, 19, 18, 17, 25, 33, 34, 35, 36, 28, 29, 30, 31, 39, 47, 46, 54, 62, 63, 64], 
#     [1, 2, 3, 11, 19, 18, 17, 25, 33, 34, 35, 36, 37, 29, 30, 31, 39, 47, 46, 54, 62, 63, 64], 
#     [1, 2, 3, 11, 19, 18, 17, 25, 33, 34, 35, 36, 28, 29, 30, 31, 39, 47, 46, 54, 62, 63, 64]
#     ]

# the shortest path： [1, 2, 3, 11, 19, 18, 17, 25, 33, 34, 35, 36, 37, 29, 30, 31, 39, 47, 46, 54, 62, 63, 64]

# steps: 22