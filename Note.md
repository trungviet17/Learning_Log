## Model 
- Model chỉ cách Django làm việc với dữ liệu được lưu trong app.  Bao gồm các trường và hành vi của dữ liệu 
- Kích hoạt model : 
    - Chỉnh sửa file model.py -> Thêm class chứa attribute dữ liệu + hành vi của nó
    - Gọi lệnh makmigrations trên tên dự án -> Django tìm cách sử db cho việc lưu dữ liệu liên quan -> tạo ra model vừa sửa trong db 
    - Lệnh migrate -> chấp nhận chính sửa

## Admin site 
### Superuser 
- Người dùng có tất cả quyền trên trang (admin)

## Making web page 
- Bao gồm 3 stage : 
    1. Định nghĩa URL : what to look for when matching a browser request with as site URL 
    2. Writing view : URL map to a particular view, view function retrieves and process the data needed for that page 
    3. writing template : view function often render the page using a template 


## Thiết kế webpage 
- Thiết kế theo dạng kế thừa từ file base.html 

## GET / POST request 
- GET request : cho việc hiện thị dữ liệu từ server 
- POST request : sử dụng khi người dùng muốn submit thông tin qua form 

## Login / Logout 
- Sử dụng module django.contrib.auth với các hàm login, logout được build sẵn, có sẵn các template
- Có sẵn đối tượng user 

##  Decorator 
@login_required : Hàm decorator này kiểm tra xem người dùng đã đăng nhập hay chưa