from collections import defaultdict


def index_2d(myList: list, value):
    for i, x in enumerate(myList):
        if value in x:
            return (i, x.index(value))


def indexes_2d(myList: list, value):
    matched_indexes = []
    for pos, x in enumerate(myList):
        [matched_indexes.append((pos, i)) for i, x in enumerate(x) if x == value]
    return matched_indexes


# Input text
with open("day12/input.txt", 'rt') as f:
    input_string = f.readlines()

# Parse into 2D list
map_list = []
map_num_list = []
for line in input_string:
    line_list = []
    line_list[:0] = line.replace("\n", "")
    map_list.append([item for item in line_list])
    map_num_list.append([ord(item)for item in line_list])

# Update values of S and E fields
x, y = index_2d(map_list, 'S')
map_num_list[x][y] = ord('a')
x, y = index_2d(map_list, 'E')
map_num_list[x][y] = ord('z')

edges = []

len_x, len_y = len(map_list), len(map_list[0])

for x, line in enumerate(map_num_list):
    for y, cell in enumerate(line):

        if x+1 < len_x and map_num_list[x][y] - map_num_list[x+1][y] >= -1:
            edges.append([(x, y), (x+1, y)])
        if x > 0 and map_num_list[x][y] - map_num_list[x-1][y] >= -1:
            edges.append([(x, y), (x-1, y)])
        if y+1 < len_y and map_num_list[x][y] - map_num_list[x][y+1] >= -1:
            edges.append([(x, y), (x, y+1)])
        if y > 0 and map_num_list[x][y] - map_num_list[x][y-1] >= -1:
            edges.append([(x, y), (x, y-1)])


def build_graph(edges):
    graph = defaultdict(list)

    # Loop to iterate over every edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]

        # Creating the graph as adjacency list, just one direction
        graph[a].append(b)
    return graph


# Function to find the shortest path between two nodes of a graph
def BFS_SP(graph, start, goal):
    explored = set()

    # Queue for traversing the graph in the BFS
    queue = [[start]]

    # If the desired node is reached
    if start == goal:
        print("Same Node")
        return 0

    # Loop to traverse the graph with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the neighbour node is the goal
                if neighbour == goal:
                    return len(new_path)-1
            explored.add(node)

    # Condition when the nodes are not connected
    return 0


graph = build_graph(edges)

# S point and every 'a' point on the map
source_points = []
source_points.append(index_2d(map_list, 'S'))
source_points = source_points + indexes_2d(map_list, 'a')
# End
destination = index_2d(map_list, 'E')

count_list = []
for source in source_points:
    # Function Call
    item = BFS_SP(graph, source, destination)
    if item != 0:
        count_list.append(item)

print(min(count_list))
