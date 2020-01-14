__author__ = 'Yijie Dong'
import matplotlib
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np

color1 = (0, 0, 1)
color2 = (1, 1, 1)
color3 = (0, 1, 0)
n = 8
# mat = np.zeros((8, 8))
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

chessboard_with_path = np.reshape(chessboard, (64,1))


my_cmap = matplotlib.colors.LinearSegmentedColormap.from_list('chessboard', [color1, color2], 2)
cs = plt.imshow(chessboard, cmap=my_cmap)

plt.xticks(np.linspace(0, 8, 8, endpoint=False), ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'), fontsize=20)
plt.yticks(np.linspace(0, 8, 8, endpoint=False), ('1', '2', '3', '4', '5', '6', '7', '8'), fontsize=20)
plt.tick_params(bottom=False, left=False, labeltop=True, labelright=True)
plt.savefig("chessboard.png")
plt.show()


graph = defaultdict(list)

for i in range(0, n):
    for j in range(0, n - 1):
        if chessboard[i][j] == chessboard[i][j + 1] == 0:
            graph[int(n * i + j + 1)].append(int(n * i + j + 2))
            graph[int(n * i + j + 2)].append(int(n * i + j + 1))

for j in range(0, n):
    for i in range(0, n - 1):
        if chessboard[i][j] == chessboard[i + 1][j] == 0:
            graph[int(n * i + j + 1)].append(int(n * i + j + 1 + n))
            graph[int(n * i + j + 1 + n)].append(int(n * i + j + 1))


# print(graph)

# Find the shortest path
def findShortestPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path

    shortestPath = []
    for node in graph[start]:
        if node not in path:
            newpath = findShortestPath(graph, node, end, path)
            if newpath:
                if not shortestPath or len(newpath) < len(shortestPath):
                    shortestPath = newpath
    return shortestPath


shortpath = findShortestPath(graph, 1, n * n)  # I want to find the shortest path from upper left point to bottom right point. So i set 1 and n*n

for k in range(len(shortpath)):
    p = shortpath[k]
    chessboard_with_path[p-1] = 2

chessboard_with_path = np.reshape(chessboard_with_path, (8,8))

my_cmap = matplotlib.colors.LinearSegmentedColormap.from_list('chessboard_with_path', [color1, color2, color3], 3)
cs = plt.imshow(chessboard_with_path, cmap=my_cmap)

plt.xticks(np.linspace(0, 8, 8, endpoint=False), ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'), fontsize=20)
plt.yticks(np.linspace(0, 8, 8, endpoint=False), ('1', '2', '3', '4', '5', '6', '7', '8'), fontsize=20)
plt.tick_params(bottom=False, left=False, labeltop=True, labelright=True)
plt.savefig("chessboard_with_path.png")
plt.show()


print('\nthe shortest path：', shortpath)

print('\nsteps:', len(shortpath) - 1)
