from app.core.kernel import PnevmaEdgeKernel


def isolated(tmp_path):
    return PnevmaEdgeKernel(
        memory_path=str(tmp_path / "memory.json"),
        genealogy_path=str(tmp_path / "genealogy.json"),
    )


def test_kernel_cycle(tmp_path):
    kernel = isolated(tmp_path)
    result = kernel.cycle_once("test experience", 0.7, 0.9)
    assert result["cycle"] == 1
    assert 0 <= result["stability_score"] <= 1


def test_memory_and_graph(tmp_path):
    kernel = isolated(tmp_path)
    kernel.cycle_once("memory graph test")
    assert len(kernel.memory.items) == 1
    assert len(kernel.graph.nodes) >= 1


def test_five_stability_tests(tmp_path):
    kernel = isolated(tmp_path)
    result = kernel.cycle_once("stability")
    assert len(result["stability"]) == 5
    assert all(isinstance(v, bool) for v in result["stability"].values())
