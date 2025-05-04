from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def ask_question(question: str):
    return {"answer": f"Answer for: {question}"}
