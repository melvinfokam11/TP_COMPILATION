def add(self, other):
        """
        surchage de l'opération d'addition  qui permet d'additionner deux atomates
        ex: Automate_1 + Automate_2 = Automate_
        @param other: deuxieme authomate
        """

        for etat in other.etats:
            if etat in self.etats:
                other.renommer_etat(",".join(etat), ",".join(etat) + "-2")

        tous_les_etats_de_union = []
        toutes_les_transitions_union = {}
        nouvel_alphabet = list(set(self.alphabet + other.alphabet))

        etat_initial_union = []
        for etat in self.etats_initiaux:
            for num_etat in etat:
                etat_initial_union.append(num_etat)

        for etat in other.etats_initiaux:
            for num_etat in etat:
                etat_initial_union.append(num_etat)

        tous_les_etats_de_union.append(etat_initial_union)
        etat_initial_union = [etat_initial_union]

        for etat in tous_les_etats_de_union:

            for character in nouvel_alphabet:

                nouvel_etat_pour_charactere = []

                for numero_etat in etat:

                    liste_des_etats = self.f_transitions(
                        [numero_etat], character)
                    if len(liste_des_etats) == 0:
                        liste_des_etats = other.f_transitions(
                            [numero_etat], character)

                    for e in liste_des_etats:
                        for num_etat in e:
                            if num_etat not in nouvel_etat_pour_charactere:
                                nouvel_etat_pour_charactere.append(num_etat)

                if nouvel_etat_pour_charactere not in tous_les_etats_de_union:
                    if len(nouvel_etat_pour_charactere) != 0:
                        tous_les_etats_de_union.append(
                            nouvel_etat_pour_charactere)

                if len(nouvel_etat_pour_charactere) != 0:
                    toutes_les_transitions_union[(tuple(etat), character)] = [
                        nouvel_etat_pour_charactere]

        etats_finaux_de_union = []
        for etat in tous_les_etats_de_union:
            for etat_final in self.etats_finaux:
                for num_etat in etat_final:
                    if num_etat in etat:
                        if etat not in etats_finaux_de_union:
                            etats_finaux_de_union.append(etat)

            for etat_final in other.etats_finaux:
                for num_etat in etat_final:
                    if num_etat in etat:
                        if etat not in etats_finaux_de_union:
                            etats_finaux_de_union.append(etat)

        etats_finaux_de_union = etats_finaux_de_union

        res = Automate()
        res.create(nouvel_alphabet, tous_les_etats_de_union, etat_initial_union,
                   etats_finaux_de_union, toutes_les_transitions_union)

        return res