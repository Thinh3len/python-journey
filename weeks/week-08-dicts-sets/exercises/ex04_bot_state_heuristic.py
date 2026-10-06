"""Exercise 04: structured course-local state → heuristic action."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    pos = state.get("position", 0)
    goal = state.get("goal", 0)
    opp = state.get("opponent_position")

    if pos == goal:
        return "wait"

    if opp is not None and abs(pos - opp) == 1:
        return "wait"

    if pos < goal:
        return "right"
    else:
        return "left"


def main() -> None:
    """Chạy một teaching state; không phải production contract."""
    state = {
        "turn": 1,
        "max_turns": 6,
        "position": 0,
        "opponent_position": 4,
        "goal": 4,
        "min_position": 0,
        "max_position": 4,
    }
    action = choose_action(state)
    print("COURSE TEACHING MODEL")
    print("NOT VUACOC PRODUCTION CONTRACT")
    print(f"action={action}, legal={action in LOCAL_ACTIONS}")


if __name__ == "__main__":
    main()