"""
Script contenant une classe faisant office de générateur infini.
"""


from collections import abc

from typing import Any


class Cursor(abc.Iterator):
    """Classe d'un itérateur infini incluant les changements de directions."""
    def __init__(self, *args: tuple[Any], default: Any = ''):
        """Initialisation de la classe.

        Args:
            args (tuple[Any]): Une liste de départ contenant tout les éléments sur lequel le curseur bouclera à l'infini dessus.
            default (str, optional): L'élément de depart qui déterminera où l'itération commencera. Defaults to ''.
        """
        self.sens = 'R'
        self.args = args
        self.default = default

    def __next__(self):
        """Surcharge de la méthode spéciale __next__.

        Returns:
            Any: Renvoie le prochain élément contenu dans la liste args.
        """
        self.N += 1 if self.sens == "R" else -1
        self.check()
        self.curs = self.args[self.N]

        return self.curs

    def __iter__(self):
        """Surcharge de la méthode spéciale __iter__.

        Returns:
            self: se retourne soit même
        """
        self.curs = self.default if self.default != ""  else self.args[-1]
        self.N = self.args.index(self.default) if self.default != ""  else -1

        return self

    def check(self):
        """Méthode mettant à jour l'attribut N suivant deux conditions."""
        if self.N > len(self.args)-1:
            self.N = 0
        elif self.N < 0:
            self.N = len(self.args)-1
