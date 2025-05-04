from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def search_papers(query: str):
    return {"message": f"Search papers for: {query}"}
