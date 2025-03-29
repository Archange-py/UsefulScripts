
class Curseur:
    """Classe d'un itérateur infini incluant les changements de directions
    """
    def __init__(self, *args, default=""):
        """Initialisateur de la classe

        Args:
            default (str, optional): élément qui déterminera où l'itération commence. Defaults to "".
        """
        self.args = args
        self.sens = "R"
        self.default = default

    def __next__(self):
        """Surcharge de la méthode spéciale __next__

        Returns:
            Any: renvoie le prochain élément contenu dans la liste args
        """
        self.N += 1 if self.sens == "R" else -1
        self.check()
        self.curs = self.args[self.N]
        return self.curs

    def __iter__(self):
        """Surcharge de la méthode spéciale __iter__

        Returns:
            self: se retourne soit même
        """
        self.curs = self.default if self.default != ""  else self.args[-1]
        self.N = self.args.index(self.default) if self.default != ""  else -1
        return self
    
    def check(self):
        """Méthode mettant à jour l'attribut N suivant deux conditions
        """
        if self.N > len(self.args)-1: self.N = 0
        elif self.N < 0: self.N = len(self.args)-1
