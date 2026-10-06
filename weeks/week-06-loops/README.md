# 🔁 Tuần 06: Vòng Lặp & Cấu Trúc Điều Khiển (Loops & Control Flow)

Thực hành vòng lặp `for`, `while`, vòng lặp lồng nhau (Nested Loops) và tư duy xây dựng chương trình theo menu interactive.

---

## 🎯 Mục Tiêu Học Tập
- Thành thạo duyệt `list`, `range`, `string`, sử dụng `enumerate()`, `zip()` và List Comprehension.
- Kiểm soát luồng thực thi với `while`, `while True` + `break` và xử lý nhập liệu an toàn.
- Bồi dưỡng tư duy hình học và ma trận thông qua bài toán vẽ hoa văn bằng vòng lặp lồng nhau.

---

## 📝 Danh Sách Bài Tập

### 1. Bài tập 01 — Vòng lặp `for` (`ex01_for_loops.py`)
- **Cửu chương**: In bảng cửu chương của số $n$ nhập từ bàn phím.
- **`enumerate()`**: Duyệt danh sách trái cây kèm số thứ tự.
- **`zip()`**: Ghép cặp danh sách tên và điểm số tương ứng.
- **`range()`**: Tính tổng các số chẵn từ 1 đến 100.
- **Fibonacci**: In ra $n$ số Fibonacci đầu tiên.
- **List Comprehension**: Tạo danh sách bình phương các số chẵn từ 1 đến 10.

### 2. Bài tập 02 — Vòng lặp `while` (`ex02_while_loops.py`)
- **Đếm ngược**: Đếm từ 10 về 1 và in thông báo phóng.
- **Đoán số**: Trò chơi đoán số ngẫu nhiên (1-100) có gợi ý "Cao hơn/Thấp hơn".
- **Nhập liệu an toàn**: Kiểm tra tuổi nhập vào nằm trong khoảng 1–120.
- **Menu ứng dụng**: Menu chọn phép tính (Cộng, Trừ, Nhân, Thoát).

### 3. Bài tập 03 — In hoa văn (`ex03_nested_loops.py`)
- Tam giác vuông kích thước $n$.
- Tam giác cân căn giữa kích thước $n$.
- Hình kim cương đối xứng kích thước $n$ (số lẻ).
- Bàn cờ vua $n \times n$ sử dụng ký tự `■` và `□`.

---

## 🎨 Mini-Project: Pattern Printer (`pattern_printer.py`)

Ứng dụng CLI cho phép người dùng chọn in các hoa văn hình học với kích thước và ký tự tùy chỉnh:
1. **Tam giác vuông**
2. **Hình kim cương**
3. **Cây thông Noel** (kèm gốc cây `|||`)
4. **Ma trận xoắn ốc (Spiral Matrix)**

---

## 🚀 Hướng Dẫn Chạy Bài TẬP

```bash
# Chạy bài tập vòng lặp for
python weeks/week-06-loops/exercises/ex01_for_loops.py

# Chạy mini-project
python weeks/week-06-loops/mini-project/pattern_printer.py