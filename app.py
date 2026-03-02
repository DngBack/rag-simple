"""
Web đơn giản để test RAG — hỏi đáp dựa trên tài liệu docs/ (Gaudi 3 PDF).
Chạy: flask --app app run (hoặc python app.py)
"""
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, render_template_string, request

load_dotenv()

# Import sau khi load_dotenv
from llm import chat, get_client, DEFAULT_MODEL
from rag import build_index, retrieve, DEFAULT_PDF

app = Flask(__name__)

# Cache index để không build lại mỗi request
_chunks = None
_vectors = None

SYSTEM_TEMPLATE = """Bạn là trợ lý tư vấn thuế thu nhập cá nhân. Dưới đây là một số đoạn trích từ tài liệu tham khảo:
{context}

Hãy trả lời câu hỏi của người dùng một cách hữu ích."""


def get_index():
    global _chunks, _vectors
    if _chunks is None or _vectors is None:
        _chunks, _vectors = build_index(DEFAULT_PDF)
    return _chunks, _vectors


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template_string(HTML_TEMPLATE, question="", context_sections=[], answer="", error=None)

    question = (request.form.get("question") or request.args.get("q") or "").strip()
    if not question:
        return render_template_string(
            HTML_TEMPLATE, question="", context_sections=[], answer="", error="Vui lòng nhập câu hỏi."
        )

    try:
        chunks, vectors = get_index()
        client = get_client()
        context_list = retrieve(question, chunks, vectors, client=client, top_k=4)
        context_text = "\n\n---\n\n".join(context_list)
        system = SYSTEM_TEMPLATE.format(context=context_text)
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": question},
        ]
        answer, _ = chat(messages, model=DEFAULT_MODEL, temperature=0.3, transcript_dir=None)
        return render_template_string(
            HTML_TEMPLATE,
            question=question,
            context_sections=context_list,
            answer=answer,
            error=None,
        )
    except Exception as e:
        return render_template_string(
            HTML_TEMPLATE,
            question=question,
            context_sections=[],
            answer="",
            error=str(e),
        )


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>RAG Test — Hỏi đáp Luật Thuế TNCN</title>
  <style>
    :root { --bg: #0f0f12; --card: #1a1a1f; --text: #e4e4e7; --muted: #71717a; --accent: #22c55e; --border: #27272a; }
    * { box-sizing: border-box; }
    body { font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); margin: 0; padding: 1.5rem; line-height: 1.6; }
    .container { max-width: 720px; margin: 0 auto; }
    h1 { font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem; color: var(--accent); }
    form { margin-bottom: 1.5rem; }
    label { display: block; font-size: 0.875rem; color: var(--muted); margin-bottom: 0.35rem; }
    input[type="text"], textarea { width: 100%; padding: 0.6rem 0.75rem; background: var(--card); border: 1px solid var(--border); border-radius: 6px; color: var(--text); font-size: 1rem; }
    textarea { min-height: 80px; resize: vertical; }
    button { margin-top: 0.5rem; padding: 0.5rem 1rem; background: var(--accent); color: var(--bg); border: none; border-radius: 6px; font-weight: 500; cursor: pointer; }
    button:hover { opacity: 0.9; }
    .error { background: #451a1a; color: #fca5a5; padding: 0.75rem; border-radius: 6px; margin-bottom: 1rem; }
    .block { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 1rem; margin-bottom: 1rem; }
    .block h2 { font-size: 0.875rem; font-weight: 600; color: var(--muted); margin: 0 0 0.5rem 0; text-transform: uppercase; letter-spacing: 0.05em; }
    .block pre, .block p { margin: 0; font-size: 0.9rem; white-space: pre-wrap; word-break: break-word; }
    .context-excerpt { font-size: 0.8rem; color: var(--muted); border-left: 3px solid var(--border); padding-left: 0.75rem; margin-bottom: 0.5rem; }
  </style>
</head>
<body>
  <div class="container">
    <h1>RAG Test — Hỏi đáp Luật Thuế TNCN</h1>
    <form method="post" action="/">
      <label for="question">Câu hỏi</label>
      <textarea id="question" name="question" placeholder="Ví dụ: Mức giảm trừ gia cảnh cho bản thân là bao nhiêu?">{{ question }}</textarea>
      <button type="submit">Gửi</button>
    </form>
    {% if error %}
    <div class="error">{{ error }}</div>
    {% endif %}
    {% if question and not error %}
    <div class="block">
      <h2>Retrieved context</h2>
      {% for s in context_sections %}
      <div class="context-excerpt">{{ s[:400] }}{% if s|length > 400 %}…{% endif %}</div>
      {% endfor %}
    </div>
    <div class="block">
      <h2>Trả lời</h2>
      <p>{{ answer }}</p>
    </div>
    {% endif %}
  </div>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
