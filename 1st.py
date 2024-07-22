class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

    def __str__(self):
        return f"({self.jug1}, {self.jug2})"

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def path(self):
        if self.parent is None:
            return [self.state]
        return self.parent.path() + [self.state]

def dfs(start_state, goal_state):
    visited = set()
    stack = [Node(start_state)]

    while stack:
        node = stack.pop()
        state = node.state

        if state == goal_state:
            return node.path()

        visited.add(state)

        # Possible actions
        actions = [
            (4, state.jug2),  # Fill jug1
            (state.jug1, 3),  # Fill jug2
            (0, state.jug2),  # Empty jug1
            (state.jug1, 0),  # Empty jug2
            (min(state.jug1 + state.jug2, 4), max(0, state.jug2 - (4 - state.jug1))),  # Pour from jug2 to jug1
            (max(0, state.jug1 - (3 - state.jug2)), min(state.jug1 + state.jug2, 3))  # Pour from jug1 to jug2
        ]

        for action in actions:
            new_state = State(action[0], action[1])
            if new_state not in visited:
                stack.append(Node(new_state, node))

    return None

# Test the algorithm
start_state = State(0, 0)  # Initial state: both jugs are empty
goal_state = State(2, 0)   # Goal state: jug1 has 2 units of water

print("Starting DFS for Water Jug Problem...")
path = dfs(start_state, goal_state)

if path:
    print("Solution found! Steps to reach the goal:")
    for i, state in enumerate(path):
        print(f"Step {i}: Jug1: {state.jug1}, Jug2: {state.jug2}")
else:
    print("No solution found!")
