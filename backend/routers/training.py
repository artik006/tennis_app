from fastapi import APIRouter

router = APIRouter(
    prefix="/training",
    tags=["training"]
)

@router.get("/")
def get_training():
    return {"training": []}
