"""
Example du fonctionnement de l'algorithme dit du tri à bulle, extrait du livre de Yan Le Cun
"""

from random import randint

def echange(tab,i,j):
  _tab = tab[j]
  tab[j] = tab[i]
  tab[i] = _tab
  return tab

def short(tab):
  for _ in range(len(tab)):
    for i in range(len(tab)):
      if i + 1 != len(tab) and int(tab[i+1]) < int(tab[i]):
          echange(tab,i+1,i)
  return tab

tab = [randint(0,100) for _ in range(20)]
print(short(tab))