import heapq

def a_star(graph, heuristic, start, goal):
    """
    A* algorithm for finding shortest path in a graph.

    Parameters:
    - graph: dict, adjacency list {node: [(neighbor, cost), ...]}
    - heuristic: dict, estimated cost from node to goal {node: h(n)}
    - start: starting node
    - goal: goal node

    Returns:
    - path: list of nodes from start to goal
    - total_cost: cost of the path
    """
    
    # Priority queue for nodes to explore: (f_cost, node)
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], start))
    
    # Cost from start to node
    g_cost = {start: 0}
    
    # Parent dictionary for path reconstruction
    parent = {start: None}
    
    while open_list:
        current_f, current = heapq.heappop(open_list)
        
        # Goal check
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, g_cost[goal]
        
        # Explore neighbors
        for neighbor, cost in graph.get(current, []):
            tentative_g = g_cost[current] + cost
            
            # If neighbor not visited or found a cheaper path
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic.get(neighbor, 0)
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current
    
    # Goal not reachable
    return None, float('inf')


# Example usage
if __name__ == "__main__":
    # Define the graph (adjacency list)
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }

    # Define heuristic values (h(n))
    heuristic = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 0
    }

    start_node = 'A'
    goal_node = 'D'

    path, total_cost = a_star(graph, heuristic, start_node, goal_node)
    print("Shortest path:", path)
    print("Total cost:", total_cost)
