from fastapi import APIRouter

router = APIRouter(
    prefix="/news",
    tags=["news"]
)

@router.get("/")
def get_news():
    return {"news": []}
