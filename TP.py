# Iles YAZI; Ludwig DINSPEL; Luca MESSIA DOLIVEUX; Gregoire LEROGNON; Arthur DEUMENI TSAKO - Paris E4 WMD

import json
import os
from collections import Counter

# Partie 1 - Comptage de lettres
mot = "Mississippi"

# Nombre de lettres "i"
nb_i = mot.count('i')
print(f"Le nombre de lettres 'i' dans la chaîne est : {nb_i}")

# Nombre de chaque lettre
compt_lettres = {lettre: mot.count(lettre) for lettre in set(mot)}
print("Nombre de chaque lettre :", compt_lettres)

# Partie 2 - Modification de lettres
freq = Counter(mot)
max_freq = max(freq.values())
lettres_plus_freq = [lettre for lettre, freq in freq.items() if freq == max_freq]

mot = ''.join(['e' if lettre in lettres_plus_freq else lettre for lettre in mot])

print("Mot original :", "Mississippi")
print("Mot modifié :", mot)
print("Fréquence d'apparition de chaque lettre :", dict(freq))

# Partie 3 - Texte fourni
texte_source = """
Je vois là-bas un être sans tête qui grimpe à une perche sans fin.

Tandis que je me promène, tentant de me délasser, d'atteindre ce fond de délassement qu'il est si difficile d'atteindre, qu'il est improbable, quoique ayant tellement
soupiré après, que je l'atteigne jamais, tandis que je me promène, je le sais là, je le sens, qui infatigablement (oh non il est terriblement fatigué), qui incessamment
grimpe, et s'en va grimpant sur son terrible chemin vertical.

Souvent il me paraît comme un amas de loques, où se trahissent deux bras, une sorte de jambe, et ce monstre qui devrait tomber de par sa position même (car elle n'a rien d'une
position d'équilibre) et plus encore par l'incessation de son dur exercice, grimpe toujours.

Pourtant de cette montée aussi je dois douter, car il échappe assez souvent à mon attention, à cause des soucis de toutes sortes que la vie a toujours su me présenter
et je me demande lorsque je le revois, les repères manquant complètement, s'il est plus haut ou, si loin d'avoir accompli des progrès, il ne serait pas plus bas.

Parfois je le vois comme un vrai fou, presque sans appui, grotesquement écarté le plus possible de cette perche qu'il hait peut-être et il y aurait de quoi, encore que l'espace
lui doive être plus haïssable encore.

Henri Michaux"""

# Compter le nombre de fois que "le" et "e" apparaissent dans le texte
nombre_le = texte_source.lower().split().count("le")
nombre_e = texte_source.lower().count("e")

# Afficher les résultats
print(f"Nombre de fois que 'le' apparaît : {nombre_le}")
print(f"Nombre de fois que 'e' apparaît : {nombre_e}")

# Effacer tous les 'e' du texte
texte_sans_e = texte_source.replace('e', '')

# Afficher le texte sans 'e'
print("\nTexte sans 'e':\n", texte_sans_e)

# Compter les occurrences de chaque mot
occurrences_mots = Counter(texte_source.lower().split())

chemin_dossier = r"C:\Users\MESSIA\Desktop\ESTIAM\E4\Python_Expert"
chemin_fichier_json = os.path.join(chemin_dossier, "fichiers.json")

# Vérifier si le dossier existe, sinon le créer
os.makedirs(chemin_dossier, exist_ok=True)

# Enregistrement JSON
statistiques = {
    "pronoms_comptes": {pron: occurrences_mots[pron] for pron in
                        ["je", "tu", "il", "elle", "nous", "vous", "ils", "elles"]},
    "e_compte_total": occurrences_mots['e']
}

with open(chemin_fichier_json, 'w') as fichier_json:
    json.dump(statistiques, fichier_json)

# Partie 4 - Mot le plus utilisé
mot_max_occurrence = max(occurrences_mots, key=occurrences_mots.get)
print("Mot le plus utilisé dans le texte:", mot_max_occurrence)

# Mot le plus utilisé (hors pronoms)
mots_non_pronoms = [mot for mot in occurrences_mots if
                    mot not in ["je", "tu", "il", "elle", "nous", "vous", "ils", "elles"]]
mot_max_occurrence_non_pronoms = max(mots_non_pronoms, key=occurrences_mots.get)
print("Mot le plus utilisé (hors pronoms) dans le texte:", mot_max_occurrence_non_pronoms)
