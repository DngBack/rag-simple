#!/usr/bin/env python3
"""
Demo 3 — Fluent-but-wrong: generate sample outputs for backup.
Use backups on stage if live model doesn't produce a "smooth but wrong" answer.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from llm import chat, DEFAULT_MODEL

TRANSCRIPT_DIR = Path(__file__).resolve().parent / "demo-kit" / "transcripts"

QUESTIONS = [
    "Mức giảm trừ gia cảnh cho bản thân người nộp thuế là bao nhiêu triệu đồng mỗi tháng?",
    "Thuế suất thuế TNCN đối với thu nhập từ tiền lương là bao nhiêu phần trăm?",
    "Người nước ngoài làm việc tại Việt Nam có phải nộp thuế TNCN không, và điều kiện là gì?",
]


def main():
    transcript_dir = TRANSCRIPT_DIR
    transcript_dir.mkdir(parents=True, exist_ok=True)

    print("Demo 3 — Fluent-but-wrong (Luật Thuế TNCN — generate backup outputs)")
    print("Config: model=%s, temperature=0.7\n" % DEFAULT_MODEL)

    for i, q in enumerate(QUESTIONS, 1):
        print(f"--- Q{i}: {q[:60]}... ---")
        content, _ = chat(
            [{"role": "user", "content": q}],
            model=DEFAULT_MODEL,
            temperature=0.7,
            transcript_dir=transcript_dir,
        )
        print(content)
        print()

    print("Lưu output 'mượt nhưng sai' (số liệu thuế không chính xác, điều khoản bịa đặt, v.v.) vào demo-kit/transcripts/ hoặc backup_screenshots/ để dùng trên lớp.")


if __name__ == "__main__":
    main()
