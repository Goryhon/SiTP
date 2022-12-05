from grammar import Grammar as Gr
from MINE import unreachableSymbols

g = Gr(
    {'A', 'B', 'C','D'},
    {'a', 'b', 'c', 'b'},
    {'B': ['ab'], 'A':['bBc', 'bb']},
    'A'
)
print(g.N)
print(g.T)
print(g.P)
print(g.S)
print()
print(unreachableSymbols(g).N)
print(unreachableSymbols(g).T)
print(unreachableSymbols(g).P)
print(unreachableSymbols(g).S)


