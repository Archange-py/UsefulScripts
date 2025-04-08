"""Algorithme de compression sans perte mis au point par Huffman, notamment utilisé dans les fichiers zip."""

class Huffman:
  class TreeBin:
    class Noeud:
      def __init__(self,contenu=None,key=None,left=None,right=None): self.contenu,self.key,self.left,self.right = contenu,key,left,right
      def __repr__(self): return "{"+str(self.left)+","+str(self.right)+"}"
    class Feuille(Noeud):
      def __init__(self,*args,**kwargs): super().__init__(*args,**kwargs);del self.left,self.right
      def __repr__(self): return self.contenu
    def __init__(self,racine): self.racine = racine
  def __init__(self,chaine): self.chaine = chaine
  def __getitem__(self,char):
    if isinstance(char,str): return self.feuilles[char]
    elif isinstance(char,int): return [f for f in self.feuilles.values()][char]
  def __setitem__(self,char,value): self.feuilles[char] = value
  def __len__(self): return len(self.feuilles)
  @staticmethod  
  def count(chaine): return {char:chaine.count(char) for char in chaine}

  def _build_tree(self):
    noeuds = [Huffman.TreeBin.Feuille(c,k) for c,k in Huffman.count(self.chaine).items()]
    while len(noeuds) > 1:
      noeuds.sort(key=lambda x: x.key);noeuds.reverse()
      left,right = noeuds.pop(),noeuds.pop()
      noeuds.append(Huffman.TreeBin.Noeud(None,left.key+right.key,left,right))
    self.tree = Huffman.TreeBin(noeuds[0])

  def _encode(self):
    feuilles = []
    def _forward(noeud,code):
      if not hasattr(noeud,"left"): feuilles.append(noeud);noeud.encode = code
      else: _forward(noeud.left,code+"0");_forward(noeud.right,code+"1")
    _forward(self.tree.racine,"");return {feuille.contenu:feuille for feuille in feuilles}

  def zip(self):
    self._build_tree();self.feuilles = self._encode()
    return "".join([self[char].encode for char in self.chaine])

  def load(self,encode):
    N,c,s = self.tree.racine,0,""
    while c != len(encode):
      if hasattr(N,"left"):
        if int(encode[c]) == 0: N = N.left
        elif int(encode[c]) == 1: N = N.right
      else: s += N.contenu;N = self.tree.racine;continue
      c += 1
    return s + N.contenu

chaine = "les chaussettes de l archiduchesse sont elles seches et archiseches"
H = Huffman(chaine)
encode = H.zip()
decode = H.load(encode)
liste = [(feuille,feuille.encode) for feuille in H]
print(chaine);print(encode);print(decode);print(liste)