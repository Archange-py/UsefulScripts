
def is_perfect(string):
    S, P = sum([ord(c) - 64 for c in string]), int("".join([str(ord(c) - 64) for c in string]))
    return (S, P, not bool(P%S))

print(is_perfect("PAUL"))
print(is_perfect("ALAIN"))

assert is_perfect("PAUL") == (50, 1612112, False)
assert is_perfect("ALAIN") == (37, 1121914, True)
