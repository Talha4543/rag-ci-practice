from fastapi import FastAPI
from pydantic import BaseModel

from app.logic import chunk_text

app = FastAPI(title="RAG CI practice API")


@app.get("/health")
def health():
    return {"status": "ok"}


class ChunkRequest(BaseModel):
    text: str
    chunk_size: int = 200
    overlap: int = 20


@app.post("/chunk")
def chunk(req: ChunkRequest):
    chunks = chunk_text(req.text, req.chunk_size, req.overlap)
    return {"count": len(chunks), "chunks": chunks}
