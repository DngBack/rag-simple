# Demo 1 — Non-determinism

## Mục tiêu
Học viên “ngộ”: cùng prompt, nhiều output đều hợp lệ; test GenAI = acceptable range, không phải exact match.

## Takeaway (chốt ≤10 giây)
"GenAI test = acceptable range, không phải exact match."

---

## Prompt chuẩn
```
Giải thích RAG là gì trong 3 câu, tiếng Việt, cho người mới học.
```

## Cấu hình
| Lần chạy | temperature | top_p | Ghi chú |
|----------|-------------|-------|--------|
| 3 lần chính | 0.7–1.0 | 1.0 | Để thấy variance |
| So sánh | 0–0.2 | 1.0 | Ổn định hơn |

## Rubric mini (pass/fail)
- [ ] Đúng định nghĩa cơ bản (RAG = retrieval + generation)
- [ ] Đúng 3 câu
- [ ] Không bịa cơ chế (không nói fine-tune)
- [ ] Dễ hiểu

---

## Chạy
- Số lần: 3 (cùng config) + 1 optional (temp 0.2).
- Tool: `python demo1_nondeterminism.py` (từ repo root).
- Backup: transcript trong `demo-kit/transcripts/`; copy 2 transcript “đúng” + 1 “nghe hay nhưng sai” vào đây hoặc `backup_screenshots/`.

## Dự kiến output
- **Điển hình**: 3 câu, đúng nghĩa RAG, không fine-tune.
- **Lỗi (backup)**: nghe hay nhưng đảo định nghĩa hoặc gộp với fine-tune.

---

## Câu hỏi gài (cho lớp)
1. A vs B (hai output khác nhau), cái nào pass? Có cần giống y nhau không?
2. Nếu một lần ra 4 câu thay vì 3, pass hay fail theo rubric?

---

## Script lớp
1. Paste prompt, cấu hình temp 0.7. Chạy 3 lần (hoặc chiếu 2 transcript backup).
2. **PAUSE**: "A vs B, cái nào pass? Có cần giống y nhau không?"
3. Chốt takeaway trên.
