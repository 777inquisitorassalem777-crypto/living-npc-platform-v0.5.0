from fastapi import FastAPI
from pydantic import BaseModel, Field
from .core.kernel import PnevmaEdgeKernel

app = FastAPI(
    title="PNEUMA–EDGE UNIQUE",
    version="1.0.0",
    description="Research cognitive architecture",
)

kernel = PnevmaEdgeKernel()


class CycleRequest(BaseModel):
    text: str = Field(min_length=1)
    novelty: float = Field(default=0.5, ge=0, le=1)
    consistency: float = Field(default=0.8, ge=0, le=1)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/status")
def status():
    return kernel.status()


@app.post("/cycle")
def cycle(request: CycleRequest):
    return kernel.cycle_once(
        request.text,
        request.novelty,
        request.consistency,
    )


@app.get("/memory")
def memory(q: str = ""):
    return kernel.memory.search(q) if q else kernel.memory.items[-20:]


@app.get("/knowledge")
def knowledge():
    return kernel.graph.export()


@app.get("/genealogy")
def genealogy():
    return kernel.unique.export()
