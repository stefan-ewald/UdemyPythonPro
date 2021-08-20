'''Test code.
'''
from typing import Any

import numpy as np

import fastvector
import math_cpython
import math_numba


l = [i for i in range(1_000_000)]
a = np.array([i for i in range(1_000_000)], dtype=np.int64)
v = fastvector.VectorND([i for i in range(1_000_000)])

NUM_ROUNDS = 200
NUM_ITERATIONS = 10


# def test_python_clip_vector(benchmark: Any) -> None:
#     benchmark.pedantic(
#         fastvector.python_clip_vector,
#         args=(v, -1, 1, v),
#         rounds=NUM_ROUNDS,
#         iterations=NUM_ITERATIONS
#     )


# def test_naive_cython_clip_vector(benchmark: Any) -> None:
#     benchmark.pedantic(
#         fastvector.naive_cython_clip_vector,
#         args=(v, -1, 1, v),
#         rounds=NUM_ROUNDS,
#         iterations=NUM_ITERATIONS
#     )


def test_cython_clip_vector(benchmark: Any) -> None:
    benchmark.pedantic(
        fastvector.cython_clip_vector,
        args=(v, -1, 1, v),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS
    )


def test_np_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        np.clip,
        args=(a, -1, 1, a),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS
    )


def test_numba_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_numba.clip,
        args=(a, -1, 1),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS
    )


def test_cpython_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cpython.clip,
        args=(l, -1, 1),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS
    )
