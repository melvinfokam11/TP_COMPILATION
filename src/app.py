from projet import*
from automatelib import *
 
alphabet = ['a','b']
epsilons=['e']
states  = [1,2,3,4]
initials = [1]
finals = [2]
transitions = [ (1,'a',1),(1,'a',3), (1,'b',2),(2,'b',1),(2,'b',4),(4,'b',2),(4,'a',4),(3,'b',2),(3,'a',4)]

z={
    'alphabet':alphabet,
    'state':states,
    'initialstate':initials,
    'finalstate':finals,
    'transition':transitions
}

print("Entrer le nombre de symbole de l'alphabet")
nb_al=int(input())
alphabet=[]
for i in range(nb_al):
    print('Entrer le symbole',i+1)
    s=input()
    alphabet.append(s)

print("Entrer le nombre d' etats")
nb_state=int(input())
states=[]
for i in range(nb_state):
    print('Entrer l etat',i+1)
    s=int(input())
    states.append(s)

print("Entrer le nombre d'etats initiaux ")
nb_state_i=int(input())
initials=[]
for i in range(nb_state_i):
    print('Entrer l etat initial ',i+1)
    s=int(input())
    initials.append(s)



print("Entrer le nombre d'etats finaux ")
nb_state_f=int(input())
finals=[]
for i in range(nb_state_f):
    print('Entrer l etat final ',i+1)
    s=int(input())
    finals.append(s)


a = automaton(alphabet = alphabet,epsilons=epsilons, states  = states,initials = initials, finals =finals,
transitions = transitions)
b=automaton(alphabet = alphabet,epsilons=epsilons, states  = states,initials = initials, finals =finals,
transitions = transitions)

def App():
    print('Menu')
    print("1-Donner la nature de l'automate\n2-Determiniser\n3-Minimiser l'automate\n5-Le langage de commentaire")
    question=int(input("Entrer la valeur de la question "))
    match question:
        case 1:
            print("Donner la nature de cet automate")
            nature_auto(z)
        case 2:
            determiniser(a)
            test=determiniser(a)
            print(test._alphabet)
            print(test._initial_states)
            print(test._states)
            print(test._adjacence)
            print(test._final_states)
        case 3:
            minimiser(a)
            test=determiniser(a)
            print(test._alphabet)
            print(test._initial_states)
            print(test._states)
            print(test._adjacence)
            print(test._final_states)
        case 5:
            print("Vous avez choisi le langage commentaire")
            texte = """acd /*abc%*/babA*/of"""
            texte=input("Entrer les commentaires ")
            commentaires = reconnaître_commentaires(texte)
            for commentaire in commentaires:
                print(commentaire)
        case _:
            print('Impossible')

App()

