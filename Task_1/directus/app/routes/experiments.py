from fastapi import APIRouter, HTTPException
from app.schemas import ExperimentCreate
from app.services.directus_service import (
    create_experiment,
    get_experiments,
    get_experiment_by_id
)
import httpx

router = APIRouter(prefix="/experiments", tags=["Experiments"])


@router.post("/")
async def create(data: ExperimentCreate):
    try:
        return await create_experiment(data.dict())
    except httpx.HTTPStatusError as e:
        # Show actual Directus error
        raise HTTPException(
            status_code=e.response.status_code,
            detail=e.response.json()
        )
    except httpx.RequestError as e:
        # Network / connection issues
        raise HTTPException(
            status_code=500,
            detail=f"Directus connection error: {str(e)}"
        )


@router.get("/")
async def list_all():
    try:
        return await get_experiments()
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=e.response.json()
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Directus connection error: {str(e)}"
        )


@router.get("/{experiment_id}")
async def get_by_id(experiment_id: int):
    try:
        return await get_experiment_by_id(experiment_id)
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=e.response.json()
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Directus connection error: {str(e)}"
        )
