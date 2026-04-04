import os

import requests
from urllib3 import request


def delete_voice(voice_id):
    headers = {
        "Authorization": f"Bearer {os.getenv('API_KEY')}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "voice-enrollment",
        "input": {
            "action": "delete_voice",
            "voice_id": voice_id
        }
    }
    response = requests.post(os.getenv("VOICE_URL"), headers=headers, json=data)
    return response.json()
