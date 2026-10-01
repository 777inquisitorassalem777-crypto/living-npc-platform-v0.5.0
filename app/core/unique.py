from __future__ import annotations
import json
from pathlib import Path


class UniqueEngine:
    """Генеалогия изменений и безопасная интеграция кандидатов."""

    def __init__(self, path="state/genealogy.json") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.records = []
        if self.path.exists():
            self.records = json.loads(self.path.read_text(encoding="utf-8"))

    def register(self, hypothesis: str, score: float, integrated: bool) -> None:
        self.records.append({
            "generation": len(self.records) + 1,
            "hypothesis": hypothesis,
            "score": score,
            "integrated": integrated,
        })
        self.path.write_text(
            json.dumps(self.records, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def export(self) -> list[dict]:
        return self.records[-100:]
