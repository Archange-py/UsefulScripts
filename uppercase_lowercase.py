"""
Script resulting from a NSI exercise containing simple utility
functions for handling uppercase and lowercase strings.
"""


def is_uppercase(*symbol: tuple[str], alone: bool = False) -> bool | tuple[bool]:
    """Test whether a character or string of characters is capitalized.

    Args:
        *symbol (tuple[str]): A character or a string of characters to test.
        alone (bool, optional): Returns a list of Booleans corresponding to the test for each character if enabled. Defaults to False.

    Returns:
        bool | tuple[bool]: Returns the test result as a Boolean.
    """
    cond = lambda char: ord("A") <= ord(char) <= ord("Z")
    results: list[bool] = [cond(char) for char in symbol]

    return results if alone else all(results)

def is_lowercase(*symbol: tuple[str], alone: bool = False) -> bool | tuple[bool]:
    """Test whether a character or string of characters is lowercase.

    Args:
        *symbol (tuple[str]): A character or a string of characters to test.
        alone (bool, optional): Returns a list of Booleans corresponding to the test for each character if enabled. Defaults to False.

    Returns:
        bool | tuple[bool]: Returns the test result as a Boolean.
    """
    cond = lambda char: ord("a") <= ord(char) <= ord("z")
    results: list[bool] = [cond(char) for char in symbol]

    return results if alone else all(results)

def uppercase(string: str, /) -> str:
    """Function that formats a character string so that all possible characters are capitalized.

    Args:
        string (str): The input character string.

    Returns:
        str: Returns the formatted character string.
    """
    return "".join([
        char if is_uppercase(char) else
        chr(ord(char) - 32) if is_lowercase(char) else 
        char for char in str(string)
    ])

def lowercase(string: str, /) -> str:
    """Function that formats a character string so that all possible characters are lowercase.

    Args:
        string (str): The input character string.

    Returns:
        str: Returns the formatted character string.
    """
    return "".join([
        char if is_lowercase(char) else
        chr(ord(char) + 32) if is_uppercase(char) else 
        char for char in str(string)
    ])
