from fastapi import FastAPI
from backend.api.routes import search, qa, summary, auth

app = FastAPI(title="Academic Paper RAG System")

# Include routers
app.include_router(search.router, prefix="/search", tags=["Search"])
app.include_router(qa.router, prefix="/qa", tags=["Q&A"])
app.include_router(summary.router, prefix="/summary", tags=["Summary"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
