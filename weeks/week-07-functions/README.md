# Tuần 07 — Functions · Decomposition · Scope · Type hints

Tuần này dùng hàm để chia một vấn đề thành những phần nhỏ, nhận input và trả
output rõ ràng. Đây là tuần thí điểm cho learning loop:

```text
Learn → Build → Test → Debug → Improve → Commit → Prove
```

## Mục tiêu

Sau Week 07, bạn có thể:

- viết và gọi hàm với `def`;
- phân biệt parameter và argument;
- dùng `return` để đưa dữ liệu về nơi gọi hàm;
- dùng default parameter ở mức cơ bản;
- giải thích local scope và tránh lạm dụng global state;
- phân rã một bài toán thành các hàm nhỏ;
- viết docstring ngắn và type hints cơ bản;
- giải thích vì sao type hints không tự kiểm tra kiểu khi chương trình chạy;
- viết một decision function đơn giản, xác định được từ input đến output.

## Prerequisites

Bạn nên hoàn thành Week 01–06 và đã quen với biến, kiểu dữ liệu, điều kiện,
chuỗi, list và loop.

## Quy trình làm

1. **Learn:** Đọc [`notes.md`](notes.md), chú ý sự khác nhau giữa `print()` và `return`, local scope, và type hints không kiểm tra kiểu lúc runtime.
2. **Build:** Chạy lần lượt các ví dụ trong [`examples/`](examples/), sau đó tự làm bốn bài trong [`exercises/`](exercises/). Đọc từng tầng trong [`hints.md`](hints.md) nếu bị kẹt; chỉ xem solutions sau khi đã thử.
3. **Test:** Với mỗi hàm, thử một trường hợp thông thường và ít nhất một trường hợp biên. Kiểm tra giá trị trả về, không chỉ nhìn nội dung được in.
4. **Debug:** Đọc traceback, xác định hàm và input gây sai, sửa một nguyên nhân rồi chạy lại trường hợp đó.
5. **Improve:** Làm rõ tên hàm và contract; tách trách nhiệm nếu một hàm đang làm nhiều việc. Không dùng global state khi có thể truyền parameter và `return` kết quả.
6. **Build + Test:** Hoàn thành [Personal Utility Toolkit](mini-project/README.md). Chạy starter từ thư mục gốc repo:
       ```bash
       python weeks/week-07-functions/mini-project/starter.py
       ```
7. **Prove:** Lưu output chạy thành công, ghi một bug đã debug, commit kết quả và cập nhật [`PROGRESS.md`](../../PROGRESS.md).

## Kiểm tra reference solutions

Lệnh dưới đây dành cho maintainer hoặc người muốn xác minh các lời giải tham khảo. Nó kiểm tra official solutions, **không** chấm bài trong `exercises/` hay `mini-project/starter.py` của người học:

```bash
python weeks/week-07-functions/checks/check_solutions.py
```

Kết quả mong đợi: `Week 07 solution checks: PASS`.

## Checklist

- [ ] Tôi dùng `return` đúng.
- [ ] Tôi chia được bài toán thành nhiều hàm.
- [ ] Tôi giải thích được local scope.
- [ ] Tôi viết được type hints cơ bản.
- [ ] Tôi biết type hints không validate runtime.
- [ ] Tôi hoàn thành decision function.
- [ ] Tôi tự kiểm tra normal case và boundary case.
- [ ] Tôi hoàn thành mini-project.
- [ ] Tôi commit kết quả.

## Evidence

Lưu lại:

- kết quả kiểm tra các normal case và boundary case;
- output khi chạy mini-project;
- commit chứa bài làm với message có ý nghĩa;
- một ghi chú ngắn về lỗi bạn đã gặp và cách bạn sửa lỗi.

## VuaCóc Bot Journey

Week 07 milestone: [Function Bot](../../projects/vuacoc-bot-journey/milestones/w07-function-bot.md).
