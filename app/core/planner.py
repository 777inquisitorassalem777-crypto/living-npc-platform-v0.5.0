from __future__ import annotations


class Planner:
    def make_plan(self, goal: str, context: dict) -> list[str]:
        return [
            f"clarify:{goal}",
            "inspect_memory",
            "inspect_world_model",
            "evaluate_values",
            "execute_low_risk_action",
            "measure_result",
        ]
