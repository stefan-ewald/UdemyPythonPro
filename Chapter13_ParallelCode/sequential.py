import math
import time


def calc(num_elements: int) -> None:
    res = 0.0
    for i in range(num_elements):
        res += math.sqrt(i)
    print(res)


def main() -> None:
    start_time = time.perf_counter()

    for _ in range(4):
        calc(8_000_000)

    end_time = time.perf_counter()
    print(f'Took: {end_time - start_time} s')


if __name__ == '__main__':
    main()
