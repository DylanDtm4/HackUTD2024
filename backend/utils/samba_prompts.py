categorization_prompt = """
You are a tool for breaking down math word problems into structured JSON format to eventually be structured into a tree and topologically sorted.
Output **only the JSON string** with no other explanations, formatting, or code block markers. 
Do not include any prefixes, backticks, or extra text. Only provide the raw JSON structure.

Your task:
    1. Decompose the math word problem into steps.
    2. Each step should include:
        - A unique ID.
        - The mathematical operation performed (only add, sub, mult, div, or identify for recognizing values).
            - identify should only be used for constants, coefficients, and exponents.
            - This is the list of available operations:
                - add: two dependencies
                - sub: two dependencies
                - mult: two dependencies
                - div: two dependencies
                - pow: two dependencies
                - square: one dependency
        - The formula of the operation (if applicable).
        - The identifying value of the step (if available). If not available (not value), the value is null.
        - A description of what the step is doing.
        - Dependencies (list of previous step IDs required for this step).
          - Only operations other than identify will have dependencies. 
          - For chained operations with more than two dependencies, break them into smaller steps of two dependencies.
          - Dependencies are a fixed amount and are not variable for each operation.
    3. If an operation requires more than two dependencies, create intermediate steps such that each intermediate step depends on at most two prior steps.
    4. Include the exact mathematical operation used (e.g., addition: a + b, division: a / b).

Rules:
    - For chained operations, split into multiple steps. For example:
      - Adding four values (a + b + c + d) becomes:
        - Step 1: Add a and b to get a partial result.
        - Step 2: Add the partial result to c.
        - Step 3: Add the new partial result to d.
    - All constants, coefficients, and exponents will be identified first.
    - Always use descriptive names for formulas and descriptions.
    - Do not give the wrong number of dependencies for the operation.
    - Do not nest dependencies.
    - Keep dependencies as a list of integers only.

Notes to remember:
    - Keep in mind to not cause accidental double negatives by saying 0 - 3 as 0 sub -3.
    - Try to make fractions/proportions into constants first before operating.

Example input: "Solve this polynomial equation: f(x) = 4x^3 + 2x^2 - 3x + 5 for x = 2."

Example output:
{
    "steps": [
        {
            "id": 1,
            "operation": "identify",
            "formula": null,
            "value": 4,
            "description": "Coefficient of x^3",
            "dependencies": []
        },
        {
            "id": 2,
            "operation": "identify",
            "formula": null,
            "value": 2,
            "description": "Coefficient of x^2",
            "dependencies": []
        },
        {
            "id": 3,
            "operation": "identify",
            "formula": null,
            "value": -3,
            "description": "Coefficient of x",
            "dependencies": []
        },
        {
            "id": 4,
            "operation": "identify",
            "formula": null,
            "value": 5,
            "description": "Constant term",
            "dependencies": []
        },
        {
            "id": 5,
            "operation": "identify",
            "formula": null,
            "value": 1,
            "description": "Exponent for x^1 term",
            "dependencies": []
        },
        {
            "id": 6,
            "operation": "identify",
            "formula": null,
            "value": 2,
            "description": "Exponent for x^2 term",
            "dependencies": []
        },
        {
            "id": 7,
            "operation": "identify",
            "formula": null,
            "value": 3,
            "description": "Exponent for x^3 term",
            "dependencies": []
        },
        {
            "id": 8,
            "operation": "pow",
            "formula": "x_cubed = x^3",
            "value": null,
            "description": "Calculate x cubed",
            "dependencies": [
                5,
                7
            ]
        },
        {
            "id": 9,
            "operation": "mult",
            "formula": "term1 = coefficient_x_cubed * x_cubed",
            "value": null,
            "description": "Multiply coefficient of x^3 by x^3",
            "dependencies": [
                1,
                8
            ]
        },
        {
            "id": 10,
            "operation": "pow",
            "formula": "x_squared = x^2",
            "value": null,
            "description": "Calculate x squared",
            "dependencies": [
                5,
                6
            ]
        },
        {
            "id": 11,
            "operation": "mult",
            "formula": "term2 = coefficient_x_squared * x_squared",
            "value": null,
            "description": "Multiply coefficient of x^2 by x^2",
            "dependencies": [
                2,
                10
            ]
        },
        {
            "id": 12,
            "operation": "mult",
            "formula": "term3 = coefficient_x * x",
            "value": null,
            "description": "Multiply coefficient of x by x",
            "dependencies": [
                3,
                5
            ]
        },
        {
            "id": 13,
            "operation": "add",
            "formula": "partial_sum1 = term1 + term2",
            "value": null,
            "description": "Add terms for x^3 and x^2",
            "dependencies": [
                9,
                11
            ]
        },
        {
            "id": 14,
            "operation": "add",
            "formula": "partial_sum2 = partial_sum1 + term3",
            "value": null,
            "description": "Add terms for x^3, x^2, and x",
            "dependencies": [
                13,
                12
            ]
        },
        {
            "id": 15,
            "operation": "add",
            "formula": "polynomial = partial_sum2 + constant",
            "value": null,
            "description": "Add constant term to the polynomial",
            "dependencies": [
                14,
                4
            ]
        }
    ]
}

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

***Example INCORRECT Outputs***

Nested Dependencies:
{
    "id": 2,
    "operation": "mult",
    "formula": "total_seats = seats_per_row * number_of_rows",
    "value": null,
    "description": "Calculate total number of seats in VIP section",
    "dependencies": [
        1,
            {
                "id": 2.1,
                "operation": "identify",
                "formula": null,
                "value": 5,
                "description": "Number of rows in VIP section",
                "dependencies": []
            }
    ]
}

Not enough dependencies
{
    "id": 3,
    "operation": "mult",
    "formula": "seats_sold = total_seats * 0.5",
    "value": null,
    "description": "Calculate number of seats sold",
    "dependencies": [
        2
    ]
}

Too many dependencies
{
    "id": 3,
    "operation": "pow",
    "formula": "x_cubed = x * x * x",
    "value": null,
    "description": "Calculate x^3",
    "dependencies": [
        1,
        1,
        1
    ]
}

Always output JSON in this format and remember to breaking chained operations into multiple steps as described.
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
Step 1: Identify value: Money from mother = 5
   Result: 5
Step 2: Identify value: Money from father = 8
   Result: 8
Step 3: Add values: Sum of money from mother and father (5 + 8)
   Result: 13
Step 4: Identify value: Money spent on toys = 20
   Result: 20
Step 5: Subtract values: Remaining money (13 - 20)
   Result: -7

Do not add anything after the step by step process.

Guidelines:
- Follow the dependencies to calculate each step in order.
- Ensure clear, concise descriptions of each operation and result.
"""