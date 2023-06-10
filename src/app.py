from projet import*
from automatelib import *
from question2 import*
from question3 import *

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

print("Welcome\n")
print("-------------------------------")
print("Entrer le nombre de symbole de l'alphabet")
print("-------------------------------")
nb_al=int(input())
alphabet=[]
for i in range(nb_al):
	print('Entrer le symbole',i+1)
	s=input()
	alphabet.append(s)
print("Voici l'alphabet ",alphabet)
print("-------------------------------")
print("Entrer le nombre d' etats")
print("-------------------------------")
nb_state=int(input())
states=[]
for i in range(nb_state):
	print('Entrer l etat',i+1)
	s=int(input())
	states.append(s)
print("Voici les etats ",states)
print("-------------------------------")
print("Entrer le nombre d'etats initiaux ")
print("-------------------------------")
nb_state_i=int(input())
initials=[]
for i in range(nb_state_i):
	print('Entrer l etat initial ',i+1)
	s=int(input())
	initials.append(s)
print('Voici les etats initiaux',initials)
print("-------------------------------")
print("Entrer le nombre d'etats finaux ")
print("-------------------------------")
nb_state_f=int(input())
finals=[]
for i in range(nb_state_f):
	print('Entrer l etat final ',i+1)
	s=int(input())
	finals.append(s)
print('Voici les etats finaux',finals)
print("-------------------------------")
print('Enter le nombre de transition')
print("-------------------------------")
nb_t=int(input())
transitions=[]
for i in range(nb_t):
	print('Pour la transition ',i+1)
	a=int(input("l'etat de depart "))
	b=int(input("L'etat d arrivee "))
	c=input("le symbole ")
	s=(a,c,b)
	transitions.append(s)
print("La table de transition ",transitions)

print("-------------------------------")
print("Voici l'alphabet ",alphabet)
print("Voici les etats ",states)
print('Voici les etats initiaux ',initials)
print('Voici les etats finaux ',finals)
print("La table de transition ",transitions)
print("-------------------------------")

"""""
alphabet = ['a','b']
epsilons=['e']
states  = [1,2,3,4]
initials = [1]
finals = [2]
transitions = [ (1,'a',1),(1,'a',3), (1,'b',2),(2,'b',1),(2,'b',4),(4,'b',2),(4,'a',4),(3,'b',2),(3,'a',4)]
"""""
z={
	'alphabet':alphabet,
	'state':states,
	'initialstate':initials,
	'finalstate':finals,
	'transition':transitions
}

a = automaton(alphabet = alphabet,epsilons=epsilons, states  = states,initials = initials, finals =finals,
transitions = transitions)
b=automaton(alphabet = alphabet,epsilons=epsilons, states  = states,initials = initials, finals =finals,
transitions = transitions)

def App():
	print('Menu')
	print("1-Donner la nature de l'automate\n2-Determiniser\n3-Minimiser l'automate\n4- Question2\n5-Question 3 \n5-Le langage de commentaire")
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
		case 4:
			# Exemple d'utilisation
			texte_source = "Le chiffre 42 est un nombre reconnu, mais ABC123 n'est pas."
			texte_source=input("Entrer le texte de départ ")
			séparateur = " "
			résultats = reconnaître_nombres(texte_source, séparateur)
			# Afficher les résultats
			for résultat in résultats:
				print(résultat)
		case 5:
			pass
		case 6:
			print("Vous avez choisi le langage commentaire")
			texte = """acd /*abc%*/babA*/of"""
			texte=input("Entrer les commentaires ")
			commentaires = reconnaître_commentaires(texte)
			for commentaire in commentaires:
				print(commentaire)
		case _:
			print('Impossible')

App()

