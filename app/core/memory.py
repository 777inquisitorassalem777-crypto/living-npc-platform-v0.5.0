from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Any


class LongTermMemory:
    def __init__(self, path: str = "state/memory.json") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.items: list[dict[str, Any]] = []
        self._load()

    def _load(self) -> None:
        if self.path.exists():
            self.items = json.loads(self.path.read_text(encoding="utf-8"))

    def add(self, text: str, importance: float = 0.5, metadata=None) -> dict:
        item = {
            "id": len(self.items) + 1,
            "text": text,
            "importance": float(max(0, min(1, importance))),
            "metadata": metadata or {},
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        self.items.append(item)
        self.save()
        return item

    def search(self, query: str, limit: int = 5) -> list[dict]:
        tokens = set(query.lower().split())
        scored = []
        for item in self.items:
            overlap = len(tokens & set(item["text"].lower().split()))
            score = overlap + item["importance"] * 0.1
            if score:
                scored.append((score, item))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [item for _, item in scored[:limit]]

    def save(self) -> None:
        self.path.write_text(
            json.dumps(self.items, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def integrity(self) -> bool:
        return all(
            isinstance(x.get("id"), int) and
            isinstance(x.get("text"), str)
            for x in self.items
        )
