"""
Script python d'une fonction pour deviner le nombre de l'utilisateur - NSI

Groupe: Davoud, Mattéo, Vincent

Algorithme du jeu 'plus bas, plus haut'

Indiquer à l'utilisateur de choisir un nombre entier positif ou négatif
borne_1 ← 0
borne_2 ← None
compteur ← 100
Tant que True est vrai faire:
    response ← Demander à l'utilisateur la position de son nombre par rapport à borne_1
    Si response = '1':
        On sort de la boucle
    Sinon si response = '-1':
        borne_2 ← borne_1
        compteur ← compteur ** 2
        borne_1 ← borne_1 - compteur
    Sinon si response = '0':
        Le nombre borne_1 est trouvé
        On sort de la fonction
Si borne_2 est None:
    borne_2 ← 100
    Tant que True est vrai faire:
        response ← Demander à l'utilisateur la position de son nombre par rapport à borne_2
        Si response = '1':
            borne_1 ← borne_2
            borne_2 ← borne_2 ** 2
        Sinon si response = '-1':
            On sort de la boucle
        Sinon si response = '0':
            Le nombre borne_2 est trouvé
            On sort de la fonction
Tant que True est vrai faire:
    milieu ← round((borne_1 + borne_2) / 2)
    response ← Demander à l'utilisateur la position de son nombre par rapport à milieu
    Si response = '1':
        borne_1 ← milieu
    Sinon si response = '-1':
        borne_2 ← milieu
    Sinon si response = '0':
        Le nombre milieu est trouvé
        On sort de la fonction
    Si borne_1 + 1 = borne_2:
        Le nombre milieu est trouvé
        On sort de la fonction
"""

def guess(accroissement: int = 2, /):
    """Fonction permettant de deviner, au fur et à mesure des questions
    un nombre entier positif ou négatif. Elle n'utilise
    qu'une seule et même question: 'Indiquez la position de
    votre nombre par rapport à x.' a partir duquel elle regarde si le nombre
    est supérieur (1), inférieur (-1), ou égal (0) à x.

    Args:
        accroissement (int, optional): Le nombre qui sera demandé comme
            point de départ pour la deuxième borne, puis mis à l'exposant de 2 
            si il est inférieur au nombre choisis par l'utilisateur. Par défaut à 100.

    Raises:
        Exception: Provoque une exception si le paramètre accroissement
            est inférieur à 2.
    """
    find = lambda nbr: print(f"Votre nombre est {nbr}.") # Pour éviter une répétition exubérante
    ask = lambda nbr: input(f"Indiquez la position de votre nombre par rapport à {nbr} : ") # idem

    def show(borne_1: str, borne_2: str, char_1: str = '-', char_2: str = '^', char_3: str = ' ', n1: int = 5, n2: int = 15):
        """Fonction pour afficher une droite horizontale comprenant les deux points
        aux abscisses des deux bornes respectives.

        Args:
            borne_1 (str): La première borne de recherche.
            borne_2 (str): Le deuxième borne de recherche
            char_1 (str, optional): Le caractère représentant la ligne. Par défaut à '-'.
            char_2 (str, optional): Le caractère représentant le point. Par défaut à '^'.
            char_3 (str, optional): Le caractère représentant les espace vide. Par défaut à ' '.
            n1 (int, optional): L'espacement de la ligne à gauche et à droite après et avant les points. Par défaut à 5.
            n2 (int, optional): L'espacement de la ligne entre les deux points. Par défaut à 15.
        """
        length: int = max(len(borne_1), len(borne_2)) # on regarde la longueur la plus grande pour chacune des deux bornes
        print('\n' + n1*char_3 + borne_1.center(length, ' ') + n2*char_3 + borne_2.center(length, ' ') + n1*char_3 \
              + '\n' + n1*char_1 + char_2.center(length, char_1) + n2*char_1 + char_2.center(length, char_1) + n1*char_1)

    if accroissement < 2: # parce que 1**2 vaudra toujours 1
        raise Exception(f"Le paramètre 'accroissement' doit être supérieur ou égale à 2: {accroissement}")

    print("Choisissez un nombre entier, qu'il soit positif ou négatif.")
    print("\nq & n: exit\n\n-1: inférieur\n0: égal\n1: supérieur")
    show('?', '?') # on affiche la droite

    borne_1: int = 0 # la première borne
    borne_2: str = '?'
    N: int = accroissement # compteur
    while True:
        match ask(borne_1): # on regarde les différentes possibilités
            case '1': break # on a trouvé la première borne
            case '-1':
                borne_2 = borne_1
                N **= 2
                borne_1 -= N
            case '0': # on a trouvé le nombre
                find(borne_1)
                return
            case 'q' | 'n': return
            case _: pass
    show(str(borne_1), str(borne_2)) # on affiche la droite

    if borne_2 == '?':
        borne_2: int = accroissement # la deuxième borne
        while True:
            match ask(borne_2): # on regarde les différentes possibilités
                case '-1': break # on a trouvé la deuxième borne
                case '1':
                    borne_1 = borne_2
                    borne_2 **= 2
                case '0': # on a trouvé le nombre
                    find(borne_2)
                    return
                case 'q' | 'n': return
                case _: pass
        show(str(borne_1), str(borne_2)) # on affiche la droite

    while True:
        milieu: int = round((borne_1 + borne_2) / 2)

        match ask(milieu): # on regarde les différentes possibilités
            case '1':
                borne_1 = milieu # on réduit l'espacement des deux bornes
            case '-1':
                borne_2 = milieu # on réduit l'espacement des deux bornes
            case '0': # on a trouvé le nombre
                find(milieu)
                return
            case 'q' | 'n': return
            case _: pass

        if borne_1 + 1 == borne_2: # on vérifie que les deux bornes ne sont pas les mêmes
            find(milieu) # sinon on l'a trouvé
            return

        show(str(borne_1), str(borne_2)) # on affiche la droite

guess(3)