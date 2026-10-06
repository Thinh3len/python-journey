"""Exercise 01: đọc, cập nhật và duyệt dictionary."""


def cap_nhat_diem(
    scores: dict[str, float], subject: str, score: float
) -> dict[str, float]:
    new_scores = scores.copy()
    new_scores[subject] = score
    return new_scores


def diem_trung_binh(scores: dict[str, float]) -> float:
    if not scores:
        return 0.0
    values = scores.values()
    return sum(values) / len(values)


def dem_tan_suat(text: str) -> dict[str, int]:
    frequency = {}
    for char in text:
        if char == " ":
            continue
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def main() -> None:
    scores = {"Toán": 8.0, "Văn": 7.0, "Anh": 9.0}
    print(cap_nhat_diem(scores, "Văn", 8.0))
    print(diem_trung_binh(scores))
    print(dem_tan_suat("hello"))


if __name__ == "__main__":
    main()