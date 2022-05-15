"""Own implementation of a 2D vector class."""
from __future__ import annotations

import numbers
from functools import total_ordering
from math import sqrt


@total_ordering
class Vector2D:
    """Vector2D class to perform simple vector operations."""

    def __init__(self, x=0, y=0):
        """Creates a vector with the given x and y values.

        Parameters
        ----------
        x : number
            x-Coordinate, by default 0
        y : number
            y-Coordinate, by default 0

        Raises
        ------
        TypeError
            If x or y are not a number.
        """
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError("You must pass in int/float values for x and y!")

    def __call__(self):
        """Callable for the vector to return its representation.

        Returns
        -------
        str
            The representation of the vector.
        """
        print("Calling the __call__ function!")
        return self.__repr__()

    def __repr__(self):
        """Returns the vector representation.

        Returns
        -------
        str
            The representation of the vector.
        """
        return f"vector.Vector2D({self.x}, {self.y})"

    def __str__(self):
        """Returns the vector as a string.

        Returns
        -------
        str
            The vector as a string.
        """
        return f"({self.x}, {self.y})"

    def __bool__(self):
        """Returns the truth value of the vector.

        Returns
        -------
        bool
            True, if the vector is not the Null-vector
            False, else
        """
        return bool(abs(self))

    def __abs__(self):
        """Returns the length (magnitude) of the vector.

        Returns
        -------
        float
            Length of the vector.
        """
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def check_vector_types(self, vector2):
        """Checks if the self and vector2 are an instance of the Vector2D class.

        Parameters
        ----------
        vector2 : Vector2D
            Other vector (right of the operator).

        Raises
        ------
        TypeError
            If self, or vector2 are not an instance of the Vector2D class.
        """
        if not isinstance(self, Vector2D) or not isinstance(vector2, Vector2D):
            raise TypeError(
                "You have to pass in two instances of the vector class!"
            )

    def __eq__(self, other_vector):
        """Check if the vectors have the same values.

        Parameters
        ----------
        other_vector : Vector2D
            Other vector (rhs)

        Returns
        -------
        bool
            True, if the both vectors have the same values.
            False, else.
        """
        self.check_vector_types(other_vector)
        is_equal = False
        if self.x == other_vector.x and self.y == other_vector.y:
            is_equal = True
        return is_equal

    def __lt__(self, other_vector):
        """Check if the self is less than the other vector.

        Parameters
        ----------
        other_vector : Vector2D
            Other vector (rhs)

        Returns
        -------
        bool
            True, if the self is less than the other vector.
            False, else.
        """
        self.check_vector_types(other_vector)
        is_less_than = False
        if abs(self) < abs(other_vector):
            is_less_than = True
        return is_less_than

    def __add__(self, other_vector):
        """Return the additon vector of the self and the other vector.

        Parameters
        ----------
        other_vector : Vector2D
            Other vector (rhs)

        Returns
        -------
        Vector2D
            The additon vector of the self and the other vector
        """
        self.check_vector_types(other_vector)
        x = self.x + other_vector.x
        y = self.y + other_vector.y
        return Vector2D(x, y)

    def __sub__(self, other_vector):
        """Returns the subtraction vector of the self and the other vector.

        Parameters
        ----------
        other_vector : Vector2D
            Other vector (rhs)

        Returns
        -------
        Vector2D
            The subtraction vector of the self and the other vector
        """
        self.check_vector_types(other_vector)
        x = self.x - other_vector.x
        y = self.y - other_vector.y
        return Vector2D(x, y)

    def __mul__(self, other):
        """Returns the multiplication of self and the other vector/number.

        Parameters
        ----------
        other : Vector2D or number
            Other vector or scaler value (rhs)

        Returns
        -------
        Vector2D
            The multiplication of self and the other vector (or number)
        """
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, numbers.Real):
            return Vector2D(self.x * other, self.y * other)
        else:
            raise TypeError(
                "You must pass in a vector or an int/float number!"
            )

    def __truediv__(self, other):
        """Returns the multiplication of self and the other vector/number.

        Parameters
        ----------
        other : Vector2D or number
            Other vector or scaler value (rhs)

        Returns
        -------
        Vector2D
            The multiplication of self and the other vector (or number)
        """
        if isinstance(other, numbers.Real):
            if other != 0.0:
                return Vector2D(self.x / other, self.y / other)
            else:
                raise ValueError("You cannot divide by zero!")
        else:
            raise TypeError("You must pass in an int/float value!")
