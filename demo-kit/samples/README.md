# Samples cho từng demo

Các file trong folder này là **output mẫu** để chiếu khi dạy hoặc dùng backup khi live không chạy.

**Markdown (đọc / copy vào slide):**
- `demo1_samples.md` — Non-determinism: 2 output đúng + 1 nghe hay nhưng sai
- `demo2_samples.md` — Prompt sensitivity: P1, P2, P3 điển hình + 1 output fail (P3)
- `demo3_samples.md` — Fluent-but-wrong: mượt-sai vs ngắn-đúng
- `demo4_samples.md` — Pipeline RAG: log prompt → context → answer (case đúng + case retrieve sai)

**CSV (import Excel / script / phân tích):**
- `demo1_samples.csv` — cột: demo, prompt, sample_id, pass_fail, output, note
- `demo2_samples.csv` — cột: demo, prompt_id, prompt_text, pass_fail, output, note
- `demo3_samples.csv` — cột: demo, question, output_id, pass_fail, output, note
- `demo4_samples.csv` — cột: demo, case_id, retrieve_ok, user_prompt, retrieved_context, final_answer, conclusion
- **`all_samples.csv`** — tổng hợp: gộp tất cả sample, cột chung: demo, row_id, pass_fail, input_prompt, output, note

**Tổng hợp (1 trang):**
- **`tong_hop.md`** — bảng tổng hợp 4 demo (mục tiêu, takeaway, số sample, file), taxonomy lỗi, câu hỏi gài, và link file.

Có thể copy nội dung vào slide hoặc mở file khi trình bày; CSV dùng cho Excel hoặc code.
