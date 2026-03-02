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

SYSTEM_PROMPT = """Bạn là trợ lý tư vấn thuế thu nhập cá nhân. Dưới đây là một số đoạn trích từ tài liệu:
{context}

Hãy trả lời câu hỏi dưới đây."""


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
    print("Loading PDF (Luật Thuế TNCN) and building index...")
    chunks, vectors = build_index(DEFAULT_PDF)
    client = get_client()
    transcript_dir = TRANSCRIPT_DIR
    transcript_dir.mkdir(parents=True, exist_ok=True)

    # Case 1: query that should retrieve correct context
    query1 = "Biểu thuế lũy tiến từng phần áp dụng cho thu nhập từ tiền lương, tiền công gồm những bậc nào?"
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
    query2 = "Tôi làm freelance và có thu nhập 50 triệu/tháng, tôi cần nộp thuế bao nhiêu?"
    print("\n" + "=" * 60)
    print("USER PROMPT (case retrieve có thể lệch):", query2)
    print("=" * 60)
    ret2, ans2 = run_rag_query(query2, chunks, vectors, client)
    print("\nRETRIEVED CONTEXT (excerpts):")
    for i, c in enumerate(ret2[:2], 1):
        print(f"  [{i}] {c[:200]}...")
    print("\nFINAL ANSWER:")
    print(ans2)
    print("\n(Nếu retrieve đúng điều khoản giảm trừ & biểu thuế thì answer đúng; nếu không → minh họa triage theo layer. Prompt lỏng nên model dễ tự bịa số liệu — đây là lỗ hổng cần tester khai thác.)")


if __name__ == "__main__":
    main()
