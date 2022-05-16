import pytest
from vector import Vector2D


V1 = Vector2D(0, 0)
V2 = Vector2D(-1, 1)
V3 = Vector2D(2.5, -2.5)


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, V2, Vector2D(-1, 1)),
        (V1, V3, Vector2D(2.5, -2.5)),
        (V3, V2, Vector2D(1.5, -1.5)),
    )
)
def test_add(lhs: Vector2D, rhs: Vector2D, exp_res: Vector2D):
    assert lhs + rhs == exp_res


@pytest.mark.parametrize(
    ('lhs', 'rhs', 'exp_res'),
    (
        (V1, V2, Vector2D(1, -1)),
        (V1, V3, Vector2D(-2.5, 2.5)),
        (V3, V2, Vector2D(3.5, -3.5)),
    )
)
def test_sub(lhs: Vector2D, rhs: Vector2D, exp_res: Vector2D):
    assert lhs - rhs == exp_res


@pytest.mark.skip(reason="Not implemented")
def test_mul(lhs: Vector2D, rhs: Vector2D, exp_res: Vector2D):
    assert lhs - rhs == exp_res


def test_raises():
    with pytest.raises(TypeError):
        _ = Vector2D(None, 2.0)


def test_repr(capture_stdout: dict):
    print(Vector2D(1.0, 2.0))
    assert capture_stdout["stdout"] == "(1.0, 2.0)\n"
