"""
Example d'une fonction de conversion, extrait du livre de ...
"""

def I(b: bin) -> int:
  """Fonction de conversion d'un nombre binaire vers un nombre entier

  Args:
      b (bin): le nombre binaire en base 2

  Raises:
      TypeError: renvoie une erraur si le nombre donné n'est pas binaire

  Returns:
      int: le nombre en base 10
  """
  b, n = str(b), 0
  for q in b:
    if q != "0" and q != "1":
      raise TypeError
  for q in range(len(b)):
    n += int(b[-q-1])*(2**q)
  return n
