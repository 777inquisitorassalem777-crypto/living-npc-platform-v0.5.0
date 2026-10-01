from __future__ import annotations
from .models import Experience, CycleReport
from .pneuma import PneumaEngine
from .philosophy import PhilosophyEngine
from .memory import LongTermMemory
from .knowledge import KnowledgeGraph
from .world import WorldModel
from .reflection import ReflectionEngine
from .planner import Planner
from .hypothesis import HypothesisGenerator
from .learning import SelfLearningEngine
from .tests import StabilitySuite
from .unique import UniqueEngine


class PnevmaEdgeKernel:
    def __init__(self, memory_path: str = "state/memory.json",
                 genealogy_path: str = "state/genealogy.json") -> None:
        self.cycle = 0
        self.history = []
        self.pneuma = PneumaEngine()
        self.philosophy = PhilosophyEngine()
        self.memory = LongTermMemory(memory_path)
        self.graph = KnowledgeGraph()
        self.world = WorldModel()
        self.reflection = ReflectionEngine()
        self.planner = Planner()
        self.hypotheses = HypothesisGenerator()
        self.learning = SelfLearningEngine()
        self.tests = StabilitySuite()
        self.unique = UniqueEngine(genealogy_path)

    def cycle_once(
        self,
        text: str,
        novelty: float = 0.5,
        consistency: float = 0.8,
    ) -> dict:
        self.cycle += 1
        exp = Experience(text, novelty, consistency)

        state = self.pneuma.update(exp)
        values = self.philosophy.evaluate(state)

        self.memory.add(
            text,
            importance=(novelty + consistency) / 2,
        )

        self.graph.connect("experience", "contains", text[:80])
        self.world.observe("last_experience", text)

        reflection = self.reflection.analyze(state, self.history)
        plan = self.planner.make_plan(
            "integrate useful experience",
            reflection,
        )

        candidates = self.hypotheses.generate(text, 5)
        best = max(candidates, key=lambda h: h.score)

        learning = self.learning.learn(
            reward=best.score,
            error=1.0 - consistency,
        )

        stability = self.tests.run(
            state,
            self.memory.integrity(),
            self.graph.consistent(),
            self.world.consistency(),
            self.history,
        )
        score = self.tests.score(stability)

        integrated = score >= 0.8
        self.unique.register(
            best.statement,
            best.score,
            integrated,
        )

        report = CycleReport(
            cycle=self.cycle,
            timestamp=__import__("datetime").datetime.now(
                __import__("datetime").timezone.utc
            ).isoformat(),
            pneuma=state.__dict__.copy(),
            plan=plan,
            hypothesis={
                "statement": best.statement,
                "score": best.score,
                "learning": learning,
            },
            stability=stability,
            integrated=integrated,
        )

        result = report.__dict__
        result["values"] = values
        result["reflection"] = reflection
        result["stability_score"] = score

        self.history.append(result)
        return result

    def status(self) -> dict:
        return {
            "cycle": self.cycle,
            "pneuma": self.pneuma.state.__dict__,
            "memory_items": len(self.memory.items),
            "knowledge_nodes": len(self.graph.nodes),
            "knowledge_edges": len(self.graph.edges),
            "learning_updates": self.learning.updates,
            "history": len(self.history),
        }
