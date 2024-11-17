import json
from datetime import datetime
import openai
import samba_prompts
client = openai.OpenAI(
    api_key="be0a187e-4e03-4a41-b612-7bd5f41700a0",
    base_url="https://api.sambanova.ai/v1",
)

def prompt_Samba(prompt):
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-70B-Instruct',
        messages=[{"role":"system","content":samba_prompts.categorization_prompt},{"role":"user","content":prompt}],
        temperature =  0.2,
        top_p = 0.8
    )

    # Generate a unique filename based on timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"response_{timestamp}.json"

    # Write the JSON response to the new file
    with open(filename, "w") as json_file:
        json.dump(response, json_file, indent=4)

    print(f"Response saved to {filename}")