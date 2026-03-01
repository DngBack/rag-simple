# Checklist chung cho mọi demo (bắt buộc)

## A. Mục tiêu & takeaway
- [ ] **1 câu mục tiêu** demo (học viên nhìn xong phải “ngộ” điều gì)
- [ ] **1 câu takeaway** chốt để bạn nói ngay sau demo (≤ 10 giây)
- [ ] **2 câu hỏi gài** để học viên trả lời (pass/fail? lỗi gì?)

## B. Môi trường chạy (để không “toang” trên lớp)
- [ ] Chọn 1 nền chạy: **ChatGPT UI / Playground / tool nội bộ** (tool nội bộ = script Python trong repo: `demo1_nondeterminism.py`, `demo2_prompt_sensitivity.py`, `demo3_fluent_but_wrong.py`, `demo4_rag_pipeline.py`)
- [ ] Chuẩn bị backup: **ảnh chụp màn hình + transcript** (phòng khi mạng/latency)
- [ ] Log tối thiểu: **model name, temperature, top_p, seed (nếu có), ngày giờ** (script ghi vào `demo-kit/transcripts/`)
- [ ] Quy tắc: **không sửa tay output** khi demo (trừ khi dùng screenshot backup)

## C. Tài sản demo (assets)
- [ ] **1 file “Demo Script” (1 trang)** cho từng demo: prompt chính + biến thể, cấu hình (temp/top_p/...), số lần chạy, dự kiến output “điển hình” + output “lỗi” (từ backup)
- [ ] **Slide 1 trang** cho mỗi demo: “Setup → Observe → Interpret” (xem `slides_demo_pages.md`)

## D. Quản trị lớp (để demo thành học)
- [ ] Thời lượng demo: **3–5 phút/demo**
- [ ] Điểm dừng **“pause”**: cho lớp vote (hands-up/poll) trước khi bạn giải thích
- [ ] Liên kết với taxonomy: bạn phải nói rõ demo này “đánh” **lỗi nào** (non-determinism / prompt sensitivity / fluent-but-wrong / pipeline layer)
