from __future__ import annotations
from .models import PneumaState


class ReflectionEngine:
    def analyze(self, state: PneumaState, history: list[dict]) -> dict:
        recent = history[-10:]
        stability = (
            sum(x.get("stability_score", 0.0) for x in recent) / len(recent)
            if recent else 1.0
        )
        return {
            "coherence": state.coherence,
            "identity": state.identity,
            "harmony": state.harmony,
            "historical_stability": stability,
            "reflection": (
                "stable" if state.harmony >= 0.6 else "requires_review"
            ),
        }
