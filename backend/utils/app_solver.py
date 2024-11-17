import json
from collections import defaultdict, deque
from . import app_math

def solve(json_string):
    # Load the JSON data
    data = json.loads(json_string)

    # Parse steps
    steps = data["steps"]
    last_step_id = steps[-1]["id"]  # Identify the last step's ID

    # Build graph and in-degree tracker
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    step_map = {step["id"]: step for step in steps}

    # Populate the graph
    for step in steps:
        for dep in step["dependencies"]:
            graph[dep].append(step["id"])
            in_degree[step["id"]] += 1

    # Topological sort using Kahn's Algorithm
    queue = deque([node for node in step_map if in_degree[node] == 0 and node != last_step_id])
    topological_order = []

    while queue:
        current = queue.popleft()
        topological_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0 and neighbor != last_step_id:
                queue.append(neighbor)

    # Ensure the last step is added last
    if in_degree[last_step_id] == 0:
        topological_order.append(last_step_id)

    # Compute results
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
        elif (operation == "add" or operation == "addition") and len(dep_values) == 2:
            results[step_id] = app_math.add(dep_values[0], dep_values[1])
        elif (operation == "sub" or operation == "subtract") and len(dep_values) == 2:
            results[step_id] = app_math.sub(dep_values[0], dep_values[1])
        elif (operation == "mult" or operation == "multiply") and len(dep_values) == 2:
            results[step_id] = app_math.mult(dep_values[0], dep_values[1])
        elif (operation == "div" or operation == "division") and len(dep_values) == 2:
            results[step_id] = app_math.divide(dep_values[0], dep_values[1])
        else:
            raise ValueError(f"Unsupported operation or missing dependencies for step {step_id}")

    return results  # Return computed results
