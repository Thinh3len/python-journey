# starter.py - Personal Utility Toolkit

def calculate_subtotal(price: float, quantity: int) -> float:
    if quantity <= 0 or price < 0:
        return 0.0
    return price * quantity


def calculate_discount(subtotal: float, percent: float = 0) -> float:
    if subtotal <= 0 or percent <= 0:
        return 0.0
    return subtotal * (percent / 100)


def calculate_average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def classify_score(average: float) -> str:
    if average >= 8.5:
        return "Xuất sắc"
    elif average >= 7.0:
        return "Khá"
    elif average >= 5.0:
        return "Trung bình"
    return "Yếu"


def format_currency(amount: float) -> str:
    return f"{amount:,.0f} VNĐ"


def main():
    print("=== 1. TÍNH HÓA ĐƠN ===")
    price = 150000.0
    quantity = 3
    discount_percent = 10.0

    subtotal = calculate_subtotal(price, quantity)
    discount_amount = calculate_discount(subtotal, discount_percent)
    final_total = subtotal - discount_amount

    print(f"Giá sản phẩm : {format_currency(price)}")
    print(f"Số lượng     : {quantity}")
    print(f"Tạm tính     : {format_currency(subtotal)}")
    print(f"Giảm giá     : {format_currency(discount_amount)} ({discount_percent}%)")
    print(f"Tổng thanh toán: {format_currency(final_total)}")

    print("\n=== 2. ĐÁNH GIÁ KẾT QUẢ HỌC TẬP ===")
    student_scores = [8.5, 7.0, 9.0, 8.0]
    avg_score = calculate_average(student_scores)
    classification = classify_score(avg_score)

    print(f"Danh sách điểm: {student_scores}")
    print(f"Điểm trung bình: {avg_score:.2f}")
    print(f"Xếp loại học lực: {classification}")


if __name__ == "__main__":
    main()