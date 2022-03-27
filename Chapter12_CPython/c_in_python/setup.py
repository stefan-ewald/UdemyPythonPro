from distutils.core import Extension
from distutils.core import setup


def main() -> None:
    setup(name="math_cpython",
          version="1.0.0",
          description="CPython module in Python",
          ext_modules=[Extension("math_cpython", ["mathmodule.c"])])


if __name__ == "__main__":
    main()
