"""Starter for the Student Manager alternative midterm track."""


def calculate_average(student: dict[str, object]) -> float:
    """Return the average of the student's scores or zero for no data."""
    scores = student.get("scores", [])
    if not isinstance(scores, list) or not scores:
        return 0.0
    return sum(float(score) for score in scores) / len(scores)


def classify_student(average: float) -> str:
    """Return an explainable classification from an average."""
    if average >= 8.5:
        return "Giỏi"
    if average >= 7.0:
        return "Khá"
    if average >= 5.0:
        return "Trung bình"
    return "Yếu"


def find_student(
    students: list[dict[str, object]], query: str
) -> dict[str, object] | None:
    """Return the first case-insensitive name match."""
    target = query.strip().lower()
    for student in students:
        name = str(student.get("name", "")).strip().lower()
        if name == target:
            return student
    return None


def main() -> None:
    """Run the starter with nested sample data."""
    students = [
        {"name": "An", "scores": [8.0, 9.0, 7.0]},
        {"name": "Bình", "scores": [7.0, 6.0, 8.0]},
    ]
    for student in students:
        average = calculate_average(student)
        print(f"{student['name']}: {average:.1f} — {classify_student(average)}")


if __name__ == "__main__":
    main()
