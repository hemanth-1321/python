import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, g=0, h=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.g = g  # Cost to reach this node
        self.h = h  # Heuristic estimate to the goal

    def total_cost(self):
        return self.g + self.h

def ao_star_search(start_state, goal_state, neighbors_fn, heuristic_fn, epsilon):
    open_set = []
    closed_set = set()
    start_node = Node(start_state, None, 0, 0, heuristic_fn(start_state))
    heapq.heappush(open_set, (start_node.total_cost(), id(start_node), start_node))
    
    while open_set:
        current_node = heapq.heappop(open_set)[2]
        
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]
        
        closed_set.add(current_node.state)
        
        for neighbor_state in neighbors_fn(current_node.state):
            if neighbor_state in closed_set:
                continue
            
            neighbor_node = Node(neighbor_state)
            neighbor_node.parent = current_node
            neighbor_node.g = current_node.g + 1  # Assuming uniform cost
            neighbor_node.h = heuristic_fn(neighbor_state)
            
            if any(neighbor_node.state == node.state for _, __, node in open_set):
                continue
            
            priority = neighbor_node.total_cost() + epsilon * neighbor_node.h
            heapq.heappush(open_set, (priority, id(neighbor_node), neighbor_node))
    
    return None

# Example usage:
def neighbors(state):
    x, y = state
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return [(x + dx, y + dy) for dx, dy in movements]

def heuristic(state):
    x, y = state
    goal_x, goal_y = 4, 4
    return abs(x - goal_x) + abs(y - goal_y)

start_state = (0, 0)
goal_state = (4, 4)
epsilon = 0.5
path = ao_star_search(start_state, goal_state, neighbors, heuristic, epsilon)
print("Path:", path)
