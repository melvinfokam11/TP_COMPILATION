a={
    'alphabet':['0','1'],
    'state':['a','b','c','d'],
    'initialstate':['a'],
    'finalstate':['b'],
    'transition':[['a','0','a'],['a','0','b'],['a','1','a'],
                  ['b','1','c'],['c','0','d'],]
}
def epsilonAFN(a):
    print(a['transition'])
    for t in a['transition']:
        if 'e' in t:
            return 'C est un epsilon AFN'
    return 'Ce n est pas un epsilon AFN'

print(epsilonAFN(a))

def is_AFN_or_AFD(a):
    table=[]
    for t in a['transition']:
        chain=''.join(t)
        table.append(chain)
    print(table)
    for state in a['state']:
        for alpha in a['alphabet']:
            val=0
            for word in table:
                if state+alpha in word:
                   val=val+1
            #print(state+alpha,' ',val)
            if(val>1):
                return 'It is a AFN'
    return 'It is a AFD'
"""""
def is_AFD(a):
    table=[]
    for t in a['transition']:
        chain=''.join(t)
        table.append(chain)
    print(table)
    for state in a['state']:
        for alpha in a['alphabet']:
            val=0
            for word in table:
                if state+alpha in word:
                   val=val+1
            #print(state+alpha,' ',val)
            if(val>1):
                return 'It is not a AFD'
    return 'It is a AFD'
"""

print(is_AFN_or_AFD(a))

