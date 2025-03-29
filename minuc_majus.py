
minuscule = lambda char: "".join([c if ord("a") <= ord(c) <= ord("z") else chr(ord(c) + 32) if ord("A") <= ord(c) <= ord("Z") else c for c in str(char)])
majuscule = lambda char: "".join([c if ord("A") <= ord(c) <= ord("Z") else chr(ord(c) - 32) if ord("a") <= ord(c) <= ord("z") else c for c in str(char)])

word = "Hello Word!"

print(word)
print(minuscule(word))
print(majuscule(word))
