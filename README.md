# rag-simple
Simple RAG for test (tài liệu: docs/ Gaudi 3 PDF). Demo kit cho buổi học test GenAI.

## Cách chạy
1. Tạo venv và cài dependency: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`
2. Copy `.env.example` thành `.env`, điền `OPENAI_API_KEY`.
3. Chạy demo từ repo root:
   - Demo 1 (non-determinism): `python demo1_nondeterminism.py`
   - Demo 2 (prompt sensitivity): `python demo2_prompt_sensitivity.py`
   - Demo 3 (fluent-but-wrong): `python demo3_fluent_but_wrong.py`
   - Demo 4 (RAG pipeline): `python demo4_rag_pipeline.py`
4. Transcript tự ghi vào `demo-kit/transcripts/`. Backup và run sheet: xem folder `demo-kit/`.
