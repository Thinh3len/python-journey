# Tuần 06 — Loops · `enumerate` · `zip` · comprehensions
Tuần này luyện cách lặp qua dữ liệu, chọn đúng kiểu vòng lặp và kiểm tra kết quả ở từng bước. Dành khoảng 7–10 giờ, chia thành các phiên ngắn.

## Kết quả cần đạt

- Dùng `for` với iterable và `range()`; dùng `while` khi cần lặp theo điều kiện.
- Dùng `break`, `continue` có chủ đích và tránh vòng lặp không có điểm dừng.
- Dùng `enumerate()` để lấy số thứ tự và `zip()` để ghép dữ liệu song song.
- Viết comprehension đơn giản, dễ đọc; dùng nested loop khi bài toán cần.

## Quy trình làm

1. **Learn:** Đọc [`notes.md`](notes.md). Tự chạy từng ví dụ nhỏ và giải thích khi nào vòng lặp kết thúc.
2. **Build:** Làm lần lượt ba file trong `exercises/`: `ex01_for_loop.py`, `ex02_while_loop.py`, rồi `ex03_patterns.py`. Hoàn thành TODO theo thứ tự; bài cuối có các thử thách bổ sung.
3. **Test:** Chạy từng file từ thư mục gốc repo. Với input, thử cả giá trị hợp lệ, biên và không hợp lệ; đối chiếu kết quả với yêu cầu trong TODO.
	```bash
	python weeks/week-06-loops/exercises/ex01_for_loop.py
	python weeks/week-06-loops/exercises/ex02_while_loop.py
	python weeks/week-06-loops/exercises/ex03_patterns.py
	```
4. **Debug:** Khi kết quả sai, kiểm tra giá trị biến ở mỗi lượt lặp, điều kiện dừng và cách cập nhật biến. Sửa một nguyên nhân rồi chạy lại đúng bài đó.
5. **Improve:** Thử thay cách duyệt index thủ công bằng `enumerate()` hoặc `zip()` khi phù hợp. Hoàn thành TODO comprehension và giữ biểu thức ngắn, dễ đọc.
6. **Build + Test:** Hoàn thành [Pattern Printer](mini-project/README.md), chạy các lựa chọn trong menu với kích thước nhỏ và kiểm tra hình in.
7. **Prove:** Ghi lại một lỗi đã debug, output mini-project và commit bài làm; cập nhật [`PROGRESS.md`](../../PROGRESS.md).

## Sau khi thử

Các lời giải tham khảo nằm trong `solutions/`. Chỉ mở để so sánh sau khi đã tự làm; hãy giải thích được điểm khác nhau và tự chạy lại bài của mình.

## Đọc thêm

[Think Python — Chapter 6: Iteration](https://allendowney.github.io/ThinkPython/chap06.html)
