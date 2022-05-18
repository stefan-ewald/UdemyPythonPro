from typing import Any

from fastvector import VectorND

import pytest


V1 = VectorND(0, 0)
V2 = VectorND(-1, 1)
V3 = VectorND(2.5, -2.5)


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, V2, VectorND(-1, 1)),
        (V1, V3, VectorND(2.5, -2.5)),
        (V3, V2, VectorND(1.5, -1.5)),
    )
)
def test_add(lhs: VectorND, rhs: VectorND, exp_res: VectorND) -> None:
    assert lhs + rhs == exp_res


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, V2, VectorND(1, -1)),
        (V1, V3, VectorND(-2.5, 2.5)),
        (V3, V2, VectorND(3.5, -3.5)),
    )
)
def test_sub(lhs: VectorND, rhs: VectorND, exp_res: VectorND) -> None:
    assert lhs - rhs == exp_res


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, V2, 0.0),
        (V1, V3, 0.0),
        (V3, V2, -5.0),
    )
)
def test_mul_vec(lhs: VectorND, rhs: VectorND, exp_res: float) -> None:
    assert lhs * rhs == exp_res


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, 2.0, VectorND(0.0, 0.0)),
        (V2, 2.0, VectorND(-2.0, 2.0)),
        (V3, 2.0, VectorND(5.0, -5.0)),
    )
)
def test_mul_float(lhs: VectorND, rhs: float, exp_res: VectorND) -> None:
    assert lhs * rhs == exp_res


@pytest.mark.skip(reason="Not implemented")
def test_abs() -> None:
    pass


@pytest.mark.parametrize(
    ('x', 'y'),
    (
        (-1, None),
        (None, -1),
        (None, None),
    )
)
def test_raises(x: Any, y: Any) -> None:
    with pytest.raises(TypeError):
        _ = VectorND(x, y)


def test_repr(capture_stdout: dict) -> None:
    print(repr(VectorND(1.0, 2.0)))
    assert capture_stdout["stdout"] == "vector.VectorND(array('d', [1.0, 2.0]))\n"


def test_str(capture_stdout: dict) -> None:
    print(str(VectorND(1.0, 2.0)))
    assert capture_stdout["stdout"] == "(array('d', [1.0, 2.0]))\n"
