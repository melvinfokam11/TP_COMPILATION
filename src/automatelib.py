#!/usr/bin/env python
#coding=utf8

class State(object):
	'''
		Classe définissant un état
	'''
	
	def __init__(self, name):
		
		self.name = name

	def __repr__(self):
		return u'<State %s>' % self.name
		
class Transition(object):
	'''
		Classe définissant une transition
	'''
	
	def __init__(self, state_from, state_to, labels):
		
		self.state_from = state_from
		self.state_to = state_to
		self.labels = labels

	def __repr__(self):
		return u'<Transition %s -> %s labeled %s>' % (self.state_from, 
								self.state_to, ', '.join(self.labels))

class EpsilonTransition(Transition):
	'''
		Classe définissant une Epsilon transition
	'''
	
	def __init__(self, state_from, state_to):
		
		self.state_from = state_from
		self.state_to = state_to

	def __repr__(self):
		return u'<EpsilonTransition %s -> %s >' % (self.state_from, 
														self.state_to)

class Automaton(object):
	'''
		Classe définissant un Automate Fini A
	'''
	
	def __init__(self, alphabet, states=(), initial_states=(), 
									final_states=(), transitions=()):
		
		# L'alphabet Σ de l'automate
		self.alphabet = set(alphabet)
		
		# Ses états Q (objets State)
		self.states = set(states)
		
		# Ses états finaux Q_f (objets State)
		self.final_states = set(final_states)
		
		# Et ses états initiaux Q_0 (objets State)
		self.initial_states = set(initial_states)
		
		# Et ses transition δ (objets Transision)
		self.transitions = set(transitions)

	
	def add_state(self, state):
		'''
			Ajouter un état à l'automate.
		'''
		
		self.states.add(state)
	
	
	def add_initial_state(self, state):
		'''
			Ajouter un état initial à l'automate
		'''
		
		self.initial_states.add(state)
		
		
	def add_final_state(self, state):
		'''
			Ajouter un état final à l'automate
		'''
		
		self.final_state.add(state)
	
	
	def add_transition(self, transition):
		'''
			Ajouter une transition à l'automate
		'''
		
		self.transitions.add(transition)


	def leave(self, state):
		'''
			Méthode qui retourne toutes les transisions qui 
			quittent state
		'''
		
		return set([tr for tr in self.transitions if tr.state_from is state])
	
	def solve_epsilons(self, tr):
		'''
			Retourne tous les états joints à une série d'epsilon transitions
		'''
		
		states_to_travel = set((tr.state_to,))
		states_travelled = set()
		tr_travelled = set((tr,))
		
		while states_to_travel:
			# On récupère un état que l'on a pas encore traité
			state = states_to_travel.pop()
			
			# Par rapport à cet état, on récupère toutes les 
			# epsilons transition qui partent de cet état
			tr_to_travel = set([tr for tr in self.leave(states_travelled) if type(tr) is EpsilonTransition and tr not in tr_travelled])
			states_to_travel |= set([tr.state_to for tr in tr_to_travel]) - states_travelled
			tr_travelled |= tr_to_travel
			states_travelled.add(state)
		return states_travelled
			
	
	def acceptance(self, word):
		states = self.initial_states
		
		for f in word:
			next_states = set()
			for s in states:
				for tr in self.leave(s):
					if type(tr) == Transition and f in tr.labels:
						next_states.add(tr.state_to)
					elif type(tr) == EpsilonTransition:
						next_states |= self.solve_epsilons(tr)
						
			states = next_states
			print (f, ' --> ', states)		
		# En Python, & est l'opérateur d'intersection des ensembles

		return bool(states & self.final_states)
				
	def render(self, filename):
		'''
			Générer une image de l'automate
		'''
		
		try:
			import pygraphviz as gv
		except ImportError:
			print ("Il faut installer pygraphviz pour utiliser les méthodes de")
			print ("visualisation de l\'automate : easy_install pygraphviz")
		else:
			graph = gv.AGraph(directed=True) # Un automate est un graphe dirigé
			graph.add_nodes_from([n.name for n in self.states])
			graph.graph_attr['rankdir'] = 'LR';
			for st in self.final_states:
				n = graph.get_node(st.name)
				n.attr['shape'] = 'doublecircle'
			for st in self.initial_states:
				n = graph.get_node(st.name)
				n.attr['style'] = 'filled'
				n.attr['fillcolor'] = '#DDDDDD'
			for tr in self.transitions:
				if type(tr) is Transition:
					graph.add_edge(tr.state_from.name, tr.state_to.name, label=', '.join(tr.labels))
				elif type(tr) is EpsilonTransition:
					graph.add_edge(tr.state_from.name, tr.state_to.name)
			graph.draw(filename, prog='dot')

	def __repr__(self):
		return u'<Automaton with %s states and %s transition>' % (
				len(self.states),
				len(self.transitions)
			)
    

def reconnaître_commentaires(texte):
    état = 0
    alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]{}|;':,.<>/?~` ")
    commentaires = []
    commentaire = ""
    
    for caractère in texte:
        if état == 0:
            if caractère == '/':
                état = 1
            else:
                état = 0
        elif état == 1:
            if caractère == '*':
                état = 2
                commentaire = ""
            else:
                état = 0
        elif état == 2:
            if caractère == '*':
                état = 3
            elif caractère == '%':
                état = 4
            elif caractère in alphabet:
                commentaire += caractère
            else:
                état = 0
        elif état == 3:
            if caractère == '/':
                état = 0
                commentaires.append(commentaire)
            elif caractère == '*':
                état = 3
            elif caractère == '%':
                état = 2
                commentaire += caractère
            else:
                état = 2
                commentaire += '*' + caractère
        elif état == 4:
            commentaire += caractère
            état = 2
    
    return commentaires

# Test de l'outil avec un exemple de texte
texte = """
acd /*abc%*/babA*/of

"""

commentaires = reconnaître_commentaires(texte)
for commentaire in commentaires:
    print(commentaire)
def determiniser_automate(etats, alphabet, transitions, etat_initial, etats_finaux):
    etats_determinises = set()  # Ensemble des états déterminisés
    nouvelle_transitions = []  # Liste des nouvelles transitions déterminisées
    nouveaux_etats_finaux = set()  # Ensemble des nouveaux états finaux déterminisés
    
    etats_non_determinises = set([etat_initial])  # Ensemble des états non déterminisés à explorer
    
    # Tant qu'il y a des états non déterminisés à explorer
    while etats_non_determinises:
        etat_non_determinise = etats_non_determinises.pop()  # Prendre un état non déterminisé
        
        if etat_non_determinise in etats_determinises:
            continue  # Passer à l'état suivant s'il a déjà été déterminisé
        
        etats_determinises.add(etat_non_determinise)  # Ajouter l'état à l'ensemble des états déterminisés
        
        for symbole in alphabet:
            etats_suivants = set()  # Ensemble des états suivants pour le symbole donné
            
            # Trouver tous les états atteignables à partir de l'état non déterminisé pour le symbole donné
            for etat in etat_non_determinise:
                for transition in transitions:
                    etat_depart, symbole_transition, etat_arrivee = transition
                    if etat == etat_depart and symbole == symbole_transition:
                        etats_suivants.add(etat_arrivee)
            
            if etats_suivants:
                etats_non_determinises.add(frozenset(etats_suivants))  # Ajouter les nouveaux états non déterminisés à explorer
                
                nouvelle_transition = (etat_non_determinise, symbole, frozenset(etats_suivants))
                nouvelle_transitions.append(nouvelle_transition)  # Ajouter la nouvelle transition déterminisée
        
        # Vérifier si l'état déterminisé contient un état final
        if any(etat in etats_finaux for etat in etat_non_determinise):
            nouveaux_etats_finaux.add(etat_non_determinise)  # Ajouter l'état déterminisé à l'ensemble des états finaux déterminisés
    
    return etats_determinises, alphabet, nouvelle_transitions, frozenset([etat_initial]), nouveaux_etats_finaux

