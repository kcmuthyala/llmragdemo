import os
import requests

#API_TOKEN = os.environ["API_TOKEN"] #Set a API_TOKEN environment variable before running
API_TOKEN = "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"
#API_URL = "https://api-inference.huggingface.co/models/llm-agents/tora-13b-v1.0" #Add a URL for a model of your choosing
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	payload = {
        "inputs": payload,
        "parameters": { #Try and experiment with the parameters
            "max_new_tokens": 1024,
            "temperature": 0.6,
            "top_p": 0.9,
            "do_sample": False,
            "return_full_text": False
        }
    }
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query("Can you please let us know more details about your")

print(output)


