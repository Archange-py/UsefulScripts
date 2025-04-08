"""
Script containing the cesar encryption function, created following a NSI exercise.
"""


def caesar_cipher(message: str, offset: int) -> str:
    """A function for cesar encryption and decryption.

    Args:
        message (str): The original or encrypted message.
        offset (int): A positive or negative number indicating the number of shifts to obtain the corresponding letter.

    Returns:
        str: Le message en clair ou chiffré.
    """
    chiffrement: dict[str, str] = {
        l:c for l, c in zip([chr(i) for i in range(65, 91)], [chr(65 + (i + offset)%26) for i in range(26)])
    }

    hidden = "".join(
        chiffrement[l] if 65 <= ord(l) <= 90 else l for l in message
    )

    return hidden
