from __future__ import annotations


class SelfLearningEngine:
    def __init__(self) -> None:
        self.updates = 0

    def learn(self, reward: float, error: float) -> dict:
        reward = max(-1.0, min(1.0, reward))
        error = max(0.0, min(1.0, error))
        signal = reward * (1.0 - error)
        self.updates += 1
        return {
            "update": self.updates,
            "learning_signal": signal,
            "accepted": signal >= 0.0,
        }
