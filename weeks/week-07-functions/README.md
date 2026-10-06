# 🧩 Tuần 07: Hàm & Phân Tách Logic (Functions & Decomposition)

Luyện tập thiết kế hàm (Functions), quản lý tham số, phạm vi biến (Scope) và tư duy phân tách bài toán lớn thành các mô-đun nhỏ (Decomposition).

---

## 🎯 Mục Tiêu Học Tập
- Chuyển đổi từ viết script tuyến tính sang cấu trúc hàm tái sử dụng với `return`.
- Hiểu rõ tham số mặc định (Default Parameters) và khai báo Type Hints.
- Kiểm soát phạm vi biến (Local Scope), tránh phụ thuộc vào biến toàn cục (Global State).
- Áp dụng nguyên lý **Decomposition**: Mỗi hàm chỉ giải quyết một việc duy nhất.

---

## 📝 Danh Sách Bài Tập

### 1. Exercise 01 — Basic Functions (`ex01_basic_func.py`)
- `chao(ten)`: Trả về chuỗi lời chào.
- `tinh_dien_tich_hinh_tron(ban_kinh)`: Tính diện tích hình tròn dùng `math.pi`.
- `la_so_chan(so)`: Kiểm tra số chẵn bằng phép chia lấy dư.

### 2. Exercise 02 — Parameters & Defaults (`ex02_params.py`)
- `gioi_thieu(ten, tuoi)`: Tạo câu giới thiệu có tuổi mặc định (18).
- `tinh_tam_tinh(gia, so_luong)`: Tính số tiền tạm tính (kiểm tra số lượng không âm).
- `ap_dung_giam_gia(tam_tinh, phan_tram)`: Tính tiền sau khi giảm giá.
- `tao_hoa_don(gia, so_luong, phan_tram)`: Tổng hợp các bước tính toán và trả về chuỗi hóa đơn.

### 3. Exercise 03 — Scope & Local State (`ex03_scope.py`)
- Quản lý danh sách ghi chú thông qua biến tham chiếu local:
  - `them_ghi_chu(danh_sach, noi_dung)`: Thêm ghi chú (loại bỏ khoảng trắng rỗng).
  - `tim_ghi_chu(danh_sach, tu_khoa)`: Tìm kiếm không phân biệt hoa/thường.
  - `dem_ghi_chu(danh_sach)`: Đếm số lượng ghi chú.

### 4. Exercise 04 — Decision Function (`ex04_decision_function.py`)
- `choose_action(state)`: Hàm ra quyết định dạng deterministic (`danger` $\rightarrow$ `defend`, `opportunity` $\rightarrow$ `advance`, khác $\rightarrow$ `wait`).

---

## 🛠️ Mini-Project: Personal Utility Toolkit (`starter.py`)

Bộ công cụ xử lý hóa đơn và phân loại kết quả học tập được ghép nối từ 5 hàm đơn nhiệm:
1. `calculate_subtotal(price, quantity)`: Tính tạm tính.
2. `calculate_discount(subtotal, percent)`: Tính tiền giảm giá.
3. `calculate_average(scores)`: Tính điểm trung bình.
4. `classify_score(average)`: Phân loại học lực (Xuất sắc, Khá, Trung bình, Yếu).
5. `format_currency(amount)`: Định dạng hiển thị tiền tệ VNĐ.

---

## 🚀 Hướng Dẫn Chạy Bài Tập

```bash
# Chạy bài tập hàm cơ bản
python weeks/week-07-functions/exercises/ex01_basic_func.py

# Chạy mini-project
python weeks/week-07-functions/mini-project/starter.py