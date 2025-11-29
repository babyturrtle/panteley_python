"""A program that prints different things depending on the input.

A number, a name, or a numeric array are accepted at the input.

If the entered number is greater than 7, then “Hello” is printed out.
If the entered name matches “John”, then “Hello, John” is printed out, otherwise "There is no such name" is printed out.
If a numeric array is entered, then only the elements of that array that are the multiples of 3 are printed out.
"""

from typing import Any, List

 
def custom_number_print(number: int) -> None:
    """Compares the number to 7 and prints 'Hello' if the number is greater than 7.
    
    Args:
        number: Any integer.
    """

    if number > 7:
        print("Hello")


def custom_string_print(name: str) -> None:
    """Compares the name to 'John' and prints 'Hello, John' if the name is 'John'.
    
    Args:
        name: Any string text.
    """

    if name == "John":
        print("Hello, John")

    else:
        print("There is no such name")


def custom_array_print(array: List[int]) -> None:
    """Looks for array elements that are the multiples of 3 and prints out an array composed of them.
    
    Args:
        array: A list with integer values.
    """

    return_array = [element for element in array if element % 3 == 0]

    print(return_array)


def main() -> None:
    """Main function of the program."""

    consent = 'yes'

    while(consent == 'yes'):

        input_value = input("Enter a number, a name, or a comma-separated numeric array: ")

        if ',' in input_value:
            try:
                input_value = [int(element) for element in input_value.split(',')]
            except ValueError as e:
                pass
        else:
            try:
                input_value = int(input_value)
            except ValueError as e:
                pass

        if isinstance(input_value, int):
            custom_number_print(input_value)
        if isinstance(input_value, str):
            custom_string_print(input_value)
        if isinstance(input_value, list):
            custom_array_print(input_value)

        consent = input("Do you want to run the program again? Type 'yes' or 'no': ")


if __name__ == '__main__':
    main()
