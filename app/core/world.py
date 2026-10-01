from __future__ import annotations
from .models import WorldState


class WorldModel:
    def __init__(self) -> None:
        self.state = WorldState()

    def observe(self, key: str, value) -> None:
        self.state.facts[key] = value

    def predict(self, key: str, value, confidence: float) -> dict:
        prediction = {
            "key": key,
            "value": value,
            "confidence": max(0.0, min(1.0, confidence)),
        }
        self.state.predictions.append(prediction)
        return prediction

    def consistency(self) -> float:
        if not self.state.predictions:
            return 1.0
        return sum(
            p["confidence"] for p in self.state.predictions
        ) / len(self.state.predictions)
