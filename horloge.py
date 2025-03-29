
class Duree:
  """Classe simulant un horloge numérique avec les minutes et les secondes"""
  def __init__(self, minutes: int = 0, secondes: int = 0):
    """Initialisateur de la classe

    Args:
        minutes (int, optional): le nombre de minutes. Defaults to 0.
        secondes (int, optional): le nombre de secondes. Defaults to 0.
    """
    self.minutes = minutes
    self.secondes = secondes

  def __str__(self) -> str:
    """Surcharge de l'affichage de la classe

    Returns:
        str: une chaine de caratère contenant les minutes et les secondes
    """
    return str(self.minutes)+":"+str(self.secondes)
    
  def __add__(self, objet: int):
    """Surcharge de l'addition

    Args:
        objet (int): le nombre de secondes

    Returns:
        Duree: une nouvelle instance de la classe Duree
    """
    nouvelle_duree = Duree()
    nouvelle_duree.minutes = self.minutes
    nouvelle_duree.secondes = self.secondes
    nouvelle_duree.secondes += objet
    if nouvelle_duree.secondes >= 60:
      nouvelle_duree.minutes += nouvelle_duree.secondes//60
      nouvelle_duree.secondes = nouvelle_duree.secondes%60
    return nouvelle_duree

D1 = Duree(5,30)
print(D1+125)