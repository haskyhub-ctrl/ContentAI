# Hướng dẫn làm video gym mannequin AI chuyên nghiệp (từng bước)

Dựa trên quy trình của @magsimich (prompt gốc: `prompts-goc.md`), bổ sung phần dựng, lồng tiếng Việt, kiểm tra chất lượng và đăng kênh.
60 bài tập kèm prompt sẵn nằm trong `prompts/` và `exercises.csv` (chạy lại `python3 build_prompts.py` nếu sửa danh sách).

> Giá, hạn mức miễn phí và giao diện của Gemini / Google Flow / CapCut thay đổi thường xuyên. Hãy kiểm tra lại trước khi bắt đầu.

---

## 0. Chuẩn bị công cụ

| Việc | Công cụ gợi ý | Ghi chú |
|---|---|---|
| Tạo ảnh | Gemini hoặc ChatGPT | Cần tải ảnh tham chiếu lên mỗi lần |
| Tạo video | Google Flow (Veo) | Tốn credit; làm theo lô để tiết kiệm |
| Lồng tiếng Việt | ElevenLabs, FPT.AI, Google TTS | Chọn giọng nam trầm, nghe thử trước |
| Dựng video | CapCut (hoặc DaVinci Resolve) | Xuất 1080×1920 |
| Thumbnail | Canva | Dùng chung một mẫu cho cả kênh |
| Nhạc | Thư viện nhạc có bản quyền cho phép (YouTube Audio Library, CapCut thư viện thương mại) | Không dùng nhạc trending nếu không rõ bản quyền |

Tạo sẵn thư mục:
```
kenh-gym/
  00-nhan-vat/        ảnh mannequin gốc
  01-anh-tu-the/      ảnh theo bài tập
  02-clip/            clip từ Flow
  03-giong/           file giọng đọc
  04-xuat/            video hoàn chỉnh
```

## 1. Khóa nhân vật (làm một lần, quan trọng nhất)

1. Mở `prompts-goc.md`, dùng prompt số 1 để tạo nhân vật.
2. Tạo 6–8 ảnh, chọn **một** ảnh đẹp nhất: tỉ lệ cơ thể đẹp, mặt trơn không có chi tiết, quần đen sạch, nền tối đúng phong cách.
3. Lưu thành `00-nhan-vat/mannequin-goc.png`. Từ đây mọi ảnh phải tham chiếu ảnh này.
4. Chốt phong cách của kênh và **không đổi nữa**: nền trắng–đen, cơ phát sáng đỏ neon. Sự nhất quán là thứ làm kênh trông chuyên nghiệp.

## 2. Làm ảnh tư thế cho từng bài

1. Mở file trong `prompts/`, ví dụ `01-barbell-bench-press...md`.
2. Trong Gemini/ChatGPT: **tải ảnh `mannequin-goc.png`** rồi dán prompt "Bước 1".
3. Kiểm tra ảnh bằng danh sách này, thiếu một mục thì tạo lại:
   - [ ] Đúng bài tập, đúng dụng cụ (thanh tạ nằm trên tay, không xuyên qua người).
   - [ ] Đủ 2 tay 2 chân, 5 ngón, không biến dạng.
   - [ ] Tư thế đúng kỹ thuật: lưng, gối, khuỷu ở vị trí an toàn. Đối chiếu với nguồn uy tín (huấn luyện viên, ACE/NSCA, ExRx).
   - [ ] Nhóm cơ mục tiêu phát sáng đúng chỗ, không phát sáng toàn thân.
   - [ ] Nhân vật giống ảnh gốc.
4. Lưu vào `01-anh-tu-the/` theo tên `01-bench-press.png`.

Mẹo: nếu AI vẽ sai dụng cụ, thêm vào prompt mô tả cụ thể, ví dụ "a flat bench, an Olympic barbell held with an overhand grip, the lifter lying on the bench".

## 3. Tạo chuyển động trong Google Flow

1. Tải ảnh tư thế lên Flow (chế độ image-to-video, 9:16).
2. Dán prompt "Clip 1" trong file bài tập. Mỗi bài có 3 prompt khác nhau về góc máy: cạnh bên, chéo trước, cận cảnh cơ.
3. Tạo mỗi clip khoảng 8–10 giây. Xem mỗi clip và loại bỏ nếu:
   - Nhân vật biến dạng, tạ xuyên người, chuyển động sai chiều.
   - Phòng tập thay đổi giữa chừng.
   - Số lần lặp quá nhanh hoặc giật.
4. Nếu hỏng: tạo lại 2–3 lần. Nếu vẫn lỗi, đơn giản hóa prompt (bỏ chi tiết thừa) hoặc đổi ảnh tư thế ban đầu.
5. Lưu clip tốt vào `02-clip/` theo tên `01-bench-a.mp4`, `01-bench-b.mp4`, `01-bench-c.mp4`.

Tiết kiệm credit: làm theo lô (cả nhóm ngực một buổi), chỉ tạo video cho ảnh đã được kiểm tra.

## 4. Lồng tiếng

1. Lấy lời thoại ở "Bước 3" trong file bài tập (hoặc cột `loi_thoai_vn` trong `exercises.csv`).
2. Đọc lại bằng tai: câu có tự nhiên không? Sửa nếu đọc vấp. Giữ ngắn, mỗi video chỉ **một** cue chính.
3. Tạo giọng đọc: giọng nam trầm, tự tin, tốc độ khoảng 1.05–1.15.
4. Xuất `.mp3` hoặc `.wav` vào `03-giong/`.

Mẹo: ghi cả tên cơ bằng tiếng Anh trong phụ đề (ví dụ "Latissimus dorsi") để người xem có thể tìm kiếm thêm.

## 5. Dựng video trong CapCut

Mục tiêu: video 25–35 giây, 1080×1920, 30fps.

Cấu trúc đề xuất:

| Giây | Nội dung |
|---|---|
| 0–2 | **Hook**: chữ lớn "Tập ngực mà không cảm thấy gì?" hoặc "Sai lầm khi tập xô" cùng clip cận cảnh cơ phát sáng |
| 2–10 | Clip góc cạnh bên, giọng đọc nêu tên bài và cơ |
| 10–20 | Clip chéo trước, giọng đọc nêu cue kỹ thuật, chữ nổi bật |
| 20–28 | Clip cận cảnh cơ co giãn |
| 28–32 | CTA: "Lưu lại để tập" + logo kênh |

Các bước:
1. Tạo dự án 9:16, 1080×1920, 30fps.
2. Kéo 3 clip vào timeline, cắt bỏ giây đầu cuối bị lỗi. Chuyển cảnh chỉ dùng cắt thẳng hoặc dissolve ngắn 0.2s; tránh hiệu ứng lòe loẹt.
3. Thêm giọng đọc, chỉnh âm lượng giọng khoảng −6 dB, nhạc nền −22 đến −18 dB.
4. Thêm phụ đề tự động rồi sửa lại cho đúng. Cỡ chữ lớn, nằm trong vùng an toàn (cách mép dưới khoảng 250px để không bị nút giao diện che).
5. Dùng **một** font và **một** màu nhấn (đỏ neon) cho toàn kênh. Tên cơ hiện bằng màu đỏ khi được nhắc tới.
6. Thêm âm thanh nhẹ (tiếng "whoosh" khi hook, tiếng thở hoặc tạ) để video sống động hơn.
7. Điều chỉnh màu: tăng tương phản nhẹ, giữ đen sâu, tránh làm cháy vùng trắng của mannequin.
8. Nâng chất lượng (upscale/enhance) nếu clip gốc là 720p.
9. Xuất: 1080×1920, 30fps, bitrate cao, H.264, MP4. Lưu vào `04-xuat/`.

## 6. Làm cho kênh trông chuyên nghiệp

- **Nhận diện cố định**: logo 1 giây ở đầu hoặc góc, cùng font, cùng bảng màu.
- **Series theo nhóm cơ**: "Ngực — 8 bài", "Lưng — 10 bài". Đặt tên video dạng `[Nhóm cơ] | [Bài tập] | [lỗi thường gặp]`.
- **Thêm giá trị riêng**: đây là phần quan trọng nhất. Thêm một cue kỹ thuật, một lỗi sai phổ biến, hoặc cảnh "sai vs đúng" cạnh nhau. Nội dung AI hàng loạt không có giá trị riêng dễ bị nền tảng đánh giá là spam và khó kiếm tiền.
- **Video dài trên YouTube**: ghép 5–8 bài cùng nhóm cơ thành video 3–5 phút, có chương.
- **Thumbnail**: mannequin to, cơ phát sáng, chữ ngắn 2–3 từ.

## 7. Đăng bài

- **Nền tảng**: TikTok, YouTube Shorts, Instagram Reels, Facebook Reels. Cùng một video nhưng đổi caption cho phù hợp từng nền tảng.
- **Tần suất**: 1 video/ngày trong 30 ngày đầu; sản xuất theo lô (một buổi làm 5–7 bài).
- **Caption**: một câu hook + tên bài tập + hashtag (#gym #tapgym #bodybuilding #fitness #tapnguc…).
- **Gắn nhãn nội dung AI**: TikTok, YouTube, Instagram đều có tùy chọn khai báo nội dung do AI tạo. Nên bật để tránh bị gỡ hoặc hạn chế.
- **Bình luận**: trả lời trong 1 giờ đầu để tăng tương tác.

## 8. Quy trình sản xuất theo lô (cho một tuần, 7 video)

| Ngày | Việc |
|---|---|
| Thứ 2 | Chọn 7 bài (một nhóm cơ), tạo ảnh tư thế, kiểm tra kỹ thuật |
| Thứ 3 | Tạo clip trong Flow (3 clip/bài) |
| Thứ 4 | Viết/sửa lời thoại, tạo giọng đọc |
| Thứ 5–6 | Dựng 7 video, xuất file |
| Thứ 7 | Lên lịch đăng cho cả tuần |
| Chủ nhật | Xem số liệu, ghi lại mẫu video nào tốt |

## 9. Lộ trình 30 ngày

- **Tuần 1**: khóa nhân vật, làm 7 video đầu (bắt đầu từ nhóm Ngực, vì dễ nhận biết).
- **Tuần 2**: thêm series Lưng, thử các kiểu hook khác nhau.
- **Tuần 3**: thêm "sai vs đúng", giữ lại kiểu hook cho kết quả tốt nhất.
- **Tuần 4**: ghép video dài cho YouTube, thử gắn liên kết sản phẩm (dụng cụ, thực phẩm bổ sung) khi đã có người xem.

## 10. Lưu ý quan trọng

- **Độ chính xác**: AI hay vẽ sai kỹ thuật. Kiểm tra từng bài với nguồn uy tín trước khi đăng, vì lời khuyên sai có thể gây chấn thương cho người xem.
- **Thông điệp an toàn**: thêm dòng nhỏ "Chọn mức tạ phù hợp, hỏi huấn luyện viên nếu có chấn thương".
- **Thu nhập**: con số 500–1000$/tháng trong bài gốc chưa được kiểm chứng. Hãy coi đây là mô hình thử nghiệm và theo dõi số liệu thật của kênh.
- **Bản quyền**: chỉ tham khảo ý tưởng từ kênh khác, không dùng lại video, giọng đọc hay nhạc của người khác.
- **Quảng cáo thực phẩm bổ sung**: không khẳng định công dụng chữa bệnh hay hiệu quả giảm cân; tuân thủ quy định quảng cáo ở Việt Nam.
