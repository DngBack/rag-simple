# Demo 3 — Fluent-but-wrong

## Mục tiêu
Mượt ≠ đúng. QA GenAI không được chấm theo văn phong; phải chấm theo evidence & rubric.

## Takeaway
"Chấm theo evidence & rubric, không theo văn phong."

---

## Câu hỏi “đánh lừa”
Chọn 1 (hoặc cả 2 tùy thời gian):
- "Phân biệt groundedness và correctness."
- "RAG có phải fine-tune không?"

## Hai output cần chuẩn bị

| Loại | Mô tả |
|------|--------|
| **Mượt nhưng sai** | Đảo định nghĩa, bịa cơ chế, văn hay nhưng nội dung sai. |
| **Ngắn nhưng đúng** | Chuẩn khái niệm, ít câu nhưng đúng. |

## Cách trình bày
1. Ẩn nhãn đúng/sai ban đầu.
2. Chiếu 1 output (ưu tiên backup “mượt nhưng sai” nếu đã có).
3. **PAUSE**: "Output này pass hay fail? Lý do? Sai trục nào?"
4. Bắt buộc lớp nêu lý do theo rubric: Correctness vs Groundedness.

## Backup bắt buộc
- Screenshot/transcript “mượt nhưng sai” trong `backup_screenshots/` hoặc `transcripts/`.
- Nếu live model không ra sai: dùng backup luôn (đừng cố chạy đến khi sai).

---

## Rubric 5 trục (nhắc khi tranh cãi)
- Correctness (đúng sự thật)
- Groundedness (bám nguồn / không bịa)
- Instruction adherence (tuân thủ yêu cầu)
- Coherence / fluency (mạch lạc, trôi chảy)
- Safety / appropriateness

---

## Chạy
- Script: `python demo3_fluent_but_wrong.py` — có thể sinh 1–2 output mẫu để lưu backup.
- Trên lớp: ưu tiên chiếu backup đã chuẩn bị.
