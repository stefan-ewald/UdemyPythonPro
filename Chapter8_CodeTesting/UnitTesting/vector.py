"""Own implementation of a 2D vector class.
"""
from __future__ import annotations

import numbers
from functools import total_ordering
from math import sqrt
from typing import SupportsFloat
from typing import Union


@total_ordering
class Vector2D:
    """Vector2D class to perform simple vector operations."""

    def __init__(self, x: SupportsFloat = 0, y: SupportsFloat = 0) -> None:
        """Create a vector with the given x and y values.

        Args:
            x (SupportsFloat, optional): x-Value. Defaults to 0.
            y (SupportsFloat, optional): y-Value. Defaults to 0.

        Raises:
            TypeError: If x or y are not a number.
        """
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError("You must pass in int/float values for x and y!")

    def __call__(self) -> str:
        """Callable for the vector representation.

        Returns:
            str: The representation of the vector.
        """
        print("Calling the __call__ function!")
        return self.__repr__()

    def __repr__(self) -> str:
        """Return the vector representation.

        Returns:
            str: The representation of the vector.
        """
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self) -> str:
        """The vector as a string.

        Returns:
            str: The vector as a string.
        """
        return f"({self.x}, {self.y})"

    def __bool__(self) -> bool:
        """Return the truth value of the vector.

        Returns:
            bool: True, if the vector is not the Null-vector. False, else.
        """
        return bool(abs(self))

    def __abs__(self) -> float:
        """Return the length (magnitude) of the vector.

        Returns:
            float: Length of the vector.
        """
        return sqrt(self.x**2.0 + self.y**2.0)

    def check_vector_types(self, vector: object) -> None:
        """Check if the vector is an instance of the Vector2D class.

        Args:
            vector (object): A vector.

        Raises:
            TypeError: If vector is not an instance of the Vector2D class.
        """
        if not isinstance(self, Vector2D) or not isinstance(vector, Vector2D):
            raise TypeError(
                "You have to pass in two instances of the vector class!"
            )

    def __eq__(self, other_vector: object) -> bool:
        """Check if the vectors have the same values.

        Args:
            other_vector (object): Other vector (rhs)

        Returns:
            bool: True, if the both vectors have the same values. False, else.
        """
        self.check_vector_types(other_vector)
        is_equal = False
        if isinstance(other_vector, Vector2D):
            if self.x == other_vector.x and self.y == other_vector.y:
                is_equal = True
        return is_equal

    def __lt__(self, other_vector: Vector2D) -> bool:
        """Check if the self is less than the other vector.

        Args:
            other_vector (Vector2D): Other vector (rhs).

        Returns:
            bool: True, if the self is less than the other vector. False, else.
        """
        self.check_vector_types(other_vector)
        is_less_than = False
        if abs(self) < abs(other_vector):
            is_less_than = True
        return is_less_than

    def __add__(self, other_vector: Vector2D) -> Vector2D:
        """Returns the additon vector of the self and the other vector.

        Args:
            other_vector (Vector2D): Other vector (rhs).

        Returns:
            Vector2D: The additon vector of the self and the other vector.
        """
        self.check_vector_types(other_vector)
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector: Vector2D) -> Vector2D:
        """Return the subtraction vector of the self and the other vector.

        Args:
            other_vector (Vector2D): Other vector (rhs).

        Returns:
            Vector2D: The subtraction vector of the self and the other vector.
        """
        self.check_vector_types(other_vector)
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(
        self, other: Union[SupportsFloat, Vector2D]
    ) -> Union[SupportsFloat, Vector2D]:
        """Return the multiplication of self and the other vector/number.

        Args:
            other (Union[SupportsFloat, Vector2D]): Other vector or scaler
                value (rhs)

        Raises:
            TypeError: Not int/float passed in.

        Returns:
            Union[SupportsFloat, Vector2D]: The multiplication of self and other.
        """
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, numbers.Real):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError(
                "You must pass in a vector or an int/float number!"
            )

    def __truediv__(self, other: SupportsFloat) -> Vector2D:
        """Return the multiplication of self and the other vector/number.

        Args:
            other: Other vector or scaler value (rhs).

        Raises:
            ValueError: Division by zero.
            TypeError: Not int/float passed in.

        Returns:
            SupportsFloat: The multiplication of self and the other vector/number.
        """
        if isinstance(other, numbers.Real):
            if other != 0.0:
                return Vector2D(self.x / other, self.y / other)
            else:
                raise ValueError("You cannot divide by zero!")
        else:
            raise TypeError("You must pass in an int/float value!")
