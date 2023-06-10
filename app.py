class AFN:
    def __init__(self, etats, alphabet, transitions, etat_initial, etats_finaux):
        self.etats = etats
        self.alphabet = alphabet
        self.transitions = transitions
        self.etat_initial = etat_initial
        self.etats_finaux = etats_finaux

    def ajouter_transition(self, depart, symbole, arrivee):
        self.transitions.append((depart, symbole, arrivee))

    def determiniser(self):
        etats_determinises = [self.epsilon_cloture([self.etat_initial])]
        nouveaux_etats = etats_determinises.copy()
        alphabet = self.alphabet.copy()
        nouvelles_transitions = []

        while nouveaux_etats:
            etat_actuel = nouveaux_etats.pop(0)

            for symbole in alphabet:
                etat_suivant = self.epsilon_cloture(self.fermeture_etat(etat_actuel, symbole))

                if etat_suivant:
                    nouvelles_transitions.append((etat_actuel, symbole, etat_suivant))

                    if etat_suivant not in etats_determinises:
                        etats_determinises.append(etat_suivant)
                        nouveaux_etats.append(etat_suivant)

        etat_initial = [self.etat_initial]
        etats_finaux = [etat for etat in etats_determinises if any(ef in etat for ef in self.etats_finaux)]

        return AFD(etats_determinises, alphabet, nouvelles_transitions, etat_initial, etats_finaux)

    def epsilon_cloture(self, etats):
        pile = list(etats)
        epsilon_cloture = set(etats)

        while pile:
            etat = pile.pop()

            for transition in self.transitions:
                depart, symbole, arrivee = transition
                if depart == etat and symbole == '':
                    if arrivee not in epsilon_cloture:
                        epsilon_cloture.add(arrivee)
                        pile.append(arrivee)

        return frozenset(epsilon_cloture)

    def fermeture_etat(self, etats, symbole):
        fermeture = set()

        for etat in etats:
            for transition in self.transitions:
                depart, s, arrivee = transition
                if depart == etat and s == symbole:
                    fermeture.add(arrivee)

        return frozenset(fermeture)


class AFD:
    def __init__(self, etats, alphabet, transitions, etat_initial, etats_finaux):
        self.etats = etats
        self.alphabet = alphabet
        self.transitions = transitions
        self.etat_initial = etat_initial
        self.etats_finaux = etats_finaux

    def ajouter_transition(self, depart, symbole, arrivee):
        self.transitions.append((depart, symbole, arrivee))


# Exemple d'utilisation
afn = AFN(['A', 'B', 'C'], ['0', '1'], [('A', '', 'B'), ('A', '0', 'A'), ('B', '1', 'C')], 'A', ['C'])

afd = afn.determiniser()

print("États de l'AFD :", afd.etats)
print("Alphabet de l'AFD :", afd.alphabet)
print("Transitions de l'AFD :", afd.transitions)
print("État initial de l'AFD :", afd.etat_initial)
print("États finaux de l'AFD :", afd.etats_finaux)