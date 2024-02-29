## Model 
- Model chỉ cách Django làm việc với dữ liệu được lưu trong app.  Bao gồm các trường và hành vi của dữ liệu 
- Kích hoạt model : 
    - Chỉnh sửa file model.py -> Thêm class chứa attribute dữ liệu + hành vi của nó
    - Gọi lệnh makmigrations trên tên dự án -> Django tìm cách sử db cho việc lưu dữ liệu liên quan -> tạo ra model vừa sửa trong db 
    - Lệnh migrate -> chấp nhận chính sửa

## Admin site 
### Superuser 
- Người dùng có tất cả quyền trên trang