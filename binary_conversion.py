"""
Example of a conversion function from binary to decimal.
"""


def convert(binary: 'Binary', /) -> 'Decimal': # type: ignore
    """Function for converting a binary number to an integer.

    Args:
        binary (int | str): Numbers in base 2 (ex: 1010).

    Raises:
        TypeError: Returns an error if the given number is not binary.

    Returns:
        int: The number in base 10.
    """
    binary: str = str(binary)
    decimal: int = 0

    if any([q != '0' and q != '1' for q in binary]):
        raise TypeError("Le nombre en argument doit absolument être composé que de '0' et de '1'.")

    for q in range(len(binary)):
        decimal += int(binary[-q-1]) * 2**q

    return decimal
