from __future__ import annotations

from typing import Container
from typing import Iterable
from typing import Sized
from typing import Collection
from typing import Sequence
from typing import MutableSequence
from typing import Protocol


class SizedIterable(Protocol):
    def __len__(self):
        pass

    def __getitem__(self, i: int):
        pass


def iterate_over_length(obj: SizedIterable) -> None:
    for i in range(len(obj)):
        print(obj[i])


if __name__ == '__main__':
    values = [1, 2, 3]

    iterate_over_length(values)
