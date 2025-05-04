from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def summarize(paper_id: str):
    return {"summary": f"Summary of paper: {paper_id}"}
