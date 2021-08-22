from __future__ import annotations

from typing import NewType
from typing import TypeVar
from typing import Union


UserId_NT = NewType('UserId_NT', str)
UserId_TV = TypeVar('UserId_TV', str, bytes)
UserId = Union[str, bytes]


def print_text1(text: UserId_NT) -> None:
    print(text)


def print_text2(text: UserId_TV) -> None:
    print(text)


def print_text3(text: UserId) -> None:
    print(text)


def main():
    u1 = 'hello'
    u2 = b'hello'

    # print_text1(u1)  # error
    # print_text1(u2)  # error
    print_text1(UserId_NT(u1))  # okay

    print_text2(u1)
    print_text2(u2)

    print_text3(u1)
    print_text3(u2)


if __name__ == '__main__':
    main()
