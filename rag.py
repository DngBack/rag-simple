"""
RAG pipeline: load PDF from docs/, chunk, embed (OpenAI), retrieve.
Used by demo4_rag_pipeline.py.
"""
import os
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

load_dotenv()

DEFAULT_PDF = Path(__file__).resolve().parent / "docs" / "gaudi-3-ai-accelerator-white-paper.pdf"
CHUNK_SIZE = 600
CHUNK_OVERLAP = 80
TOP_K = 4
EMBEDDING_MODEL = "text-embedding-3-small"


def get_client() -> OpenAI:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not set.")
    return OpenAI(api_key=key)


def extract_text_from_pdf(path: Path) -> str:
    reader = PdfReader(path)
    parts = []
    for page in reader.pages:
        parts.append(page.extract_text() or "")
    return "\n".join(parts)


def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end - overlap
    return chunks


def embed_chunks(client: OpenAI, chunks: list[str]) -> np.ndarray:
    resp = client.embeddings.create(model=EMBEDDING_MODEL, input=chunks)
    return np.array([e.embedding for e in resp.data], dtype=np.float32)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))


def build_index(pdf_path: Path | None = None) -> tuple[list[str], np.ndarray]:
    path = pdf_path or DEFAULT_PDF
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")
    text = extract_text_from_pdf(path)
    chunks = chunk_text(text)
    if not chunks:
        raise ValueError("No chunks from PDF.")
    client = get_client()
    vectors = embed_chunks(client, chunks)
    return chunks, vectors


def retrieve(
    query: str,
    chunks: list[str],
    vectors: np.ndarray,
    client: OpenAI | None = None,
    top_k: int = TOP_K,
) -> list[str]:
    client = client or get_client()
    q_emb = embed_chunks(client, [query])[0]
    scores = np.array([cosine_similarity(q_emb, v) for v in vectors])
    idx = np.argsort(scores)[::-1][:top_k]
    return [chunks[i] for i in idx]
