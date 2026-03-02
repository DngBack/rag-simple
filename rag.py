"""
RAG pipeline: load PDF from docs/, chunk, embed (OpenAI), retrieve.
Used by demo4_rag_pipeline.py.
"""
import os
from pathlib import Path

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI
from pdf2image import convert_from_path
import pytesseract

load_dotenv()

DEFAULT_PDF = Path(__file__).resolve().parent / "docs" / "luat109-2025.pdf"
INDEX_CACHE_DIR = Path(__file__).resolve().parent / ".index_cache"
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
    images = convert_from_path(str(path), dpi=200)
    parts = []
    for img in images:
        text = pytesseract.image_to_string(img, lang="vie")
        parts.append(text)
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


def save_index(chunks: list[str], vectors: np.ndarray, cache_dir: Path = INDEX_CACHE_DIR) -> None:
    """Save chunks and vectors to disk for fast reuse."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    import json
    (cache_dir / "chunks.json").write_text(json.dumps(chunks, ensure_ascii=False), encoding="utf-8")
    np.save(str(cache_dir / "vectors.npy"), vectors)
    print(f"[cache] Saved {len(chunks)} chunks to {cache_dir}")


def load_index(cache_dir: Path = INDEX_CACHE_DIR) -> tuple[list[str], np.ndarray]:
    """Load chunks and vectors from disk. Raises FileNotFoundError if cache missing."""
    import json
    chunks_path = cache_dir / "chunks.json"
    vectors_path = cache_dir / "vectors.npy"
    if not chunks_path.exists() or not vectors_path.exists():
        raise FileNotFoundError(f"Index cache not found at {cache_dir}. Run: python rag.py")
    chunks = json.loads(chunks_path.read_text(encoding="utf-8"))
    vectors = np.load(str(vectors_path))
    print(f"[cache] Loaded {len(chunks)} chunks from {cache_dir}")
    return chunks, vectors


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


if __name__ == "__main__":
    print("Building index from PDF (OCR + embed)...")
    chunks, vectors = build_index(DEFAULT_PDF)
    save_index(chunks, vectors)
    print(f"Done. {len(chunks)} chunks ready. Run 'python app.py' to start the web app.")
