# Demo 1 — Non-determinism: Sample outputs

**Prompt:** Giải thích RAG là gì trong 3 câu, tiếng Việt, cho người mới học.  
**Cấu hình:** temperature 0.7, cùng prompt chạy 3 lần.

---

## Sample A (PASS — đúng, khác wording)

RAG là kỹ thuật kết hợp bước “tìm kiếm” tài liệu với bước “sinh câu trả lời”. Hệ thống trước khi trả lời sẽ truy vấn cơ sở dữ liệu (ví dụ tài liệu nội bộ) để lấy đoạn văn liên quan. Mô hình ngôn ngữ dùng đúng những đoạn đó để viết câu trả lời, nên giảm bịa đặt và bám nguồn.

---

## Sample B (PASS — đúng, khác cách diễn đạt)

Retrieval-Augmented Generation (RAG) gồm hai bước: retrieval (lấy tài liệu liên quan từ kho) và generation (sinh câu trả lời dựa trên tài liệu đó). Nhờ vậy câu trả lời dựa trên nguồn có sẵn thay vì chỉ dựa vào kiến thức có sẵn trong mô hình. RAG không cần fine-tune lại mô hình, chỉ cần có kho tài liệu và bước truy vấn.

---

## Sample C (FAIL — nghe hay nhưng sai)

RAG là phương pháp fine-tune mô hình ngôn ngữ trên từng bộ tài liệu riêng để nó “nhớ” nội dung và trả lời chính xác hơn. Người ta thường dùng câu hỏi–đáp từ tài liệu để huấn luyện thêm, giúp mô hình vừa giữ kiến thức nền vừa bám sát tài liệu nội bộ. Kết quả là hệ thống trả lời mượt và đúng với từng kho tài liệu.

**Lỗi:** Nói RAG = fine-tune (sai). RAG = retrieval + generation, không train lại model.

---

**Câu hỏi gài:** A vs B, cái nào pass? Có cần giống y nhau không? → Cả A và B đều pass; không cần giống nhau. C → fail (sai định nghĩa).
