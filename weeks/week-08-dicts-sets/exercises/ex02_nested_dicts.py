"""Exercise 02: đọc và biến đổi nested data."""


def diem_trung_binh(student: dict[str, object]) -> float:
    scores = student.get("scores", [])
    if not isinstance(scores, list) or not scores:
        return 0.0
    return sum(scores) / len(scores)


def hoc_sinh_tot_nhat(classroom: dict[str, dict[str, object]]) -> str:
    if not classroom:
        return ""
    
    best_student = ""
    max_avg = -1.0
    
    for name, student in classroom.items():
        avg = diem_trung_binh(student)
        if avg > max_avg:
            max_avg = avg
            best_student = name
            
    return best_student


def tong_gia_tri_kho(products: dict[str, dict[str, object]]) -> float:
    total_value = 0.0
    for product in products.values():
        price = product.get("price", 0.0)
        quantity = product.get("quantity", 0)
        if isinstance(price, (int, float)) and isinstance(quantity, (int, float)):
            total_value += price * quantity
    return total_value


def main() -> None:
    classroom = {
        "An": {"age": 20, "scores": [8, 9, 7]},
        "Bình": {"age": 21, "scores": [7, 6, 8]},
    }
    print(hoc_sinh_tot_nhat(classroom))


if __name__ == "__main__":
    main()