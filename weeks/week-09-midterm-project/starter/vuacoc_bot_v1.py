"""Starter for the course-local VuaCóc Bot V1 midterm track."""

LOCAL_ACTIONS = {"left", "right", "wait"}


def choose_action(state: dict[str, int]) -> str:
    """Return a legal course-local action from a small structured state."""
    position = state.get("position", 0)
    goal = state.get("goal", position)
    opponent = state.get("opponent_position")

    if position == goal:
        return "wait"
    if opponent is not None and abs(position - opponent) <= 1:
        return "wait"
    if position < goal:
        return "right"
    return "left"


def explain_action(state: dict[str, int], action: str) -> str:
    """Explain which observed state values led to an action."""
    position = state.get("position")
    opponent = state.get("opponent_position")
    goal = state.get("goal")
    return (
        f"position={position}, opponent={opponent}, goal={goal} -> {action}"
    )


def main() -> None:
    """Smoke-test one structured course-local state."""
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
    print(explain_action(state, action))
    print(f"legal={action in LOCAL_ACTIONS}")


if __name__ == "__main__":
    main()
