"""Own implementation of a 2D vector class.
"""
from __future__ import annotations

import array
import numbers
from functools import total_ordering
from math import sqrt
from typing import Any
from typing import SupportsFloat
from typing import Union


@total_ordering
class VectorND:
    def __init__(self, *args: Any, dtype: str = "d") -> None:
        """Create a vector with the given values.

        Args:
            args (Any): The vector values.
            dtype (str): The data type of the array.array.

        Raises:
            TypeError: If x or y are not a number.
        """
        if len(args) == 1 and isinstance(args[0], list):
            self.values = array.array(dtype, args[0])
        elif len(args) > 0:
            inputs = [val for val in args]
            self.values = array.array(dtype, inputs)
        else:
            raise TypeError('You must pass in int/float value for x and y!')

    def __repr__(self) -> str:
        """Return the vector representation.

        Returns:
            The representation of the vector.
        """
        return f'vector.VectorND({self.values})'

    def __str__(self) -> str:
        """The vector as a string.

        Returns:
            The vector as a string.
        """
        return f'({self.values})'

    def __abs__(self) -> float:
        """Return the length (magnitude) of the vector.

        Returns:
            Length of the vector.
        """
        return sqrt(sum(pow(val, 2) for val in self.values))

    def __eq__(self, other_vector: object) -> bool:
        """Check if the vectors have the same values.

        Args:
            other_vector: Other vector (rhs)

        Returns:
            True, if the both vectors have the same values.
            False, else.
        """
        if not isinstance(other_vector, VectorND):
            return False
        return self.values == other_vector.values

    def __lt__(self, other_vector: VectorND) -> bool:
        """Check if the self is less than the other vector.

        Args:
            other_vector: Other vector (rhs).

        Returns:
            True, if the self is less than the other vector.
            False, else.
        """
        if not isinstance(other_vector, VectorND):
            raise TypeError('You must pass in a VectorND instance!')
        return abs(self) < abs(other_vector)

    def __add__(self, other_vector: VectorND) -> VectorND:
        """Returns the additon vector of the self and the other vector.

        Args:
            other_vector: Other vector (rhs).

        Returns:
            The additon vector of the self and the other vector.
        """
        if not isinstance(other_vector, VectorND):
            raise TypeError('You must pass in a VectorND instance!')
        result = [v1 + v2 for v1, v2 in zip(self.values, other_vector.values)]
        return VectorND(result)

    def __sub__(self, other_vector: VectorND) -> VectorND:
        """Return the subtraction vector of the self and the other vector.

        Args:
            other_vector: Other vector (rhs).

        Returns:
            The subtraction vector of the self and the other vector.
        """
        if not isinstance(other_vector, VectorND):
            raise TypeError('You must pass in a VectorND instance!')
        result = [v1 - v2 for v1, v2 in zip(self.values, other_vector.values)]
        return VectorND(result)

    def __mul__(
        self, other: Union[VectorND, SupportsFloat]
    ) -> Union[VectorND, SupportsFloat]:
        """Return the multiplication of self and the other vector/number.

        Args:
            other: Other vector or scaler value (rhs)

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and the other vector/number.
        """
        if isinstance(other, VectorND):
            return sum([v1 * v2 for v1, v2 in zip(self.values, other.values)])
        if not isinstance(other, numbers.Real):
            raise TypeError('You must pass in an int/float!')
        return VectorND([v * other for v in self.values])

    def __truediv__(self, other: SupportsFloat) -> VectorND:
        """Return the multiplication of self and the other vector/number.

        Args:
            other: Other vector or scaler value (rhs).

        Raises:
            ValueError: Division by zero.
            TypeError: Not int/float passed in.

        Returns:
            The multiplication of self and the other vector/number.
        """
        if not isinstance(other, numbers.Real):
            raise TypeError('You must pass in an int/float!')
        return VectorND([v / other for v in self.values])
