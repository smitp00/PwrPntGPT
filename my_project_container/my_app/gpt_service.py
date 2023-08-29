# my_app/gpt_service.py

import requests
import json

def get_summary_from_gpt(content):
    api_key = "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"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "prompt": f"Summarize the following text into bullet points in few sentences\n{content}",
        "max_tokens": 500  # You can set the max tokens based on your requirement
    }
    
    response = requests.post("https://api.openai.com/v1/engines/davinci/completions", headers=headers, json=data)
    
    if response.status_code == 200:
        result = json.loads(response.text)
        summary = result['choices'][0]['text'].strip()
        return summary
    else:
        string = "Error:", response.status_code, response.text
        return string