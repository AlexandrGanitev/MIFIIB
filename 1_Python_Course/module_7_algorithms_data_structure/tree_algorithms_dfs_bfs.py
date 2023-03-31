print("Поиск в глубину depth-first search,DFS алгоритм")
# Using a Python dictionary to act as an adjacency list
'''The illustrated graph is represented using
an adjacency list - an easy way to do it in Python
is to use a dictionary data structure.
Each vertex has a list of its adjacent nodes stored.'''
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : [],
    'D' : [],
    'E' : []
}

# visited is a set that is used to keep track of visited nodes.
visited = set()

'''dfs follows the algorithm described:
1. It first checks if the current node is unvisited - if yes, it is appended in the visited set.
2. Then for each neighbor of the current node, the dfs function is invoked again.
3. The base case is invoked when all the nodes are visited. The function then returns.'''

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

# Driver Code
'''The dfs function is called and is passed the visited set,
the graph in the form of a dictionary, and A, 
which is the starting node (root node).'''
dfs(visited, graph, 'A')

print("Поиск в ширину breadth-first search,BFS алгоритм")
'''The illustrated graph is represented using an adjacency list. 
An easy way to do this in Python is to use a dictionary data structure,
where each vertex has a stored list of its adjacent nodes.'''
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : [],
    'D' : [],
    'E' : []
}

visited = []  # List to keep track of visited nodes.
# queue is a list that is used to keep track of nodes currently in the queue.
queue = []  # Initialize a queue

'''bfs follows the algorithm:
1. It checks and appends the starting node to the visited list and the queue.
2. Then, while the queue contains elements, 
it keeps taking out nodes from the queue, 
appends the neighbors of that node to the queue if they are unvisited, 
and marks them as visited.
3. This continues until the queue is empty.'''


def bfs(visited, graph, node) :
    visited.append(node)
    queue.append(node)

    while queue :
        s = queue.pop(0)
        print(s, end=" ")

        for neighbor in graph[s] :
            if neighbor not in visited :
                visited.append(neighbor)
                queue.append(neighbor)


# Driver Code
'''The arguments of the bfs function are the visited list, 
the graph in the form of a dictionary, 
and the starting node A.'''
bfs(visited, graph, 'A')