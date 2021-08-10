from my_lib import POWER_OF
from my_lib import my_function


def main():
    my_int_value = 3
    # my_bool = True
    # my_float = 2.5
    my_function(my_int_value)

    print(f"Dir:\n{dir()}")
    print(f"Globals:\n{globals()}")
    print(f"Locals:\n{locals()}")


if __name__ == '__main__':
    main()
