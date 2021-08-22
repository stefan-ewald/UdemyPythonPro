import math
import time
from threading import Thread


NUM_THREADS = 4


def calc(num_elements: int) -> None:
    res = 0.0
    for i in range(num_elements):
        res += math.sqrt(i)
    print(res)


def main() -> None:
    threads = []
    for _ in range(NUM_THREADS):
        threads.append(Thread(target=calc, args=(8_000_000,)))

    start_time = time.perf_counter()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter()
    print(f'Took: {end_time - start_time} s')


if __name__ == '__main__':
    main()
