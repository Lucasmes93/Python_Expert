import json
import os
from collections import Counter

###################### Partie 1 - Comptage de lettres ######################
mot = "Mississippi"

# Nombre de lettres "i"
lettre_cible = 'i'

nb_lettres_cible = mot.count(lettre_cible)
print(f"Le nombre de lettres '{lettre_cible}' dans la chaîne est : {nb_lettres_cible}")

# Nombre de chaque lettre
comp_lettres = {lettre: mot.count(lettre) for lettre in set(mot)}
print("Nombre de chaque lettre :", comp_lettres)



#################### Partie 2 - Modification de lettres ####################
freq = Counter(mot)
max_freq = max(freq.values())
lettres_plus_freq = [lettre for lettre, freq in freq.items() if freq == max_freq]

lettre_modifiee = 'e'
mot_modifie = ''.join([lettre_modifiee if lettre in lettres_plus_freq else lettre for lettre in mot])

print("Mot original :", mot)
print("Mot modifié :", mot_modifie)
print("Fréquence d'apparition de chaque lettre :", dict(freq))



######################### Partie 3 - Texte fourni #########################
texte_source = """
Je vois là-bas un être sans tête qui grimpe à une perche sans fin.

Tandis que je me promène, tentant de me délasser, d'atteindre ce fond de délassement qu'il est si difficile 
d'atteindre, qu'il est improbable, quoique ayant tellement soupiré après, que je l'atteigne jamais, tandis que je me 
promène, je le sais là, je le sens, qui infatigablement (oh non il est terriblement fatigué), qui incessamment 
grimpe, et s'en va grimpant sur son terrible chemin vertical.

Souvent il me paraît comme un amas de loques, où se trahissent deux bras, une sorte de jambe, et ce monstre qui 
devrait tomber de par sa position même (car elle n'a rien d'une position d'équilibre) et plus encore par 
l'incessation de son dur exercice, grimpe toujours.

Pourtant de cette montée aussi je dois douter, car il échappe assez souvent à mon attention, à cause des soucis de 
toutes sortes que la vie a toujours su me présenter et je me demande lorsque je le revois, les repères manquant 
complètement, s'il est plus haut ou, si loin d'avoir accompli des progrès, il ne serait pas plus bas.

Parfois je le vois comme un vrai fou, presque sans appui, grotesquement écarté le plus possible de cette perche qu'il 
hait peut-être et il y aurait de quoi, encore que l'espace lui doive être plus haïssable encore.

Henri Michaux"""

# Compter le nombre de fois que "le" et "e" apparaissent dans le texte
mot_cible_1 = "le"
mot_cible_2 = "e"
nombre_mot_cible_1 = texte_source.lower().split().count(mot_cible_1)
nombre_mot_cible_2 = texte_source.lower().count(mot_cible_2)

# Afficher les résultats
print(f"Nombre de fois que '{mot_cible_1}' apparaît : {nombre_mot_cible_1}")
print(f"Nombre de fois que '{mot_cible_2}' apparaît : {nombre_mot_cible_2}")

# Effacer tous les 'e' du texte
texte_sans_lettre = texte_source.replace(lettre_modifiee, '')

# Afficher le texte sans 'e'
print("\nTexte sans '{}':\n".format(lettre_modifiee), texte_sans_lettre)

# Compter les occurrences de chaque mot
occurrences_mots = Counter(texte_source.lower().split())

chemin_dossier = r"D:\ESTIAM\E4\Python\Python_Expert"
nom_fichier_json = "fichiers.json"
chemin_fichier_json = os.path.join(chemin_dossier, nom_fichier_json)

# Vérifier si le dossier existe, sinon le créer
os.makedirs(chemin_dossier, exist_ok=True)

# Enregistrement JSON
pronoms_cibles = ["je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles",
                  "me", "te", "se", "nous", "vous", "le", "la", "les", "lui", "leur",
                  "moi", "toi", "soi", "nous", "vous", "eux", "elles",
                  "ce", "cet", "cette", "ces",
                  "le mien", "la mienne", "les miens", "les miennes",
                  "le tien", "la tienne", "les tiens", "les tiennes",
                  "le sien", "la sienne", "les siens", "les siennes",
                  "le nôtre", "la nôtre", "les nôtres",
                  "le vôtre", "la vôtre", "les vôtres",
                  "le leur", "la leur", "les leurs",
                  "celui", "celle", "ceux", "celles",
                  "qui", "que", "quoi", "dont", "où",
                  "quel", "quelle", "quels", "quelles",
                  "quelque chose", "quelqu'un",
                  "rien", "personne",
                  "tout", "tous", "toute", "toutes",
                  "chacun", "chacune",
                  "plusieurs",
                  "certains", "certaines",
                  "m'", "t'", "s'", "l'", "y", "en"]

statistiques = {
    "pronoms_comptes": {pron: occurrences_mots[pron] for pron in pronoms_cibles},
    "{}_compte_total".format(lettre_modifiee): occurrences_mots[lettre_modifiee]
}

with open(chemin_fichier_json, 'w') as fichier_json:
    json.dump(statistiques, fichier_json)



###################### Partie 4 - Mot le plus utilisé ######################
mot_max_occurrence = max(occurrences_mots, key=occurrences_mots.get)
print("Mot le plus utilisé dans le texte:", mot_max_occurrence)

# Mot le plus utilisé (hors pronoms)
mots_non_pronoms = [mot for mot in occurrences_mots if mot not in pronoms_cibles]
mot_max_occurrence_non_pronoms = max(mots_non_pronoms, key=occurrences_mots.get)
print("Mot le plus utilisé (hors pronoms) dans le texte:", mot_max_occurrence_non_pronoms)



##################### Partie 5 - Couple de 2 elements #####################
elems = ['a', 'b', 'c', 'a', 'b', 'a', 'd', 'e']

#Créer des couples de deux valeurs
couples = [(elems[i], elems[i+1]) for i in range(0, len(elems)-1, 2)]
print(f"Voici les couples de 2 elements :{couples} de la liste d'element suiviant : {elems} ")
