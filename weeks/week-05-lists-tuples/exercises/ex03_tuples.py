"""Exercise 03: tuple, packing and unpacking."""

coordinate = (3, 7)

x, y = coordinate

profile: tuple[str, int, str] = "An", 20, "Python"
name, age, topic = profile

left = "A"
right = "B"
left, right = right, left

print(f"coordinate: x={x}, y={y}")
print(f"profile: {name} · {age} · {topic}")
print(f"swapped: {left}, {right}")
