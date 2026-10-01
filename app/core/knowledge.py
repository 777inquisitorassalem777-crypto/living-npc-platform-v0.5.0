from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Edge:
    source: str
    relation: str
    target: str


class KnowledgeGraph:
    def __init__(self) -> None:
        self.nodes: set[str] = set()
        self.edges: list[Edge] = []

    def add_node(self, node: str) -> None:
        self.nodes.add(node)

    def connect(self, source: str, relation: str, target: str) -> None:
        self.add_node(source)
        self.add_node(target)
        edge = Edge(source, relation, target)
        if edge not in self.edges:
            self.edges.append(edge)

    def neighbors(self, node: str) -> list[str]:
        return [
            e.target for e in self.edges
            if e.source == node
        ]

    def consistent(self) -> bool:
        return all(
            e.source in self.nodes and e.target in self.nodes
            for e in self.edges
        )

    def export(self) -> dict:
        return {
            "nodes": sorted(self.nodes),
            "edges": [
                {
                    "source": e.source,
                    "relation": e.relation,
                    "target": e.target,
                }
                for e in self.edges
            ],
        }
