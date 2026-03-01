# Demo 2 — Prompt sensitivity

## Mục tiêu
Đổi wording nhỏ → hành vi đổi lớn; QA cần test nhiều biến thể prompt; robustness theo paraphrase/constraint là trục test riêng.

## Takeaway
"Robustness theo paraphrase/constraint là trục test riêng."

---

## Prompt set (3)

| Id | Nội dung |
|----|----------|
| **P1 (base)** | Tóm tắt đoạn sau trong 2 câu. |
| **P2 (constraint nhẹ)** | Tóm tắt đoạn sau trong 2 câu, cho người mới, không thuật ngữ. |
| **P3 (constraint dễ fail)** | Tóm tắt đoạn sau trong 2 câu và liệt kê 3 gạch đầu dòng. |

## Input
File: `demo-kit/input_demo2_paragraph.txt` — đoạn 5–7 câu, 2–3 ý rõ (chính sách hoàn tiền, làm việc từ xa, nghỉ phép).

## Cấu hình
- temperature ≈ 0.5 (để thấy “lúc tuân thủ, lúc lạc”).
- Chạy lần lượt P1, P2, P3 với cùng đoạn văn.

---

## Checklist pass/fail từng prompt

**P1**
- [ ] Đúng nội dung
- [ ] Đúng 2 câu

**P2**
- [ ] Đúng nội dung
- [ ] Không thuật ngữ
- [ ] Dễ hiểu

**P3**
- [ ] Đúng nội dung
- [ ] Đúng 2 câu
- [ ] Có 3 bullet (format gạch đầu dòng)

## Backup
Chuẩn bị 1 output fail instruction rõ ràng (không bullet, viết dài) — lưu trong `transcripts/` hoặc `backup_screenshots/`.

---

## Chạy
- Tool: `python demo2_prompt_sensitivity.py` (từ repo root).
- Backup: transcript mỗi lần trong `demo-kit/transcripts/`.

## Câu hỏi gài
1. Cùng nội dung, vì sao QA phải test nhiều biến thể prompt?
2. P3 yêu cầu “2 câu + 3 bullet” — nếu model chỉ trả lời 2 câu không bullet, fail trục nào?

---

## Script lớp
1. Mở input_demo2_paragraph.txt, copy đoạn văn.
2. P1: "Tóm tắt đoạn sau trong 2 câu." + [dán]. Chạy.
3. P3: "... trong 2 câu và liệt kê 3 gạch đầu dòng." + [dán]. Chạy.
4. **PAUSE**: "Cùng nội dung, vì sao QA phải test nhiều biến thể prompt?"
5. Chốt takeaway.
