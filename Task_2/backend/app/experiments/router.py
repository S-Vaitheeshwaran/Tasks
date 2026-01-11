from fastapi import APIRouter, HTTPException
import requests

from app.config import DIRECTUS_URL, DIRECTUS_TOKEN
from app.llm.client import LLMClient
from app.experiments.service import run_document_qa

router = APIRouter()

HEADERS = {
    "Authorization": f"Bearer {DIRECTUS_TOKEN}",
    "Content-Type": "application/json"
}

@router.post("/experiments/{experiment_id}/run")
def run_experiment(experiment_id: str, question: str):
    try:
        # 1️⃣ Fetch experiment (SAFE)
        exp_res = requests.get(
            f"{DIRECTUS_URL}/items/llm_experiments/{experiment_id}",
            headers=HEADERS
        )

        if exp_res.status_code != 200:
            raise HTTPException(status_code=404, detail="Experiment not found")

        experiment = exp_res.json().get("data")
        if experiment is None:
            raise HTTPException(status_code=404, detail="Experiment not found")

        # 2️⃣ Update status → running
        requests.patch(
            f"{DIRECTUS_URL}/items/llm_experiments/{experiment_id}",
            json={"status": "running"},
            headers=HEADERS
        )

        # 3️⃣ Run LLM
        llm = LLMClient()
        answer = run_document_qa(experiment, question, llm)

        # 4️⃣ Update status → completed
        requests.patch(
            f"{DIRECTUS_URL}/items/llm_experiments/{experiment_id}",
            json={"status": "completed"},
            headers=HEADERS
        )

        return {"answer": answer}

    except HTTPException:
        raise

    except Exception as e:
        # 5️⃣ Update status → failed
        requests.patch(
            f"{DIRECTUS_URL}/items/llm_experiments/{experiment_id}",
            json={"status": "failed"},
            headers=HEADERS
        )
        raise HTTPException(status_code=500, detail=str(e))
