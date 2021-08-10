from my_lib import CONSTANT_VAR
from my_lib import my_function


my_float = 0.0


def main():
    my_int_value = 3
    my_bool = True
    my_function(my_int_value)
    print(CONSTANT_VAR)

    print(f"Dir:\n{dir(my_int_value)}")
    print(f"Globals:\n{globals()}")
    print(f"Locals:\n{locals()}")


if __name__ == '__main__':
    main()
