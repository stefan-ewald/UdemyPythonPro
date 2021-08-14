from distutils.core import setup, Extension


def main() -> None:
    setup(name="add",
          version="1.0.0",
          description="CPython module in Python",
          ext_modules=[Extension("add", ["mathmodule.c"])])


if __name__ == "__main__":
    main()
