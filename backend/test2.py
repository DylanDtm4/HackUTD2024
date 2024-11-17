from utils.app_samba import prompt_Samba_json, prompt_Samba_result
from utils.app_solver import solve

json_string = prompt_Samba_json('A school purchased 40 sets of chairs and desks. Each set costs $125. Later, 10 sets were found defective and returned. What is the total cost for the remaining sets?')

results = solve(json_string)

print(prompt_Samba_result(results, json_string))
