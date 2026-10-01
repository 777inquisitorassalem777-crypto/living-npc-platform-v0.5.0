from __future__ import annotations
from .models import PneumaState


class StabilitySuite:
    """Пять детерминированных архитектурных тестов."""

    def run(
        self,
        state: PneumaState,
        memory_ok: bool,
        graph_ok: bool,
        world_score: float,
        history: list[dict],
    ) -> dict[str, bool]:

        tests = {
            "pneuma_coherence":
                0.0 <= state.coherence <= 1.0,
            "value_consistency":
                0.0 <= state.harmony <= 1.0,
            "memory_integrity":
                memory_ok,
            "world_model_consistency":
                0.0 <= world_score <= 1.0 and graph_ok,
            "evolution_symbiosis":
                (
                    state.identity >= 0.45 and
                    state.harmony >= 0.45 and
                    len(history) >= 0
                ),
        }
        return tests

    @staticmethod
    def score(results: dict[str, bool]) -> float:
        return sum(results.values()) / len(results)
