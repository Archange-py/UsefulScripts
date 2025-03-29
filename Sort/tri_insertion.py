
def permute(L, a, b):
    if not (a < b < len(L)):
        raise TypeError

    return L[:a] + [L[b]] + L[a+1:b] + [L[a]] + L[b+1:]

L = list(range(15))

print(permute(L, 3, 6))

L = [5, 7, 9, 2, 4]

print(permute(L, 1, 3))