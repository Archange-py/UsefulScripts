"""
A small script resulting from a NSI exercise about perfect word.
"""


def is_perfect(string: str, /) -> tuple[int, int, bool]:
    """Consider the following two tables:
    {'a': 1, 'b': 2, 'c': 3, ..., 'z': 26} and {'A': 1, 'B': 2, 'C': 3, ..., 'Z': 26}

    For a given word (a string of non-empty characters consisting only of uppercase letters), we determine :
    - on the one hand, its concatenated alphabetic code, obtained by juxtaposing
    the text of the codes of each of its characters, and read as a single integer
    - and on the other hand, its summed code, which is the sum of the codes of each of its characters.

    This word is said to be “perfect” if the summed code divides the concatenated code.

    Args:
        string (str): The input character string.

    Returns:
        tuple[int, int, bool]: Returns a tuple containing its sum, its concatenated sum,
        and the test result respectively.
    """
    S: int = sum([ord(c) - 64 for c in string])
    P: int = int("".join([str(ord(c) - 64) for c in string]))

    return (S, P, not bool(P % S))
