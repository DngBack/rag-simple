"""
OpenAI client with configurable params and logging for demo kit.
Logs: model, temperature, top_p, seed (if any), timestamp.
"""
import os
import json
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Defaults for demos
DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_TOP_P = 1.0


def get_client() -> OpenAI:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY not set. Copy .env.example to .env and set your key.")
    return OpenAI(api_key=key)


def chat(
    messages: list[dict],
    *,
    model: str = DEFAULT_MODEL,
    temperature: float = DEFAULT_TEMPERATURE,
    top_p: float = DEFAULT_TOP_P,
    seed: int | None = None,
    transcript_dir: Path | None = None,
) -> tuple[str, dict]:
    """
    Call OpenAI Chat Completions. Returns (content, run_log).
    run_log has: model, temperature, top_p, seed, timestamp, prompt, response.
    """
    client = get_client()
    opts = {
        "model": model,
        "temperature": temperature,
        "top_p": top_p,
        "messages": messages,
    }
    if seed is not None:
        opts["seed"] = seed

    ts = datetime.utcnow().isoformat() + "Z"
    resp = client.chat.completions.create(**opts)
    content = resp.choices[0].message.content or ""

    run_log = {
        "model": model,
        "temperature": temperature,
        "top_p": top_p,
        "seed": seed,
        "timestamp": ts,
        "prompt": messages,
        "response": content,
    }

    if transcript_dir:
        transcript_dir = Path(transcript_dir)
        transcript_dir.mkdir(parents=True, exist_ok=True)
        safe_ts = ts.replace(":", "-").replace(".", "-")
        path = transcript_dir / f"run_{safe_ts}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(run_log, f, ensure_ascii=False, indent=2)
        print(f"  [log] {path}")

    return content, run_log
