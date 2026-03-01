#!/usr/bin/env python3
"""
Demo 2 — Prompt sensitivity: small wording change, big behavior change.
Reads input from demo-kit/input_demo2_paragraph.txt, runs P1/P2/P3, logs to demo-kit/transcripts/.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from llm import chat, DEFAULT_MODEL

INPUT_FILE = Path(__file__).resolve().parent / "demo-kit" / "input_demo2_paragraph.txt"
TRANSCRIPT_DIR = Path(__file__).resolve().parent / "demo-kit" / "transcripts"

P1 = "Tóm tắt đoạn sau trong 2 câu."
P2 = "Tóm tắt đoạn sau trong 2 câu, cho người mới, không thuật ngữ."
P3 = "Tóm tắt đoạn sau trong 2 câu và liệt kê 3 gạch đầu dòng."


def main():
    if not INPUT_FILE.exists():
        print(f"Missing {INPUT_FILE}")
        return
    text = INPUT_FILE.read_text(encoding="utf-8").strip()
    transcript_dir = TRANSCRIPT_DIR
    transcript_dir.mkdir(parents=True, exist_ok=True)

    prompts = [
        ("P1 (base)", P1),
        ("P2 (constraint nhẹ)", P2),
        ("P3 (constraint dễ fail)", P3),
    ]
    print("Demo 2 — Prompt sensitivity")
    print("Input (first 200 chars):", text[:200] + "..." if len(text) > 200 else text)
    print("Config: model=%s, temperature=0.5\n" % DEFAULT_MODEL)

    for name, prompt_template in prompts:
        user_content = prompt_template + "\n\n" + text
        print(f"--- {name} ---")
        content, _ = chat(
            [{"role": "user", "content": user_content}],
            model=DEFAULT_MODEL,
            temperature=0.5,
            top_p=1.0,
            transcript_dir=transcript_dir,
        )
        print(content)
        print()


if __name__ == "__main__":
    main()
