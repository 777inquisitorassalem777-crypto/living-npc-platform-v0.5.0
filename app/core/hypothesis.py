from __future__ import annotations
import hashlib
from .models import Hypothesis


class HypothesisGenerator:
    def generate(self, observation: str, count: int = 5) -> list[Hypothesis]:
        base = observation.strip() or "unknown observation"
        variants = [
            f"Улучшить согласованность модели через: {base}",
            f"Проверить альтернативную интерпретацию: {base}",
            f"Сопоставить память и модель мира для: {base}",
            f"Изменить стратегию планирования для: {base}",
            f"Проверить устойчивость ценностей при: {base}",
        ]
        result = []
        for i, statement in enumerate(variants[:count]):
            digest = hashlib.sha256(statement.encode()).hexdigest()
            score = int(digest[:4], 16) / 65535
            result.append(Hypothesis(statement, score))
        return result
