import re

def reconnaître_nombres(texte, séparateur):
    mots = texte.split(séparateur)  # Diviser le texte en mots en utilisant le séparateur spécifié
    motif_nombre = r'^\d+$'  # Motif pour reconnaître un nombre (une séquence de chiffres)

    résultats = []
    for mot in mots:
        if re.match(motif_nombre, mot):
            résultats.append(f"{mot} : nombre")
        else:
            résultats.append(f"{mot} : Non reconnu")

    return résultats

"""# Exemple d'utilisation
texte_source = "Le chiffre 42 est un nombre reconnu, mais ABC123 n'est pas."
séparateur = " "
résultats = reconnaître_nombres(texte_source, séparateur)

# Afficher les résultats
for résultat in résultats:
    print(résultat)"""