from my_lib import GLOBAL_MYLIB_VAR


my_global_int = 0.0


def main():
    my_local_int = 3
    print(GLOBAL_MYLIB_VAR)

    print(f"Locals:\n{locals()}")
    print(f"Globals:\n{globals()}")


if __name__ == '__main__':
    main()
