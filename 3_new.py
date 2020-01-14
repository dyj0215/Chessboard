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


# the shortest path： [1, 2, 3, 11, 19, 18, 17, 25, 33, 34, 35, 36, 37, 29, 30, 31, 39, 47, 46, 54, 62, 63, 64]

# steps: 22
