# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding


def interface(jeu):
    """Retourne les éléments de l'interface pour le menu "Game Over", défini également les boutons dans la variable jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.

    Retourne:
        - dict: Dictionnaire comportant les éléments de l'interface.
    """
    jeu["boutons"] = ["Recommencer", "Menu Principal"]

    sous_titre = "Score: " + str(jeu["score"])

    if jeu["score"] > jeu["sauvegarde"]["record"]:
        sous_titre += "\n*NOUVEAU RECORD*"  # Met en valeur le score si c'est un nouveau record

    return {
        "titre": "Game Over",
        "sous_titre": sous_titre
    }


def boutons(jeu):
    """Permet au joueur d'intéragir avec les boutons du menu principal.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if jeu["score"] > jeu["sauvegarde"]["record"]:
        jeu["sauvegarde"]["record"] = jeu["score"]  # Met à jour le record s'il est supérieur à l'ancien

    jeu.pop("score")

    if jeu["curseur"] == 0:  # Bouton Recommencer
        jeu["statut"] = 1
    else:  # Bouton Menu Principal
        jeu["statut"] = 0
