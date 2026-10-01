from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Experience:
    text: str
    novelty: float = 0.5
    consistency: float = 0.5
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class PneumaState:
    meaning: float = 0.6180339887
    coherence: float = 0.6180339887
    identity: float = 0.6180339887
    harmony: float = 0.6180339887


@dataclass
class WorldState:
    facts: dict[str, Any] = field(default_factory=dict)
    predictions: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class Hypothesis:
    statement: str
    score: float
    evidence: list[str] = field(default_factory=list)
    status: str = "candidate"


@dataclass
class CycleReport:
    cycle: int
    timestamp: str
    pneuma: dict[str, float]
    plan: list[str]
    hypothesis: dict[str, Any]
    stability: dict[str, bool]
    integrated: bool
