"""Starter for the Week 08 Decision Dashboard."""

REQUIRED_FIELDS = {"position", "goal"}
LOCAL_ACTIONS = {"left", "right", "wait"}


def validate_state(state: dict[str, object]) -> bool:
    """Return whether all required fields exist."""
    return REQUIRED_FIELDS.issubset(state.keys())


def summarize_state(state: dict[str, object]) -> str:
    """Return a short learner-readable summary."""
    pos = state.get("position", 0)
    goal = state.get("goal", 0)
    opp = state.get("opponent_position", "N/A")
    history = state.get("history", [])

    return f"Position: {pos} | Goal: {goal} | Opponent: {opp} | History steps: {len(history)}"


def recommend_action(state: dict[str, object]) -> str:
    """Return one recommendation from 2–4 explainable rules."""
    pos = state.get("position")
    goal = state.get("goal")

    if not isinstance(pos, int) or not isinstance(goal, int):
        return "wait"

    opp = state.get("opponent_position")

    if pos == goal:
        return "wait"

    if isinstance(opp, int) and abs(pos - opp) == 1:
        return "wait"

    if pos < goal:
        return "right"
    else:
        return "left"


def run_case(name: str, dashboard: dict[str, object]) -> None:
    """Helper to run and display test cases."""
    print(f"\n--- TEST CASE: {name} ---")
    state = dashboard.get("state")
    tags = dashboard.get("tags", set())

    if not isinstance(state, dict):
        print("State không hợp lệ")
        return

    is_valid = validate_state(state)
    print(f"Tags: {tags}")
    print(f"valid={is_valid}")

    if is_valid:
        print(summarize_state(state))
        action = recommend_action(state)
        print(f"action={action}, legal={action in LOCAL_ACTIONS}")
    else:
        print("State thiếu required fields!")


def main() -> None:
    """Run the dashboard on normal, boundary, and missing optional field models."""
    print("COURSE TEACHING MODEL")
    print("NOT VUACOC PRODUCTION CONTRACT")

    normal_case = {
        "state": {
            "position": 1,
            "opponent_position": 3,
            "goal": 4,
            "history": ["right", "right"],
        },
        "tags": {"course-local", "week-08", "normal-case"},
    }

    boundary_case = {
        "state": {
            "position": 4,
            "opponent_position": 2,
            "goal": 4,
            "history": ["right", "right", "wait"],
        },
        "tags": {"course-local", "week-08", "at-goal"},
    }

    missing_optional_case = {
        "state": {
            "position": 0,
            "goal": 2,
        },
        "tags": {"course-local", "week-08", "minimal-state"},
    }

    invalid_case = {
        "state": {
            "position": 1,
        },
        "tags": {"course-local", "week-08", "invalid-state"},
    }

    run_case("Normal Case", normal_case)
    run_case("Boundary Case (At Goal)", boundary_case)
    run_case("Missing Optional Field", missing_optional_case)
    run_case("Invalid Case (Missing Required Field)", invalid_case)

    print("\n" + "=" * 40)
    print("DATA MODELING DECISION:")
    print("- Dict chính (`dashboard`): Đóng gói toàn bộ thông tin hệ thống.")
    print("- Nested Dict (`state`): Lưu trữ trạng thái động của đối tượng (vị trí, đối thủ).")
    print("- Nested List (`history`): Lưu trữ lịch sử di chuyển phục vụ phân tích.")
    print("- Set (`REQUIRED_FIELDS`, `tags`): Kiểm tra nhanh quyền hạn/nhãn và validate tập dữ liệu.")
    print("- Field bắt buộc (`position`, `goal`): Cần thiết để thuật toán điều hướng hoạt động.")
    print("- Field tùy chọn (`opponent_position`, `history`): Bổ trợ thêm thông tin nâng cao.")


if __name__ == "__main__":
    main()