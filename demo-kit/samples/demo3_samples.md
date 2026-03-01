# Demo 3 — Fluent-but-wrong: Sample outputs

Chiếu **ẩn nhãn** trước, cho lớp vote pass/fail và nêu lý do theo rubric (Correctness / Groundedness).

---

## Câu hỏi: "RAG có phải fine-tune không? Giải thích ngắn gọn."

---

### Output 1 (Ẩn nhãn khi chiếu — đây là **FAIL: mượt nhưng sai**)

RAG thực chất là một dạng fine-tune đặc biệt: người ta fine-tune mô hình ngôn ngữ trên từng bộ tài liệu riêng để nó "nhớ" nội dung đó và trả lời chính xác hơn. Nhờ vậy mô hình vừa giữ được kiến thức nền vừa bám sát tài liệu nội bộ. Cách làm này tiết kiệm hơn so với fine-tune toàn bộ vì chỉ cần train trên kho tài liệu của từng đơn vị.

**Sai ở đâu:** RAG **không** phải fine-tune. RAG = retrieval (truy vấn tài liệu) + generation (sinh câu trả lời từ tài liệu lấy được). Không có bước train/fine-tune mô hình trên tài liệu. → Fail **Correctness** (và Groundedness nếu coi “định nghĩa đúng” là nguồn).

---

### Output 2 (Ẩn nhãn khi chiếu — đây là **PASS: ngắn nhưng đúng**)

Không. RAG là retrieval (lấy tài liệu liên quan) + generation (sinh câu trả lời từ tài liệu đó). Không có bước fine-tune; mô hình dùng nguyên, chỉ thêm bước truy vấn và đưa kết quả vào prompt.

**Đúng:** Khái niệm chuẩn; ngắn, đủ ý.

---

**Chốt:** QA GenAI chấm theo evidence & rubric, không theo văn phong. Output 1 mượt nhưng sai; Output 2 ít câu nhưng đúng.

---

## Câu hỏi phụ: "Phân biệt groundedness và correctness."

### Output mượt nhưng sai (backup)

Groundedness là mức độ đúng với sự thật bên ngoài (facts). Correctness là mức độ bám sát nguồn tài liệu đã cung cấp. Một câu trả lời có thể correctness cao (bám nguồn) nhưng groundedness thấp nếu nguồn đó sai.

**Sai:** Đảo định nghĩa. Thường: **groundedness** = bám nguồn / không bịa; **correctness** = đúng sự thật / đúng đáp án. (Một số taxonomy dùng gần nhau, nhưng “đảo” rõ ràng thì fail.)
