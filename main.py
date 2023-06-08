a={
    'alphabet':['a'],
    'state':[1,2],
    'initialstate':[1],
    'finalstate':[2],
    'transition':[[1,'e',1],[1,'a',2],[2,'a',2]]
}
def epsilonAFN(a):
    print(a['transition'])
    for t in a['transition']:
        if 'e' in t:
            return 'C est un epsilon AFN'
    return 'Ce n est pas un epsilon AFN'

print(epsilonAFN(a))
