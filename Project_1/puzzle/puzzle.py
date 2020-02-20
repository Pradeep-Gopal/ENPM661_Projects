# Importing the libraries
import numpy as np

# Creating an empty matrix to get the input matrix from
Node_State = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print("\n")
print("Enter the elements of the puzzle in row wise fashion")
for i in range(0, len(Node_State[1])):
    for j in range(0, len(Node_State[1])):
        Node_State[i][j] = input()

print("\n")
print("The jumbled puzzle is : \n")
print(Node_State)
print("\n")
print("**************Wait till the puzzle is solved***************** \n")

# Choose one
# Node_State = np.array([[1, 0, 3], [4, 2, 5], [7, 8, 6]])  # simplest
# Node_State = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])  # takes_lot_of_time
# Node_State = np.array([[2, 4, 3], [7, 8, 0], [6, 1, 5]])  # working_maybe_a_min
# Node_State = np.array([[1, 0, 2], [4, 6, 8], [7, 3, 5]])  # working_instant
# Node_State = np.array([[4, 8, 1], [5, 2, 0], [7, 6, 3]]) # working_instant
# Node_State = np.array([[7, 2, 3], [1, 5, 6], [4, 8, 0]])  # working_maybe_a_min

# Variables Initialization
Goal_Node = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
ParentNodes = {1: 0}
AllNodes = {1: Node_State}
path = list()
notepad_path = list()

NewNode1 = Node_State.copy()
NewNode2 = Node_State.copy()
NewNode3 = Node_State.copy()
NewNode4 = Node_State.copy()

a = 1
b = 1
next_node = 1
flag = 1
clean = 1
note_path = 0


# Functions

# Function to get the Blank tile location
def BlankTileLocation(state):
    for i in range(0, len(Node_State[1])):
        for j in range(0, len(Node_State[1])):
            if state[i, j] == 0:
                return [i, j]


# Moves the 0 to the left position
def ActionMoveLeft(state, i, j):
    New_state = state.copy()
    if j == 0:
        # print("cannot perform left movement")
        return [0, state]
    else:
        # print("left movement performed")
        New_state[i, j - 1], New_state[i, j] = New_state[i, j], New_state[i, j - 1]
        return [1, New_state]


# Moves the 0 to the right position
def ActionMoveRight(state, i, j):
    New_state = state.copy()
    if j == 2:
        # print("cannot perform Right movement")
        return [0, state]
    else:
        # print("right movement performed")
        New_state[i, j + 1], New_state[i, j] = New_state[i, j], New_state[i, j + 1]
        return [1, New_state]


# Moves the 0 to the up position
def ActionMoveUp(state, i, j):
    New_state = state.copy()
    if i == 0:
        # print("cannot perform Up movement")
        return [0, state]
    else:
        # print("up movement performed")
        New_state[i - 1, j], New_state[i, j] = New_state[i, j], New_state[i - 1, j]
        return [1, New_state]


# Moves the 0 to the down position
def ActionMoveDown(state, i, j):
    New_state = state.copy()
    if i == 2:
        # print("cannot perform Down movement")
        return [0, state]

    else:
        # print("Down movement performed")
        New_state[i + 1, j], New_state[i, j] = New_state[i, j], New_state[i + 1, j]
        return [1, New_state]


# Adds the New node to the AllNodes dictionary
def AddNode(New_N):
    global a
    global b
    global flag
    flag = 1
    for values in AllNodes.values():
        if (values == New_N).all():
            flag = 0
            # print("present_do not add")
    if flag == 1:
        # print("Not present_do add")
        a = a + 1
        AllNodes[a] = New_N
        ParentNodes[a] = b


# Function which runs all the movement of '0' functions
def Check_and_Add(state1):
    global b
    global NewNode1
    global NewNode2
    global NewNode3
    global NewNode4

    [i, j] = BlankTileLocation(state1)

    [Status, NewNode] = ActionMoveLeft(state1, i, j)
    # print(NewNode)
    AddNode(NewNode)
    # print("")
    NewNode1 = NewNode.copy()

    [Status, NewNode] = ActionMoveUp(state1, i, j)
    # print(NewNode)
    AddNode(NewNode)
    # print("")
    NewNode2 = NewNode.copy()

    [Status, NewNode] = ActionMoveRight(state1, i, j)
    # print(NewNode)
    AddNode(NewNode)
    # print("")
    NewNode3 = NewNode.copy()

    [Status, NewNode] = ActionMoveDown(state1, i, j)
    # print(NewNode)
    AddNode(NewNode)
    # print("")
    # print("Next Iteration")
    # print("")
    NewNode4 = NewNode.copy()
    b = b + 1


# Function to return the key value for a certain value in AllNodes Dictionary
def get_key_AllNodes(val):
    for key, value in AllNodes.items():
        if (val == value).all():
            return key
    return "key doesn't exist"


# Function to return the key value for a certain value in ParentNodes Dictionary
def get_key_ParentNodes(val):
    for key, value in ParentNodes.items():
        if val == value:
            return key
    return "key doesn't exist"


# Deletes excess Nodes in the Allnodes Dictionary after the Goal Node
def clean_AllNodes(AllNodes):
    key = get_key_AllNodes(Goal_Node)
    length = len(AllNodes)
    while key != length:
        key = key + 1
        AllNodes.pop(key, None)


# Generates the path using reverse tracking
def generate_path(p_nodes):
    Start_key = get_key_AllNodes(Node_State)
    print("Start_key =")
    print(Start_key)
    print("")

    Goal_key = get_key_AllNodes(Goal_Node)
    print("Goal_key = ")
    print(Goal_key)
    print("")

    Goal = 0

    path.insert(Goal, Goal_key)
    print("goal_path = ")

    while path[Goal] != Start_key:
        Goal = Goal + 1
        path.insert(Goal, p_nodes[Goal_key])
        Goal_key = p_nodes[Goal_key]
    path.sort()
    print(path)
    return path


# Function to print the path from the Dictiionary
def print_optimalpath(path):
    global note_path
    global notepad_path
    print("***********************  Optimal path from Start to Goal  ************************")
    print("")

    for m in path:
        notepad_path.insert(note_path, AllNodes[m])
        note_path = note_path + 1
        print(AllNodes[m])
        print("")


# Converts List to string
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for i in range(0, len(s[1])):
        for j in range(0, len(s[1])):
            str1 = str1 + str(s[j, i])

    str1 = " ".join(str1)
    # return string
    return str1


# Creates the nodePath.txt file
def nodePath_filegen(notepad_path):
    # Creates the nodePath.txt File

    # Creates a new file
    with open('nodePath.txt', 'w') as fp:
        pass
        for m in notepad_path:
            fp.write(listToString(m))
            fp.write("\n")


# Creates the NodesInfo.txt File
def NodesInfo_filegen(ParentNodes):
    # Creates the NodesInfo.txt File

    # Creates a new file
    with open('NodesInfo.txt', 'w') as fp:
        pass
        for key, value in sorted(ParentNodes.items()):
            fp.write(str(key))
            fp.write(" ")
            fp.write(str(value))
            fp.write(" ")
            fp.write("0")
            fp.write("\n")


# Creates the Nodes.txt File
def Nodes_filegen(AllNodes):
    # Creates the Nodes.txt File

    # Creates a new file
    with open('Nodes.txt', 'w') as fp:
        pass
        for key, value in sorted(AllNodes.items()):
            fp.write(listToString(value))
            fp.write("\n")


# Loops until the Goal Node is reached
while ((not (np.array_equal(NewNode1, Goal_Node))) and (not (np.array_equal(NewNode2, Goal_Node))) and (
        not (np.array_equal(NewNode3, Goal_Node))) and (not (np.array_equal(NewNode4, Goal_Node)))):
    # global next_node
    Check_and_Add(AllNodes[next_node])
    next_node = next_node + 1

# Function to remove redundant nodes after goal node
clean_AllNodes(AllNodes)

print("")
print("")
print("***********************  AllNodes in Dictionary  ************************")
print("")
print(AllNodes)
print("")
print("")

print("***********************  Parent Nodes  ************************")
print("")
print(ParentNodes)
print("")
print("")

# Function to generate the Goal path from Start node
print("***********************  Shortest path from Start to Goal Node  ************************")
goal_path = generate_path(ParentNodes)
print("")
print("")

# Function to print the Goal path from Start node
print_optimalpath(goal_path)

# Creates the .txt Files
nodePath_filegen(notepad_path)
NodesInfo_filegen(ParentNodes)
Nodes_filegen(AllNodes)
