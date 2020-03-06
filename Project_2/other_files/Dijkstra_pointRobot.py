import cv2
import numpy as np

infinity = 10000000000000000000
height = 100
width = 200

blank_image = np.zeros((height, width, 3), np.uint8)

# x>=90 and x<= 110 and y>=40 and y<=60
# x>=0 and x<=2 and y>=1 and y<=2
# (x-160)^2+(y-50)^2 < 15^2

blank_image[40:40 + 20, 90:90 + 20] = (255, 255, 255)
# blank_image[2:3, 0:3] = (255,255,255)

center_coordinates = (160, 50)
radius = 15
color = (255, 255, 255)
thickness = -1
blank_image = cv2.circle(blank_image, center_coordinates, radius, color, thickness)

cv2.imshow("T", blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

maze = {}
inner_dict = {}
maze = {}
inner_dict = {}


def top_left(i, j):
    #     print("top_left called")
    cost = 1.414
    new_i = i - 1
    new_j = j - 1
    if ((new_i - 160) ** 2 + (new_j - 50) ** 2 < 15 ** 2) or (new_i >= 90 and new_i <= 110 and new_j >= 40 and new_j <= 60):
        return None, None, None
    elif ((new_i < 0) or (new_j < 0) or (new_i > width - 1) or (new_j > height - 1)):
        return None, None, None
    else:
        return cost, new_i, new_j


def top(i, j):
    #     print("top called")
    cost = 1
    new_i = i
    new_j = j - 1
    if (new_i >= 90 and new_i <= 110 and new_j >= 40 and new_j <= 60) or ((new_i - 160) ** 2 + (new_j - 50) ** 2 < 15 ** 2):
        return None, None, None
    elif (new_i < 0 or new_j < 0 or new_i > width - 1 or new_j > height - 1):
        return None, None, None
    else:
        return cost, new_i, new_j


def top_right(i, j):
    #     print("top_right called")
    cost = 1.414
    new_i = i + 1
    new_j = j - 1
    if ((new_i - 160) ** 2 + (new_j - 50) ** 2 < 15 ** 2) or (new_i >= 90 and new_i <= 110 and new_j >= 40 and new_j <= 60):
        return None, None, None
    elif new_i < 0 or new_j < 0 or new_i > width - 1 or new_j > height - 1:
        return None, None, None
    else:
        return cost, new_i, new_j


def right(i, j):
    #     print("right called")
    cost = 1
    new_i = i + 1
    new_j = j
    if ((new_i - 160) ** 2 + (new_j - 50) ** 2 < 15 ** 2) or  (new_i >= 90 and new_i <= 110 and new_j >= 40 and new_j <= 60):
        return None, None, None
    elif new_i < 0 or new_j < 0 or new_i > width - 1 or new_j > height - 1:
        return None, None, None
    else:
        return cost, new_i, new_j


def bottom_right(i, j):
    #     print("bottom_right called")
    cost = 1.414
    new_i = i + 1
    new_j = j + 1
    if ((new_i - 160) ** 2 + (new_j - 50) ** 2 < 15 ** 2) or (new_i >= 90 and new_i <= 110 and new_j >= 40 and new_j <= 60):
        return None, None, None

    elif ((new_i < 0 or new_j < 0 or new_i > width - 1 or new_j > height - 1) or (
            new_i >= 0 and new_i <= 2 and new_j >= 1 and new_j <= 2)):
        return None, None, None
    else:
        return cost, new_i, new_j


def bottom(i, j):
    #     print("bottom called")
    cost = 1
    new_i = i
    new_j = j + 1
    if ((new_i - 160) ** 2 + (new_j - 50) ** 2 < 15 ** 2) or (90 <= new_i <= 110 and 40 <= new_j <= 60):
        return None, None, None
    elif (new_i < 0 or new_j < 0 or new_i > width - 1 or new_j > height - 1):
        return None, None, None
    else:
        return cost, new_i, new_j


def bottom_left(i, j):
    #     print("bottom_left called")

    cost = 1.414
    new_i = i - 1
    new_j = j + 1
    if (90 <= new_i <= 110 and 40 <= new_j <= 60) or ((new_i - 160) ** 2 + (new_j - 50) ** 2 < 15 ** 2):
        return None, None, None
    elif (new_i < 0 or new_j < 0 or new_i > width - 1 or new_j > height - 1):
        return None, None, None
    else:
        return cost, new_i, new_j


def left(i, j):
    #     print("left called")
    cost = 1
    new_i = i - 1
    new_j = j
    if ((new_i - 160) ** 2 + (new_j - 50) ** 2 < 15 ** 2) or (new_i >= 0 and new_i <= 2 and new_j >= 1 and new_j <= 2):
        return None, None, None
    elif new_i < 0 or new_j < 0 or new_i > width - 1 or new_j > height - 1:
        return None, None, None
    else:
        return cost, new_i, new_j


def function(i, j):
    weight1, new_i1, new_j1 = top_left(i, j)
    weight2, new_i2, new_j2 = top(i, j)
    weight3, new_i3, new_j3 = top_right(i, j)
    weight4, new_i4, new_j4 = right(i, j)
    weight5, new_i5, new_j5 = bottom_right(i, j)
    weight6, new_i6, new_j6 = bottom(i, j)
    weight7, new_i7, new_j7 = bottom_left(i, j)
    weight8, new_i8, new_j8 = left(i, j)

    if (weight1 != None):
        inner_dict[(new_i1, new_j1)] = weight1
        maze[(i, j)] = inner_dict
    if (weight2 != None):
        inner_dict[(new_i2, new_j2)] = weight2
        maze[(i, j)] = inner_dict
    if (weight3 != None):
        inner_dict[(new_i3, new_j3)] = weight3
        maze[(i, j)] = inner_dict
    if (weight4 != None):
        inner_dict[(new_i4, new_j4)] = weight4
        maze[(i, j)] = inner_dict
    if (weight5 != None):
        inner_dict[(new_i5, new_j5)] = weight5
        maze[(i, j)] = inner_dict
    if (weight6 != None):
        inner_dict[(new_i6, new_j6)] = weight6
        maze[(i, j)] = inner_dict
    if (weight7 != None):
        inner_dict[(new_i7, new_j7)] = weight7
        maze[(i, j)] = inner_dict
    if (weight8 != None):
        inner_dict[(new_i8, new_j8)] = weight8
        maze[(i, j)] = inner_dict


for i in range(width):
    for j in range(height):
        inner_dict = {}
        function(i, j)
#         cv2.imshow("Blank",blank_image)

def dijkstra(maze, start, goal):
    dist_from_start = {}
    parent_node = {}
    Allnodes = maze
    infinity = 1000000000
    shortest_path = []
    for node in Allnodes:
        dist_from_start[node] = infinity
    dist_from_start[start] = 0

    while Allnodes:
        minNode = None
        for node in Allnodes:
            if minNode is None:
                minNode = node
            elif dist_from_start[node] < dist_from_start[minNode]:
                minNode = node
                x = minNode[0]
                y = minNode[1]
                blank_image[y, x] = (0, 0, 255)
                cv2.imshow("traverse", blank_image)

        for childNode, cost in maze[minNode].items():
            if cost + dist_from_start[minNode] < dist_from_start[childNode]:
                dist_from_start[childNode] = cost + dist_from_start[minNode]
                parent_node[childNode] = minNode
        Allnodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            shortest_path.insert(0, currentNode)
            currentNode = parent_node[currentNode]
        except KeyError:
            print('shortest_path not reachable')
            break
    shortest_path.insert(0, start)
    if dist_from_start[goal] != infinity:
        print('Shortest distance is ' + str(dist_from_start[goal]))
        print('And the shortest_path is ' + str(shortest_path))
        return shortest_path


short_path = dijkstra(maze, (5, 5), (111, 48))

for path in short_path:
    x = path[0]
    y = path[1]
    blank_image[y,x] = (255,255,0)
    cv2.namedWindow('T',cv2.WINDOW_NORMAL)

cv2.resizeWindow('T', 1000,2000)
cv2.imshow("T",blank_image)

cv2.waitKey(0)
cv2.destroyAllWindows()