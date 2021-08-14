from my_lib import GLOBAL_MYLIB_VAR


global_int = 0.0


def fun():
    a = 2


def main():
    if True:
        b = 2
    local_int = 3
    print(local_int)
    print(global_int)
    print(GLOBAL_MYLIB_VAR)

    print(f"Locals:\n{locals()}")
    print(f"Globals:\n{globals()}")


if __name__ == '__main__':
    main()
