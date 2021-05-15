# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
import menu_principal  # Pour les caractéristiques de chacun des menus
import menu_game_over
import menu_options


def interface(jeu):
    """Permet l'affichage des éléments de l'interface du menu.
    
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    background(0)
    fill(*jeu["couleurs"][jeu["sauvegarde"]["couleur"]])  # * permet d'extraire les valeurs du tuple en paramètre
    textAlign(CENTER)

    # Définition éléments interface selon le statut du jeu
    if jeu["statut"] == 0:
        elements = menu_principal.interface(jeu)
    elif jeu["statut"] == 2:
        elements = menu_game_over.interface(jeu)
    else:
        elements = menu_options.interface(jeu)

    # Titre
    textFont(jeu["polices"]["retro"], 48)
    text(elements["titre"], width // 2, height // 2 - 150)

    # Sous-titre (si défini)
    if "sous_titre" in elements:
        textSize(20)
        text(elements["sous_titre"], width // 2, height // 2 - 120)

    # Boutons
    textSize(28)
    longueur_max = 0  # Longueur maximale atteinte par les boutons. Permet d'aligner le curseur avec tous les boutons

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

    if jeu["statut"] == 0:
        menu_principal.boutons(jeu)
    elif jeu["statut"] == 2:
        menu_game_over.boutons(jeu)
    else:
        remise_a_zero = menu_options.boutons(jeu)

    if remise_a_zero:  # Retrait variables liées à l'affichage du menu au changement de statut de jeu
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
