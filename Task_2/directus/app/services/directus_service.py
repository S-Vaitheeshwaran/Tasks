import httpx
from app.config import DIRECTUS_URL, DIRECTUS_TOKEN

HEADERS = {
    "Authorization": f"Bearer {DIRECTUS_TOKEN}",
    "Content-Type": "application/json"
}

async def create_experiment(data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{DIRECTUS_URL}/items/experiments",
            json=data,
            headers=HEADERS
        )
        response.raise_for_status()
        return response.json()["data"]

async def get_experiments():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{DIRECTUS_URL}/items/experiments",
            headers=HEADERS
        )
        response.raise_for_status()
        return response.json()["data"]

async def get_experiment_by_id(exp_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{DIRECTUS_URL}/items/experiments/{exp_id}",
            headers=HEADERS
        )
        response.raise_for_status()
        return response.json()["data"]
