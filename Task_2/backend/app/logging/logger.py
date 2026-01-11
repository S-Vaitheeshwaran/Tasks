import requests
from datetime import datetime
from app.config import DIRECTUS_URL, DIRECTUS_TOKEN

HEADERS = {
    "Authorization": f"Bearer {DIRECTUS_TOKEN}",
    "Content-Type": "application/json"
}

def log_experiment(data: dict):
    data["timestamp"] = datetime.utcnow().isoformat()

    requests.post(
        f"{DIRECTUS_URL}/items/llm_experiment_logs",
        json=data,
        headers=HEADERS
    )
