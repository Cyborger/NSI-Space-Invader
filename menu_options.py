# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding

if False:
    from ..lib.Processing3 import *


def interface(jeu):
    """Retourne les éléments de l'interface pour le menu des options, défini également les boutons dans la variable jeu.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.

    Retourne:
        - dict: Dictionnaire comportant les éléements de l'interface.
    """
    jeu["boutons"] = [
        "Couleur HUD : " + jeu["sauvegarde"]["couleur"],
        "Vies joueur : " + str(jeu["sauvegarde"]["vies"]),
        "Ennemis max : " + str(jeu["sauvegarde"]["max_ennemis"]),
        "Facteur vitesse : " + str(jeu["sauvegarde"]["vitesse"])
    ]

    if jeu["sauvegarde"]["debug"]:
        jeu["boutons"].append("Debug : actif")
    else:
        jeu["boutons"].append("Debug : inactif")

    jeu["boutons"].append("Menu Principal")

    return {
        "titre": "Options"
    }


def boutons(jeu):
    """Permet au joueur d'intéragir avec les boutons du menu principal.

    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.

    Retourne:
        - bool: Booléen indiquant s'il faut réinitialiser le curseur et les boutons.
    """
    if jeu["curseur"] == 0:  # Bouton Couleurs
        couleurs = jeu["couleurs"].keys()
        for i in range(len(couleurs)):  # Permet d'aller à la couleur "suivante" parmis la liste des couleurs
            if jeu["sauvegarde"]["couleur"] == couleurs[i]:
                jeu["sauvegarde"]["couleur"] = couleurs[i + 1] if i + 1 < len(couleurs) else couleurs[0]
                break  # Permet d'éviter de modifier plusieurs fois la couleur

    elif jeu["curseur"] == 1:  # Bouton Vies du joueur
        vies = jeu["sauvegarde"]["vies"]
        jeu["sauvegarde"]["vies"] = vies + 1 if vies < 3 else 1
    elif jeu["curseur"] == 2:  # Bouton Ennemis max (pour définir le nombre d'ennemi maximum à l'écran)
        ennemis_max = jeu["sauvegarde"]["max_ennemis"]
        jeu["sauvegarde"]["max_ennemis"] = ennemis_max + 3 if ennemis_max < 9 else 3
    elif jeu["curseur"] == 3:  # Bouton Vitesse (pour changer le facteur de vitesse du jeu)
        vitesse = jeu["sauvegarde"]["vitesse"]
        jeu["sauvegarde"]["vitesse"] = vitesse + 1 if vitesse < 3 else 1
    elif jeu["curseur"] == 4:  # Bouton Debug (voir rapport)
        jeu["sauvegarde"]["debug"] = not jeu["sauvegarde"]["debug"]
    else:
        jeu["statut"] = 0
        return True

    return False
