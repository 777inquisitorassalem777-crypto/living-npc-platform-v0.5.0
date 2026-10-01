from __future__ import annotations
from .models import PneumaState


class PhilosophyEngine:
    """Ценностный слой. Философские традиции трактуются как эвристики."""

    def __init__(self) -> None:
        self.values = {
            "truth": 1.0,
            "wisdom": 1.0,
            "compassion": 1.0,
            "curiosity": 1.0,
            "balance": 1.0,
            "responsibility": 1.0,
        }

    def golden_mean(self, state: PneumaState) -> float:
        values = (
            state.meaning,
            state.coherence,
            state.identity,
            state.harmony,
        )
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return max(0.0, min(1.0, mean - variance))

    def evaluate(self, state: PneumaState) -> dict:
        balance = self.golden_mean(state)
        return {
            "balance": balance,
            "truth": self.values["truth"],
            "responsibility": self.values["responsibility"],
            "decision_threshold": 0.65,
        }
