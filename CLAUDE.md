# CLAUDE.md

## Quyền truy cập mạng

Khi một trang web hoặc tên miền không truy cập được (lỗi DNS, proxy từ chối, 403/407...):

- Đừng chỉ báo "bị chặn" rồi dừng lại.
- Hỏi người dùng có muốn cho phép truy cập tên miền đó không, và gửi luôn yêu cầu duyệt (dùng `update_environment` để thêm tên miền vào danh sách cho phép).
- Sau khi được duyệt, thử lại ngay.
