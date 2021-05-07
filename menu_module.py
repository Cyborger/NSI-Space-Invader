# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
import sauvegarde_module

if False:
    from lib.Processing3 import *


def interface(jeu):
    """Permet l'affichage des éléments de l'interface du menu.
    
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    background(0)
    fill(*jeu["couleurs"][jeu["options"]["couleur"]])  # L'étoile permet d'extraire les valeurs du tuple
    textAlign(CENTER)  # Centre le texte

    sous_titre = ""  # Permet d'afficher un sous titre selon le statut de jeu

    # Définition éléments interface selon le statut du jeu
    if jeu["statut"] == 0:  # Menu principal
        titre = "Space Invader"
        sous_titre = "Par Romain SEZNEC"
        jeu["boutons"] = ["Jouer", "Options", "Quitter"]
    elif jeu["statut"] == 2:  # Menu "Game Over"
        titre = "Game Over"
        jeu["boutons"] = ["Recommencer", "Menu Principal"]

        sous_titre += "Score: " + str(jeu["scores"]["actuel"])

        if jeu["scores"]["actuel"] > jeu["scores"]["record"]:
            sous_titre += "\n*NOUVEAU RECORD*"  # Met en valeur le score si c'est un nouveau record
    else:  # Options
        titre = "Options"
        jeu["boutons"] = [
            "Couleur HUD : " + jeu["options"]["couleur"],
            "Vies joueur : " + str(jeu["options"]["vies"]),
            "Menu Principal",
        ]

    # Titre
    textFont(jeu["polices"]["retro"], 48)
    text(titre, width // 2, height // 2 - 150)

    # Sous-titre (si défini)
    if sous_titre != "":
        textSize(20)
        text(sous_titre, width // 2, height // 2 - 120)

    # Boutons
    textFont(jeu["polices"]["retro"])
    longueur_max = 0  # Indique la longueur maximale atteinte par les boutons pour le placement du curseur

    for i in range(len(jeu["boutons"])):
        text(jeu["boutons"][i], width // 2, height // 2 + 50 * i)

        if textWidth(jeu["boutons"][i]) > longueur_max:  # textWidth récupère la longueur d'un str en pixel
            longueur_max = textWidth(jeu["boutons"][i])

    # Curseur
    if "curseur" not in jeu:  # Initialisation du curseur
        jeu["curseur"] = 0

    text("<", (width + longueur_max) // 2 + 30, height // 2 + 50 * jeu["curseur"])
    text(">", (width - longueur_max) // 2 - 30, height // 2 + 50 * jeu["curseur"])


def boutons(jeu):
    """Fonction appelée lorsqu'un des boutons a été sélectionné par l'utilisateur.
    
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if "curseur" not in jeu:  # Évite l'exécution de la fonction si l'interface n'a pas encore été initialisée
        return

    remise_a_zero = True  # Indique si les variables liés au menu dans la variable jeu doivent être supprimés

    if jeu["statut"] == 0:  # Utilisation de conditions imbriqués pour une meilleur lisibilité
        if jeu["curseur"] == 0:  # Bouton Jouer
            jeu["statut"] = 1
        elif jeu["curseur"] == 1:  # Bouton Options
            jeu["statut"] = 3
        else:  # Bouton Quitter
            exit()
    elif jeu["statut"] == 2:
        if jeu["scores"]["actuel"] > jeu["scores"]["record"]:
            jeu["scores"]["record"] = jeu["scores"]["actuel"]  # Met à jour le record s'il est supérieur à l'ancien

        jeu["scores"]["actuel"] = 0  # Remise à zéro du score pour la prochaine partie

        if jeu["curseur"] == 0:  # Bouton Recommencer
            jeu["statut"] = 1
        else:  # Bouton Menu Principal
            jeu["statut"] = 0
    else:
        sauvegarde = sauvegarde_module.charger()  # Pour sauvegarder les paramètres

        if jeu["curseur"] == 0:  # Bouton Couleurs
            couleurs = jeu["couleurs"].keys()
            for i in range(len(couleurs)):  # Permet d'aller à la couleur "suivante" parmis la liste des couleurs
                if jeu["options"]["couleur"] == couleurs[i]:
                    jeu["options"]["couleur"] = couleurs[i + 1] if i + 1 < len(couleurs) else couleurs[0]
                    break  # Permet d'éviter de modifier plusieurs fois la couleur

            sauvegarde["couleur"] = jeu["options"]["couleur"]
            remise_a_zero = False
        elif jeu["curseur"] == 1:  # Bouton Vies du joueur
            vies = jeu["options"]["vies"]
            jeu["options"]["vies"] = vies + 1 if vies < 3 else 1
            remise_a_zero = False
        else:
            jeu["statut"] = 0

        sauvegarde_module.sauvegarder(sauvegarde)

    if remise_a_zero:  # Retrait variables liées à l'affichage du menu
        jeu.pop("curseur")
        jeu.pop("boutons")


def clavier(jeu):
    """Permet à l'utilisateur d'interagir avec les boutons du menu par les touches du clavier:
        - DOWN
        - UP
        - ENTER
        - RIGHT
        
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if "curseur" not in jeu:  # Évite l'exécution de la fonction si l'interface n'a pas encore été initialisée
        return

    if keyCode == DOWN:  # Fait descendre le curseur
        if jeu["curseur"] < len(jeu["boutons"]) - 1:  # Garde le curseur inférieur au nombre de boutons
            jeu["curseur"] += 1 if jeu["curseur"] < len(jeu["boutons"]) - 1 else -len(jeu["boutons"]) + 1
        else:  # Le ramène en haut s'il dépasse le nombre de boutons
            jeu["curseur"] = 0
    elif keyCode == UP:  # Fait remonter le curseur
        if jeu["curseur"] > 0:  # Garde le curseur supérieur à zéro
            jeu["curseur"] -= 1
        else:  # Le ramène en bas s'il est inférieur à zéro
            jeu["curseur"] = len(jeu["boutons"]) - 1
    elif key == ENTER:
        boutons(jeu)


def souris(jeu, clic):
    """Permet à l'utilisateur d'interagir avec les boutons du menu par la souris.
    
    Paramètres:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
        - bool clic: Permet d'indiquer ou non que la souris a été cliqué.
    """
    if "curseur" not in jeu:  # Évite l'exécution de la fonction si l'interface n'a pas encore été initialisée
        return

    for i in range(len(jeu["boutons"])):
        if (width // 2 + 100 > mouseX > width // 2 - 100 and  # Vérifie si la souris est sur le bouton
                height // 2 - 30 + 50 * i < mouseY < height // 2 + 30 + 50 * i):
            if clic:
                boutons(jeu)
            else:
                jeu["curseur"] = i
