"""Exercise 01: list create, read, update and delete."""

subjects = ["Toán", "Văn", "Anh"]

subjects.append("Tin")
print(
    f"after append: first={subjects[0]}, "
    f"last={subjects[-1]}, middle={subjects[1:-1]}"
)

subjects.insert(1, "Sử")
print(
    f"after insert: first={subjects[0]}, "
    f"last={subjects[-1]}, middle={subjects[1:-1]}"
)

subjects[0] = "Toán học"
print(
    f"after update: first={subjects[0]}, "
    f"last={subjects[-1]}, middle={subjects[1:-1]}"
)

subjects.remove("Anh")
print(
    f"after remove: first={subjects[0]}, "
    f"last={subjects[-1]}, middle={subjects[1:-1]}"
)

last_subject = subjects.pop()
print(
    f"after pop: first={subjects[0]}, "
    f"last={subjects[-1]}, middle={subjects[1:-1]}"
)
print(f"popped={last_subject}, remaining={subjects}")
