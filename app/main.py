from .core.kernel import PnevmaEdgeKernel


def main():
    kernel = PnevmaEdgeKernel()
    for text in (
        "Первое наблюдение системы",
        "Новая гипотеза о согласованности",
        "Проверка устойчивости",
    ):
        result = kernel.cycle_once(text, novelty=0.7, consistency=0.85)
        print(result)
    print(kernel.status())


if __name__ == "__main__":
    main()
