import os
import json
from datetime import datetime
import openai
import utils.samba_prompts as samba_prompts

client = openai.OpenAI(
    api_key="90a7b7fe-206a-4f84-8122-a9d9879a8e21",
    base_url="https://api.sambanova.ai/v1",
)

def prompt_Samba_json(prompt):
    # Call the API and get the response
    response = client.chat.completions.create(
        model='Meta-Llama-3.1-405B-Instruct',
        messages=[{"role": "system", "content": samba_prompts.categorization_prompt},
                  {"role": "user", "content": prompt}],
        temperature=0.2,
        top_p=0.8
    )
    
    return response.choices[0].message.content

def prompt_Samba_result(results, json_string):
    # Call the API and get the response
    prompt = json_string + '\n' + str(results)

    response = client.chat.completions.create(
        model='Meta-Llama-3.1-405B-Instruct',
        messages=[{"role": "system", "content": samba_prompts.result_prompt},
                  {"role": "user", "content": prompt}],
        temperature=0.1,
        top_p=0.8
    )
    
    return response.choices[0].message.content
