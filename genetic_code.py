"""
A script containing a single function for an SVT exercise in NSI.
"""


GENETIC_CODE: dict[str, str] = {
    "UUU": "Phénylalanine", "UUC": "Phénylalanine", "UUA": "Leucine", "UUG": "Leucine", "CUU": "Leucine", "CUC": "Leucine", "CUA": "Leucine", "CUG": "Leucine", "AUU": "Isoleucine", "AUC": "Isoleucine", "AUA": "Isoleucine", "AUG": "Méthionine", "GUU": "Valine", "GUC": "Valine", "GUA": "Valine", "GUG": "Valine", "UCU": "Sérine", "UCC": "Sérine", "UCA": "Sérine", "UCG": "Sérine", "CCU": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline", "ACU": "Thréonine", "ACC": "Thréonine", "ACA": "Thréonine", "ACG": "Thréonine", "GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine", "UAU": "Tyrosine", "UAC": "Tyrosine", "UAA": "Stop", "UAG": "Stop", "CAU": "Histidine", "CAC": "Histidine", "CAA": "Glutamine", "CAG": "Glutamine", "AAU": "Asparagine", "AAC": "Asparagine", "AAA": "Lysine", "AAG": "Lysine", "GAU": "Acide aspartique", "GAC": "Acide aspartique", "GAA": "Acide glutamique", "GAG": "Acide glutamique", "UGU": "Cystéine", "UGC": "Cystéine", "UGA": "Stop", "UGG": "Tryptophane", "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine", "AGU": "Sérine", "AGC": "Sérine", "AGA": "Arginine", "AGG": "Arginine", "GGU": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine"
}

def translate(string: str, /) -> list[str]:
    """A function for converting a genetic code string into
    a set of names corresponding to the acids.

    Args:
        string (str): A character string consisting of a three-letter code from among A, G, U and T.

    Raises:
        TypeError: Causes an error if the total length of the string is not a multiple of three.

    Returns:
        list[str]: Returns a list with the different acid names corresponding to the associated genetic codes.
    """
    modulo_three: int = len(string) % 3

    if modulo_three:
        raise TypeError(f"The string in argument must be a multiple of 3. You must add {3 - modulo_three} letter(s).")

    tab: list[str] = [string[i]+string[i+1]+string[i+2] for i in range(0, len(list(string))-2, 3)]

    return [GENETIC_CODE[seq] for seq in tab]
