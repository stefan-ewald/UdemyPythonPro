import itertools
import math
import time
from multiprocessing import Pool


NUM_PROCESSES = 4


def calc(num_elements: int) -> None:
    res = 0.0
    for i in range(num_elements):
        res += math.sqrt(i)
    print(res)


def main() -> None:
    start_time = time.perf_counter()

    with Pool(processes=NUM_PROCESSES) as pool:
        pool.map(calc, itertools.repeat(8_000_000, NUM_PROCESSES))

    end_time = time.perf_counter()
    print(f'Took: {end_time - start_time} s')


if __name__ == '__main__':
    main()
