# Slides demo — 1 trang / demo (Setup → Observe → Interpret)

Có thể copy nội dung vào PowerPoint/Google Slides; mỗi demo 1 slide.

---

## Demo 1 — Non-determinism
- **Setup**: Cùng prompt "Giải thích RAG là gì trong 3 câu, tiếng Việt.", temp 0.7. Chạy 3 lần.
- **Observe**: Ba output khác nhau (hoặc chiếu 2 transcript backup).
- **Interpret**: Pass/fail? Có cần giống y nhau không? → GenAI test = acceptable range, không exact match.

---

## Demo 2 — Prompt sensitivity
- **Setup**: Cùng đoạn văn (input_demo2_paragraph.txt). P1: "Tóm tắt trong 2 câu." P3: "... 2 câu và 3 gạch đầu dòng."
- **Observe**: P1 vs P3 — format và độ tuân thủ khác nhau.
- **Interpret**: Vì sao QA phải test nhiều biến thể prompt? → Robustness theo paraphrase/constraint là trục test riêng.

---

## Demo 3 — Fluent-but-wrong
- **Setup**: Chiếu 1 output (ẩn nhãn đúng/sai). Ưu tiên backup "mượt nhưng sai".
- **Observe**: Lớp vote pass hay fail; nêu lý do.
- **Interpret**: Sai trục nào (Correctness / Groundedness)? → Chấm theo evidence & rubric, không theo văn phong.

---

## Demo 4 — Pipeline RAG (optional)
- **Setup**: User prompt → Retrieved context (từ docs PDF) → Final answer.
- **Observe**: (Optional) Case retrieve sai → answer sai.
- **Interpret**: Triage theo layer: lỗi retrieval hay lỗi LLM?
