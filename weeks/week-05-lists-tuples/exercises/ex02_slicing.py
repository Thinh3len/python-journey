"""Exercise 02: slicing, mutability, alias and copy."""

numbers = [1, 2, 3, 4, 5, 6]

first_three: list[int] = numbers[:3]
last_three: list[int] = numbers[-3:]

alias: list[int] = numbers
copied: list[int] = numbers.copy()

alias.append(7)

print(f"first_three={first_three}, last_three={last_three}")
print(f"numbers={numbers}")
print(f"alias={alias}")
print(f"copied={copied}")
print(f"alias shares numbers: {alias is numbers}")
print(f"copied is independent: {copied is not numbers}")
