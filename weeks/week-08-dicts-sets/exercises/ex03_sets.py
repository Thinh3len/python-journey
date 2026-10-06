"""Exercise 03: uniqueness, membership và set operations."""


def phan_tich_mon_hoc(
    semester_one: set[str], semester_two: set[str]
) -> dict[str, set[str]]:
    return {
        "common": semester_one.intersection(semester_two),
        "only_one": semester_one.difference(semester_two),
        "only_two": semester_two.difference(semester_one),
        "all": semester_one.union(semester_two),
    }


def loai_trung_giu_thu_tu(words: list[str]) -> list[str]:
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result


def tu_chung(first: str, second: str) -> set[str]:
    set_first = set(first.lower().split())
    set_second = set(second.lower().split())
    return set_first.intersection(set_second)


def la_anagram(first: str, second: str) -> bool:
    clean_first = sorted(first.lower().replace(" ", ""))
    clean_second = sorted(second.lower().replace(" ", ""))
    return clean_first == clean_second


if __name__ == "__main__":
    print(loai_trung_giu_thu_tu(["dict", "set", "dict"]))