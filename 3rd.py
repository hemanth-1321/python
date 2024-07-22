import heapq

# Define a class to represent nodes in the search tree
class Node:
    # Constructor to initialize a node with its state, parent node, cost, and heuristic
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state          # The state represented by this node
        self.parent = parent        # The parent node in the search tree
        self.cost = cost            # The cost to reach this node from the start node
        self.heuristic = heuristic  # The estimated cost from this node to the goal

    # Method to calculate the total cost of the node (cost + heuristic)
    def total_cost(self):
        return self.cost + self.heuristic

# A* search function to find a path from start_state to goal_state
def astar_search(start_state, goal_state, neighbors_fn, heuristic_fn):
    open_set = []                   # Priority queue to store nodes to be explored
    closed_set = set()              # Set to store states that have already been explored

    # Create the starting node with its state and heuristic value
    start_node = Node(start_state, cost=0, heuristic=heuristic_fn(start_state))

    # Push the starting node into the priority queue with its total cost as priority
    heapq.heappush(open_set, (start_node.total_cost(), id(start_node), start_node))

    # Loop until all nodes in the open_set have been explored
    while open_set:
        # Pop the node with the lowest total cost from the priority queue
        current_node = heapq.heappop(open_set)[2]

        # If we reach the goal state, reconstruct and return the path
        if current_node.state == goal_state:
            path = []
            # Trace back from the goal node to the start node to construct the path
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get it from start to goal

        # Add the current state to the closed_set, marking it as explored
        closed_set.add(current_node.state)

        # Explore neighbors of the current state
        for neighbor_state in neighbors_fn(current_node.state):
            # Skip this neighbor if it has already been explored
            if neighbor_state in closed_set:
                continue

            # Create a new node for the neighbor state
            neighbor_node = Node(neighbor_state)

            # Set the parent of the neighbor node to the current node
            neighbor_node.parent = current_node

            # Calculate the cost to reach this neighbor (assuming uniform cost of 1 per step)
            neighbor_node.cost = current_node.cost + 1

            # Calculate the heuristic value for the neighbor state
            neighbor_node.heuristic = heuristic_fn(neighbor_state)

            # Check if the neighbor is already in the open_set
            in_open_set = any(node.state == neighbor_state for (_, __, node) in open_set)
            if in_open_set:
                continue  # Skip this neighbor if it's already in the open_set

            # Push the neighbor node into the priority queue with its total cost as priority
            heapq.heappush(open_set, (neighbor_node.total_cost(), id(neighbor_node), neighbor_node))

    # Return None if no path is found
    return None

# Example function to get neighboring states (up, down, left, right movements)
def neighbors(state):
    x, y = state
    movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return [(x + dx, y + dy) for dx, dy in movements]

# Example heuristic function (Manhattan distance to the goal state)
def heuristic(state, goal=(4, 4)):
    goal_x, goal_y = goal
    x, y = state
    return abs(x - goal_x) + abs(y - goal_y)

# Example usage of the A* search algorithm
start_state = (0, 0)
goal_state = (4, 4)
path = astar_search(start_state, goal_state, neighbors, heuristic)
print("Path:", path)
