# Demo 4 — Pipeline RAG (optional)

## Mục tiêu
Minh họa pipeline nhiều lớp: user prompt → retrieved context → final answer; triage theo layer khi retrieve sai hoặc tool omit.

## Takeaway
Khi lỗi xảy ra, cần xác định layer: retrieval sai hay LLM bỏ qua context?

---

## Flow
1. **User prompt** → 2. **Retrieved context** (từ docs/ PDF) → 3. **Final answer**

## Tài liệu
- `docs/gaudi-3-ai-accelerator-white-paper.pdf` (Intel Gaudi 3)

## Câu hỏi mẫu (RAG đúng)
- "Intel Gaudi 3 có bao nhiêu HBM memory và bandwidth? Nêu ngắn gọn số liệu."
- Dự kiến: 128 GB HBM, 3.7 TB/s (từ whitepaper).

## Case “retrieve sai” hoặc lệch
- "Gaudi 3 dùng process bao nhiêu nm?"
- Đáp án đúng trong tài liệu: TSMC 5nm. Nếu retrieved không chứa đoạn đó → answer sai → minh họa triage: lỗi ở layer retrieval.

---

## Chạy
- Tool: `python demo4_rag_pipeline.py` (từ repo root). Cần `OPENAI_API_KEY`.
- In ra: User prompt → Retrieved context (excerpts) → Final answer (2 cases).

## Trên lớp
- Chiếu: User prompt → Retrieved context → Final answer.
- (Hoặc slide + log giả nếu không chạy RAG thật.)

## Script lớp
1. Chiếu 3 thứ: user prompt → retrieved context → final answer.
2. (Optional) Case retrieve sai → minh họa triage theo layer.
