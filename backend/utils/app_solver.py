import json
from collections import defaultdict, deque

def solve(filename):
    # Step 1: Read JSON data from file
    with open(filename, "r") as file:
        data = json.load(file)

    # Step 2: Parse data
    steps = data["steps"]
    root_parameters = data["root_parameters"]

    # Build graph and track in-degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Map step IDs to their data
    step_map = {step["id"]: step for step in steps}

    # Populate the graph and in-degree
    for step in steps:
        for dep in step["dependencies"]:
            graph[dep].append(step["id"])
            in_degree[step["id"]] += 1

    # Step 3: Topological Sort using Kahn's Algorithm
    queue = deque([node for node in step_map if in_degree[node] == 0])  # Start with root nodes
    topological_order = []

    while queue:
        current = queue.popleft()
        topological_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Compute values
    results = {}
    for step_id in topological_order:
        step = step_map[step_id]
        operation = step["operation"]
        dependencies = step["dependencies"]

        # Fetch dependency values
        dep_values = [results[dep] for dep in dependencies]

        # Perform operations
        if operation == "identify":
            results[step_id] = step["value"]
        elif operation == "division" and len(dep_values) == 2:
            results[step_id] = dep_values[0] / dep_values[1]

    # Print Results
    print("Computed Values:")
    for step_id, value in results.items():
        print(f"Step {step_id}: {value}")

    
