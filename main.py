a={
    'alphabet':['0','1'],
    'state':['a','b','c','d'],
    'initialstate':['a'],
    'finalstate':['b'],
    'transition':[['a','0','a'],['a','1','b'],
                  ['b','1','c'],['c','0','d'],]
}


def epsilonAFN(a):
    print(a['transition'])
    for t in a['transition']:
        if 'e' in t:
            return 'C est un epsilon AFN'
    return 'Ce n est pas un epsilon AFN'

def is_AFN_or_AFD(a):
    table=[]
    if len(a["initialstate"])>1:
        return 'It s a AFN'
    for t in a['transition']:
        print(t)
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
"""""
class AFD:
    def __init__(self, etats, alphabet, transitions, etat_initial, etats_finaux):
        self.etats = etats
        self.alphabet = alphabet
        self.transitions = transitions
        self.etat_initial = etat_initial
        self.etats_finaux = etats_finaux

    def minimiser(self):
        # Étape 1: Partition des états finaux et non finaux
        partition = [self.etats_finaux, list(set(self.etats) - set(self.etats_finaux))]
       
        # Étape 2: Répéter jusqu'à ce qu'il n'y ait plus de changements dans la partition
        while True:
            nouvelle_partition = []
            for groupe in partition:
                nouveaux_groupes = self.partitionner(groupe, partition)
                nouvelle_partition.extend(nouveaux_groupes)
            if nouvelle_partition == partition:
                break
            partition = nouvelle_partition

        # Étape 3: Construction du nouvel automate minimal
        nouveaux_etats = []
        nouveaux_transitions = []
        nouvel_etat_initial = self.etat_initial
        nouveaux_etats_finaux = []

        print("voici la partition",partition)

        for groupe in partition:
            print(partition)
            nouvel_etat = '-'.join(groupe)
            nouveaux_etats.append(nouvel_etat)
            if self.etat_initial in groupe:
                nouvel_etat_initial = nouvel_etat
            if any(etat in self.etats_finaux for etat in groupe):
                nouveaux_etats_finaux.append(nouvel_etat)

            for symbole in self.alphabet:
                arrivee = self.get_arrivee(groupe, symbole, partition)
                if arrivee:
                    nouveaux_transitions.append((nouvel_etat, symbole, arrivee))

        return AFD(nouveaux_etats, self.alphabet, nouveaux_transitions, nouvel_etat_initial, nouveaux_etats_finaux)

    def partitionner(self, groupe, partition):
        nouveaux_groupes = []
        for symbole in self.alphabet:
            arrivees = [self.get_arrivee(groupe, symbole, partition)]
            for groupe_exist in nouveaux_groupes:
                if groupe_exist[0] == arrivees[0]:
                    groupe_exist.append(symbole)
                    arrivees = []
                    break
            if arrivees:
                nouveaux_groupes.append(arrivees + [symbole])
        return [groupe_exist for groupe_exist in nouveaux_groupes if len(groupe_exist) > 1]

    def get_arrivee(self, groupe, symbole, partition):
        for etat in groupe:
            for transition in self.transitions:
                depart, s, arrivee = transition
                if depart == etat and s == symbole:
                    for groupe_exist in partition:
                        if arrivee in groupe_exist:
                            return '-'.join(groupe_exist)
        return None


# Exemple d'utilisation
alphabet = ['0', '1']
etats = ['A', 'B', 'C', 'D', 'E']
transitions = [
    ('A', '0', 'B'),
    ('A', '1', 'C'),
    ('B', '0', 'A'),
    ('B', '1', 'D'),
    ('C', '0', 'E'),
    ('C', '1', 'A'),
    ('D', '0', 'B'),
    ('D', '1', 'E'),
    ('E', '0', 'E'),
    ('E', '1', 'E')
]
etat_initial = 'A'
etats_finaux = ['C', 'D']

automate = AFD(etats, alphabet, transitions, etat_initial, etats_finaux)
automate_minimal = automate.minimiser()

print("Automate initial:")
print("États:", automate.etats)
print("Alphabet:", automate.alphabet)
print("Transitions:", automate.transitions)
print("État initial:", automate.etat_initial)
print("États finaux:", automate.etats_finaux)

print("\nAutomate minimal:")
print("États:", automate_minimal.etats)
print("Alphabet:", automate_minimal.alphabet)
print("Transitions:", automate_minimal.transitions)
print("État initial:", automate_minimal.etat_initial)
print("États finaux:", automate_minimal.etats_finaux)
"""


a={
    'alphabet':['0','1'],
    'state':['a','b','c','d'],
    'initialstate':['a'],
    'finalstate':['b'],
    'transition':[['a','0','a'],['a','1','b'],
                  ['b','1','c'],['c','0','d'],]
}
print(is_AFN_or_AFD(a))

