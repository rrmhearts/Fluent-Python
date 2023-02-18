from typing import Union

# def take_number(number: str | int | float):

def take_number(number: Union[str, int, float] ):

    if isinstance(number, str):
        try:
            return int(number)
        except ValueError:
            print(f"\t{number} is not a number")
    else:
        return int(number)


print(take_number('5'))
print(take_number('Not number'))
print(take_number(5))
print(take_number(5.1))
