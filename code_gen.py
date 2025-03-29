
def translate(string):
    if len(string) % 3:
        raise TypeError

    liste = [string[i]+string[i+1]+string[i+2] for i in range(0, len(list(string))-2, 3)]
    genetic_code = {
        "UUU": "Phénylalanine", "UUC": "Phénylalanine", "UUA": "Leucine", "UUG": "Leucine", "CUU": "Leucine", "CUC": "Leucine", "CUA": "Leucine", "CUG": "Leucine", "AUU": "Isoleucine", "AUC": "Isoleucine", "AUA": "Isoleucine", "AUG": "Méthionine", "GUU": "Valine", "GUC": "Valine", "GUA": "Valine", "GUG": "Valine", "UCU": "Sérine", "UCC": "Sérine", "UCA": "Sérine", "UCG": "Sérine", "CCU": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline", "ACU": "Thréonine", "ACC": "Thréonine", "ACA": "Thréonine", "ACG": "Thréonine", "GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine", "UAU": "Tyrosine", "UAC": "Tyrosine", "UAA": "Stop", "UAG": "Stop", "CAU": "Histidine", "CAC": "Histidine", "CAA": "Glutamine", "CAG": "Glutamine", "AAU": "Asparagine", "AAC": "Asparagine", "AAA": "Lysine", "AAG": "Lysine", "GAU": "Acide aspartique", "GAC": "Acide aspartique", "GAA": "Acide glutamique", "GAG": "Acide glutamique", "UGU": "Cystéine", "UGC": "Cystéine", "UGA": "Stop", "UGG": "Tryptophane", "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine", "AGU": "Sérine", "AGC": "Sérine", "AGA": "Arginine", "AGG": "Arginine", "GGU": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine"
    }

    return [genetic_code[seq] for seq in liste]

print(translate("AAGUCGAUCGUGACUGCAUGCUCGUGACGUGCUAGCUGAUGCUGCUAGUCGUAGUGCUAGCUCGUAGCUAGCGUGAUGCUAGAA"))