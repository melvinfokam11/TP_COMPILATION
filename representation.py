import graphviz

def generer_graphe(alphabet, etats, etat_initial, etats_finaux, table_transition):
    # Création d'un nouvel objet de graphe
    graphe = graphviz.Digraph(format='png')

    # Ajout des états au graphe
    for etat in etats:
        if etat == etat_initial:
            graphe.node(etat, label=etat, shape='doublecircle')
        elif etat in etats_finaux:
            graphe.node(etat, label=etat, shape='doublecircle')
        else:
            graphe.node(etat, label=etat, shape='circle')

    # Ajout des transitions au graphe
    for depart, transitions in table_transition.items():
        for symbole, arrivee in transitions.items():
            graphe.edge(depart, arrivee, label=symbole)

    # Génération du graphe au format PNGgraphviz.generer_graphe('automate', view=True)
    filenameAFD = graphe.render(filename='imageGraphAFD')
# Demande à l'utilisateur d'entrer les données
alphabet = input("Veuillez entrer l'alphabet (séparé par des virgules): ").split(',')
etats = input("Veuillez entrer l'ensemble des états (séparé par des virgules): ").split(',')
etat_initial = input("Veuillez entrer l'état initial: ")
etats_finaux = input("Veuillez entrer les états finaux (séparés par des virgules): ").split(',')

table_transition = {}
for etat in etats:
    transitions = {}
    for symbole in alphabet:
        arrivee = input(f"Veuillez entrer l'état d'arrivée pour la transition ({etat} -> {symbole}): ")
        transitions[symbole] = arrivee
    table_transition[etat] = transitions

# Génération de la représentation graphique de l'automate
generer_graphe(alphabet, etats, etat_initial, etats_finaux, table_transition)