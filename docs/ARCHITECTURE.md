# Architecture

## Four core layers

### PNEUMA
Internal semantic/coherence state:
`meaning`, `coherence`, `identity`, `harmony`.

### PHILOSOPHY
A value and reflection layer. Cultural/philosophical material can be represented as configurable heuristics. It is not encoded as scientific fact.

### EDGE
Adaptation contour:
hypothesis generation → evaluation → learning → integration.

### UNIQUE
Maintains genealogy of candidate changes and records whether a candidate was integrated.

## Supporting infrastructure

Memory, KnowledgeGraph, WorldModel, Reflection, Planner and StabilitySuite are supporting services around the four-layer core.

## Cognitive cycle

1. Receive experience.
2. Update PNEUMA.
3. Evaluate values.
4. Persist memory.
5. Update graph/world model.
6. Reflect.
7. Plan.
8. Generate hypotheses.
9. Learn.
10. Run five stability tests.
11. Integrate only if threshold is met.
12. Record genealogy.

## GPU

The current prototype is CPU-first. GPU is an infrastructure option rather than a claim that a GPU creates consciousness. A future embedding/LLM module can use PyTorch/CUDA without changing the kernel API.
