from __future__ import annotations

from typing import Any
from typing import Collection
from typing import Container
from typing import Iterable
from typing import MutableSequence
from typing import Protocol
from typing import Sequence
from typing import Sized


class SizedMutableIterable(Protocol):
    def __len__(self):
        pass

    def __getitem__(self, i: int):
        pass

    def __setitem__(self, i: int, v: Any):
        pass


def iterate_over_length(obj: SizedMutableIterable) -> None:
    for i in range(len(obj)):
        obj[i] = i**2
        print(obj[i])


if __name__ == '__main__':
    values = [1, 2, 3]

    iterate_over_length(values)
