# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding


def interface(jeu):
    """Retourne les éléments de l'interface pour le menu principal, défini également les boutons dans la variable jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.

    Retourne:
        - dict: Dictionnaire comportant les éléements de l'interface.
    """
    jeu["boutons"] = ["Jouer", "Options", "Quitter"]
    return {
        "titre": "Space Invader",
        "sous_titre": "Par Romain SEZNEC"
    }


def boutons(jeu):
    """Permet au joueur d'intéragir avec les boutons du menu principal.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if jeu["curseur"] == 0:  # Bouton Jouer
        jeu["statut"] = 1
    elif jeu["curseur"] == 1:  # Bouton Options
        jeu["statut"] = 3
    else:  # Bouton Quitter
        exit()
