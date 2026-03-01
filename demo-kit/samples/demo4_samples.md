# Demo 4 — Pipeline RAG: Sample log

Minh họa 3 lớp: **User prompt** → **Retrieved context** → **Final answer**. Khi sai: triage xem lỗi ở retrieval hay ở LLM.

---

## Case 1: Retrieve đúng → Answer đúng

### User prompt
Intel Gaudi 3 có bao nhiêu HBM memory và bandwidth? Nêu ngắn gọn số liệu.

### Retrieved context (excerpts)
- "... The Intel Gaudi 3 AI accelerator features two compute dies, which together contain 8 MME engines, 64 TPC engines and 24x 200 Gbps RDMA NIC ports. In addition, the total of 8 HBM2e chips comprise a **128 GB** unified High Bandwidth Memory (HBM). The Intel Gaudi 3 AI accelerator excels at training and inference with 1.8 PFlops of FP8 and BF16 compute, **128 GB of HBM2e memory capacity, and 3.7 TB/s of HBM bandwidth**."
- "... With 1.5x faster HBM bandwidth and 1.33x larger HBM capacity, the Intel Gaudi 3 AI accelerator provides an order-of-magnitude improvement in large language model inference performance ..."

### Final answer
Intel Gaudi 3 có **128 GB** HBM2e memory và băng thông HBM **3.7 TB/s**.

**Kết luận:** Retrieval lấy đúng đoạn có số liệu → LLM trả lời đúng. Pipeline ổn.

---

## Case 2: Retrieve lệch / thiếu → Answer sai (triage theo layer)

### User prompt
Gaudi 3 dùng process bao nhiêu nm?

### Retrieved context (excerpts — giả sử không chứa câu “TSMC 5nm”)
- "... The Intel Gaudi 3 AI accelerator (Figure 1) features two identical compute dies, connected through a high-bandwidth, low-latency interconnect ..."
- "... BF16 MME TFLOPS 432 vs 1678, HBM Capacity 96 GB vs 128 GB ..."

(Đoạn có "TSMC 5nm" / "7nm process" không nằm trong top-k retrieved.)

### Final answer (sai hoặc mơ hồ)
Tài liệu không nêu rõ process node của Gaudi 3. / Hoặc model đoán sai.

**Kết luận:** Lỗi ở **layer retrieval** — không lấy được đoạn chứa "TSMC 5nm". Cần cải thiện chunking/embedding hoặc query, không phải lỗi LLM bỏ qua context.

---

**Takeaway:** Khi đáp án sai, cần xác định: retrieval có lấy đúng đoạn không? Nếu context không có thông tin → triage retrieval; nếu context có mà answer vẫn sai → xem layer LLM.
