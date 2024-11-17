categorization_prompt = """
You are a tool for breaking down math word problems into structured JSON format.
Do not add the heading and ending ```.

Your task:
    1. Decompose the math word problem into steps.
    2. Each step should include:
        - A unique ID.
        - The mathematical operation performed (only add, sub, mult, div, or identify for recognizing values).
        - The formula of the operation (if applicable).
        - The identifying value of the step (if available). If not available (not value), the value is null.
        - A description of what the step is doing.
        - Dependencies (list of previous step IDs required for this step).
          - Only operations other than identify will have dependencies.
          - There can only be **two dependencies per operation**. 
          - For chained operations with more than two dependencies, break them into smaller steps.
    3. If an operation requires more than two dependencies, create intermediate steps such that each intermediate step depends on at most two prior steps.
    5. Include the exact mathematical operation used (e.g., addition: a + b, division: a / b).

Rules:
    - For chained operations, split into multiple steps. For example:
      - Adding four values (a + b + c + d) becomes:
        - Step 1: Add a and b to get a partial result.
        - Step 2: Add the partial result to c.
        - Step 3: Add the new partial result to d.
    - Always use descriptive names for formulas and descriptions.

Example input: "Sophia collected $5 from her mother, $8 from her father, $12 from her aunt, and $10 from her uncle. She then spent $20 on toys and saved the remaining money. How much money did Sophia save?"

Example output:
{
    "steps": [
        {
            "id": 1,
            "operation": "identify",
            "formula": null,
            "value": 5,
            "description": "Money from mother",
            "dependencies": []
        },
        {
            "id": 2,
            "operation": "identify",
            "formula": null,
            "value": 8,
            "description": "Money from father",
            "dependencies": []
        },
        {
            "id": 3,
            "operation": "add",
            "formula": "partial_sum_1 = money_from_mother + money_from_father",
            "value": null,
            "description": "Sum of money from mother and father",
            "dependencies": [
                1,
                2
            ]
        },
        {
            "id": 4,
            "operation": "identify",
            "formula": null,
            "value": 12,
            "description": "Money from aunt",
            "dependencies": []
        },
        {
            "id": 5,
            "operation": "add",
            "formula": "partial_sum_2 = partial_sum_1 + money_from_aunt",
            "value": null,
            "description": "Add money from aunt to previous sum",
            "dependencies": [
                3,
                4
            ]
        },
        {
            "id": 6,
            "operation": "identify",
            "formula": null,
            "value": 10,
            "description": "Money from uncle",
            "dependencies": []
        },
        {
            "id": 7,
            "operation": "add",
            "formula": "total_money_collected = partial_sum_2 + money_from_uncle",
            "value": null,
            "description": "Add money from uncle to previous total",
            "dependencies": [
                5,
                6
            ]
        },
        {
            "id": 8,
            "operation": "identify",
            "formula": null,
            "value": 20,
            "description": "Money spent on toys",
            "dependencies": []
        },
        {
            "id": 9,
            "operation": "sub",
            "formula": "money_saved = total_money_collected - money_spent",
            "value": null,
            "description": "Calculate remaining money after spending",
            "dependencies": [
                7,
                8
            ]
        }
    ]
}

Example input: "Emma went to a store and bought 3 notebooks for $5 each. She also bought a pen for $2. She had $30 with her. After her purchases, she split the remaining money equally between herself and her friend. How much money did each of them get?"
Example output:
{
    "steps": [
        {
            "id": 1,
            "operation": "identify",
            "formula": null,
            "value": 3,
            "description": "Number of notebooks",
            "dependencies": []
        },
        {
            "id": 2,
            "operation": "identify",
            "formula": null,
            "value": 5,
            "description": "Cost of each notebook",
            "dependencies": []
        },
        {
            "id": 3,
            "operation": "mult",
            "formula": "total_cost_notebooks = number_of_notebooks * cost_per_notebook",
            "value": null,
            "description": "Calculate total cost of notebooks",
            "dependencies": [
                1,
                2
            ]
        },
        {
            "id": 4,
            "operation": "identify",
            "formula": null,
            "value": 2,
            "description": "Cost of pen",
            "dependencies": []
        },
        {
            "id": 5,
            "operation": "add",
            "formula": "total_cost = total_cost_notebooks + cost_of_pen",
            "value": null,
            "description": "Calculate total cost of purchases",
            "dependencies": [
                3,
                4
            ]
        },
        {
            "id": 6,
            "operation": "identify",
            "formula": null,
            "value": 30,
            "description": "Initial amount of money",
            "dependencies": []
        },
        {
            "id": 7,
            "operation": "sub",
            "formula": "remaining_money = initial_money - total_cost",
            "value": null,
            "description": "Calculate remaining money",
            "dependencies": [
                6,
                5
            ]
        },
        {
            "id": 8,
            "operation": "identify",
            "formula": null,
            "value": 2,
            "description": "Split the cost",
            "dependencies": []
        },
        {
            "id": 9,
            "operation": "division",
            "formula": "money_per_person = remaining_money / 2",
            "value": null,
            "description": "Split remaining money between Emma and her friend",
            "dependencies": [
                7,
                8
            ]
        }
    ]
}

Always output JSON in this format, breaking chained operations into multiple steps as described.
"""

result_prompt = """
You are a step-by-step math problem solver.

Your task:
1. Use the provided JSON file containing steps and initial values to solve the math problem sequentially.
2. For each step:
   - State the step ID and its description.
   - Show the operation being performed, including the formula.
   - Display the intermediate result of the calculation for this step.
3. Maintain a list of results corresponding to each step ID, including intermediate and final values.

Input Example:
{
    "steps": [
        {
            "id": 1,
            "operation": "identify",
            "formula": null,
            "value": 5,
            "description": "Money from mother",
            "dependencies": []
        },
        {
            "id": 2,
            "operation": "identify",
            "formula": null,
            "value": 8,
            "description": "Money from father",
            "dependencies": []
        },
        {
            "id": 3,
            "operation": "add",
            "formula": "partial_sum_1 = money_from_mother + money_from_father",
            "value": null,
            "description": "Sum of money from mother and father",
            "dependencies": [
                1,
                2
            ]
        },
        {
            "id": 4,
            "operation": "identify",
            "formula": null,
            "value": 20,
            "description": "Money spent on toys",
            "dependencies": []
        },
        {
            "id": 5,
            "operation": "sub",
            "formula": "money_saved = partial_sum_1 - money_spent",
            "value": null,
            "description": "Calculate remaining money",
            "dependencies": [
                3,
                4
            ]
        }
    ]
}
{1: 5, 2: 8, 3: 13, 4: 20, 5: -7}

Output Example:
Step-by-Step Process:
1. [Step 1] Identify value: Money from mother = 5
   Result: 5
2. [Step 2] Identify value: Money from father = 8
   Result: 8
3. [Step 3] Add values: Sum of money from mother and father (5 + 8)
   Result: 13
4. [Step 4] Identify value: Money spent on toys = 20
   Result: 20
5. [Step 5] Subtract values: Remaining money (13 - 20)
   Result: -7

Do not add anything after the step by step process.

Guidelines:
- Follow the dependencies to calculate each step in order.
- Ensure clear, concise descriptions of each operation and result.
"""
