#!/usr/bin/env python3
"""
Demo 1 — Non-determinism: same prompt, multiple valid outputs.
Runs the same prompt 3 times with temp 0.7; optionally once with temp 0.2 for comparison.
Logs to demo-kit/transcripts/.
"""
import sys
from pathlib import Path

# Allow running from repo root
sys.path.insert(0, str(Path(__file__).resolve().parent))
from llm import chat, DEFAULT_MODEL

PROMPT = "Thuế thu nhập cá nhân là gì? Giải thích trong 3 câu, tiếng Việt, cho người mới tìm hiểu."
TRANSCRIPT_DIR = Path(__file__).resolve().parent / "demo-kit" / "transcripts"


def main():
    transcript_dir = TRANSCRIPT_DIR
    transcript_dir.mkdir(parents=True, exist_ok=True)

    print("Demo 1 — Non-determinism (Thuế TNCN)")
    print("Prompt:", PROMPT)
    print("Config: model=%s, temperature=0.7, 3 runs\n" % DEFAULT_MODEL)

    for i in range(1, 4):
        print(f"--- Run {i} ---")
        content, log = chat(
            [{"role": "user", "content": PROMPT}],
            model=DEFAULT_MODEL,
            temperature=0.7,
            top_p=1.0,
            transcript_dir=transcript_dir,
        )
        print(content)
        print()

    print("--- Optional: 1 run with temp=0.2 (more stable) ---")
    content, _ = chat(
        [{"role": "user", "content": PROMPT}],
        model=DEFAULT_MODEL,
        temperature=0.2,
        top_p=1.0,
        transcript_dir=transcript_dir,
    )
    print(content)


if __name__ == "__main__":
    main()
