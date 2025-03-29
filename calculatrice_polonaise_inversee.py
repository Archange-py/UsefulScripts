"""
Implémentation de deux algorithme permettant respectivement de passer d'une forme de calcul normal
à une notation polonaise inverse, puis de résoudre cette dernière, extrait du livre: 15 énigmes
ludiques pour se perfectionner en programmation python
"""

OPERATEURS = ["+","-","*","/"]

def shunting_yard(n: str) -> str:
  """Algorithme shunting yard

  Args:
      n (str): chaîne de caractères contenant la notation de calcul normale

  Returns:
      str: renvoi la chaîne de caractères correspondant à la notation polonaise inversé
  """
  print("Input:",n)
  yard,output = [],[]
#  n = " ".join(char for char in list(n))
  _n = n.split()
  for char in _n:
    if char.isdigit(): output.append(char)
    elif char in OPERATEURS:
      for c in yard:
        if c in OPERATEURS and c > char:
          yard.pop(yard.index(c))
          output.append(c)
      yard.append(char)
    elif char == "(": yard.append(char)
    elif char == ")":
      for c in yard:
        if c in OPERATEURS:
          yard.pop(yard.index(c))
          output.append(c)
        elif c == "(":
          yard.pop(yard.index(c))
          break
  for c in yard:
    if c in OPERATEURS:
      yard.pop(yard.index(c))
      output.append(c)
  for i,c in enumerate(output):
    if c in OPERATEURS and i != len(output)-1 and output[i+1] in OPERATEURS:
      oper1 = c
      output[i] = output[i+1]
      output[i+1] = oper1
  print("Not. Pol. Inv.:"," ".join(char for char in output))
  return " ".join(char for char in output)

def calculatrice(n : str) -> float:
  """Algorithme pour résoudre un calcul en notation polonaise inversé

  Args:
      n (str): chaîne de caractères correspondant à la notation polonaise inversé

  Returns:
      float: renvoi le résultat du calcul
  """
  not_polonaise = shunting_yard(n)
  liste = not_polonaise.split()
  for oper in [char for char in not_polonaise if char in OPERATEURS]:
    i0 = liste.index(oper)
    n1,n2 = liste[i0-1],liste[i0-2]
    i1,i2 = liste.index(n1),liste.index(n2)
    liste.pop(i0);liste.pop(i1);liste.pop(i2)
    if oper == "*": calcul = float(n2) * float(n1);print(n2,"*",n1,"=",calcul)
    elif oper == "/": calcul = float(n2) / float(n1);print(n2,"/",n1,"=",calcul)
    elif oper == "+": calcul = float(n2) + float(n1);print(n2,"+",n1,"=",calcul)
    elif oper == "-": calcul = float(n2) - float(n1);print(n2,"-",n1,"=",calcul)
    liste.insert(i2,str(calcul))
  return liste[0]

def _calculatrice(n: str) -> float:
  """Algorithme pour résoudre un calcul en notation polonaise inversé, version corrigé

  Args:
      n (str): chaîne de caractères correspondant à la notation polonaise inversé

  Returns:
      float: renvoi le résultat du calcul
  """
  liste,pile = shunting_yard(n).split(),[]
  for char in liste:
    if char.isdigit(): pile.append(char)
    elif char in OPERATEURS:
      b,a = eval(str(pile.pop())),eval(str(pile.pop()))
      if char == "*": pile.append(a*b)
      elif char == "/": pile.append(a/b)
      elif char == "+": pile.append(a+b)
      elif char == "-": pile.append(a-b)
  return pile[0]

#print("Output:", calculatrice("4 * ( 1 + 2 ) - 3"))
#print("Output:", calculatrice("( 48 + 56 ) * ( 7 / 11 )"))
print("Output:", calculatrice("( 48 + 56 ) * ( 7 / 11 )"))