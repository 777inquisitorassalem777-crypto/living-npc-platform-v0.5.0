from __future__ import annotations
from .models import Experience, PneumaState


class PneumaEngine:
    """Символический слой смысла и внутренней согласованности."""

    def __init__(self) -> None:
        self.state = PneumaState()

    @staticmethod
    def clamp(value: float) -> float:
        return max(0.0, min(1.0, value))

    def update(self, experience: Experience) -> PneumaState:
        n = self.clamp(experience.novelty)
        c = self.clamp(experience.consistency)

        self.state.meaning = self.clamp(
            0.95 * self.state.meaning + 0.05 * n
        )
        self.state.coherence = self.clamp(
            0.90 * self.state.coherence + 0.10 * c
        )
        self.state.identity = self.clamp(
            0.98 * self.state.identity + 0.02 * self.state.coherence
        )
        self.state.harmony = (
            self.state.meaning +
            self.state.coherence +
            self.state.identity
        ) / 3.0
        return self.state
