#!/usr/bin/env python3
"""
Demo 4 — Pipeline RAG: user prompt → retrieved context → final answer.
Uses docs/gaudi-3-ai-accelerator-white-paper.pdf. Optionally shows a "retrieve wrong" case.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from llm import chat, get_client, DEFAULT_MODEL
from rag import build_index, retrieve, DEFAULT_PDF

TRANSCRIPT_DIR = Path(__file__).resolve().parent / "demo-kit" / "transcripts"

SYSTEM_PROMPT = """Bạn trả lời dựa CHỈ vào Context dưới đây. Nếu thông tin không có trong Context, hãy nói rõ "Không có trong tài liệu."
Context:
{context}
"""


def run_rag_query(
    query: str,
    chunks: list[str],
    vectors,
    client,
    *,
    top_k: int = 4,
    temperature: float = 0.3,
):
    retrieved = retrieve(query, chunks, vectors, client=client, top_k=top_k)
    context = "\n\n---\n\n".join(retrieved)
    system = SYSTEM_PROMPT.format(context=context)
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": query},
    ]
    answer, _ = chat(
        messages,
        model=DEFAULT_MODEL,
        temperature=temperature,
        transcript_dir=TRANSCRIPT_DIR,
    )
    return retrieved, answer


def main():
    print("Loading PDF and building index...")
    chunks, vectors = build_index(DEFAULT_PDF)
    client = get_client()
    transcript_dir = TRANSCRIPT_DIR
    transcript_dir.mkdir(parents=True, exist_ok=True)

    # Case 1: query that should retrieve correct context
    query1 = "Intel Gaudi 3 có bao nhiêu HBM memory và bandwidth? Nêu ngắn gọn số liệu."
    print("\n" + "=" * 60)
    print("USER PROMPT:", query1)
    print("=" * 60)
    ret1, ans1 = run_rag_query(query1, chunks, vectors, client)
    print("\nRETRIEVED CONTEXT (excerpts):")
    for i, c in enumerate(ret1[:2], 1):
        print(f"  [{i}] {c[:200]}...")
    print("\nFINAL ANSWER:")
    print(ans1)

    # Case 2 (optional): query that may retrieve less relevant context — triage by layer
    query2 = "Gaudi 3 dùng process bao nhiêu nm?"
    print("\n" + "=" * 60)
    print("USER PROMPT (case retrieve có thể lệch):", query2)
    print("=" * 60)
    ret2, ans2 = run_rag_query(query2, chunks, vectors, client)
    print("\nRETRIEVED CONTEXT (excerpts):")
    for i, c in enumerate(ret2[:2], 1):
        print(f"  [{i}] {c[:200]}...")
    print("\nFINAL ANSWER:")
    print(ans2)
    print("\n(Nếu retrieve đúng đoạn 'TSMC 5nm' thì answer đúng; nếu không → minh họa triage theo layer.)")


if __name__ == "__main__":
    main()
