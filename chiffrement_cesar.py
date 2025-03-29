
def cesar(message, decalage):
    dico = {l:c for l, c in zip([chr(i) for i in range(65, 91)], [chr(65 + (i + decalage)%26) for i in range(26)])}
    cript = "".join(dico[l] if 65 <= ord(l) <= 90 else l for l in message)
    return cript

print(cesar("HELLO WORLD!", 5))
print(cesar("MJQQT BTWQI!", -5) )

assert cesar('HELLO WORLD!', 5) == 'MJQQT BTWQI!'
assert cesar('MJQQT BTWQI!', -5) == 'HELLO WORLD!'

assert cesar('BONJOUR LE MONDE !', 23) == 'YLKGLRO IB JLKAB !'
assert cesar('YLKGLRO IB JLKAB !', -23) == 'BONJOUR LE MONDE !'