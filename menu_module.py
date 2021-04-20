# -*- coding: utf-8 -*- Pour que l'interpréteur Python utilise l'encodage UTF-8 plutôt que l'encodage ASCII, voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding

def interface(jeu):
    """Permet l'affichage des éléments de l'interface du menu.
    
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    background(0)
    fill(65, 255, 0)
    textAlign(CENTER) # Permet de centrer le texte (https://py.processing.org/reference/textAlign.html)
    
    # Définition des éléments de l'interface selon le statut du jeu
    if jeu["statut"] == 0:
        titre = "Space Invader"
        jeu["boutons"] = ["Jouer", "Options", "Quitter"]
    elif jeu["statut"] == 2:
        titre = "Game Over"
        jeu["boutons"] = ["Recommencer", "Menu Principal"]

    # Titre
    textFont(jeu["polices"]["retro"], 48)
    text(titre, width // 2, height // 2 - 100)

    # Boutons
    textFont(jeu["polices"]["retro"])
    longueurMax = 0 # Permet d'indiquer la longueur maximale atteint par les boutons pour le placement du curseur

    for i in range(len(jeu["boutons"])):
        text(jeu["boutons"][i], width // 2, height // 2 + 50 * i)

        if textWidth(jeu["boutons"][i]) > longueurMax: # textWidth permet de récupérer la longueur d'une chaîne de caractère en pixel
            longueurMax = textWidth(jeu["boutons"][i])
    
    # Curseur
    if not "curseur" in jeu: # Initialisation du curseur
        jeu["curseur"] = 0

    text("<", (width + longueurMax) // 2 + 30, height // 2 + 50 * jeu["curseur"])
    text(">", (width - longueurMax) // 2 - 30, height // 2 + 50 * jeu["curseur"])
    
def boutons(jeu):
    """Fonction appelée lorsque l'un des boutons a été sélectionné par l'utilisateur.
    
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if jeu["curseur"] == 0: # Bouton Jouer et Recommencer
        jeu["statut"] = 1
    elif jeu["curseur"] == 1 and jeu["statut"] == 0: # Bouton Options (menu principal uniquement)
        jeu["statut"] = 2
    elif jeu["curseur"] == 1 and jeu["statut"] == 2: # Bouton Menu Principal (Game Over uniquement)
        jeu["statut"] = 0
    else: # Bouton Quitter (menu principal uniquement)
        exit()
    
    jeu.pop("curseur") # Retrait des variables liées à l'affichage du menu
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
    if not "curseur" in jeu: # Permet d'éviter l'exécution de la fonction si l'interface n'a pas encore été initialisée
        return

    if keyCode == DOWN:
        jeu["curseur"] += 1 if jeu["curseur"] < len(jeu["boutons"]) - 1 else -len(jeu["boutons"]) + 1 # Incrémente de 1 au curseur s'il est inférieur à la longueur de la liste (partant de 0)
    elif keyCode == UP:
        jeu["curseur"] += -1 if jeu["curseur"] > 0 else len(jeu["boutons"]) - 1 # Incrémente de -1 au curseur s'il est supérieur à 0
    elif key == ENTER or keyCode == RIGHT:
        boutons(jeu)

def souris(jeu, clic):
    """Permet à l'utilisateur d'interagir avec les boutons du menu par la souris.
    
    Paramètres:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
        - bool clic: Permet d'indiquer ou non que la souris a été cliqué.
    """
    if not "curseur" in jeu: # Permet d'éviter l'exécution de la fonction si l'interface n'a pas encore été initialisée
        return

    for i in range(len(jeu["boutons"])):
        if (mouseX < width // 2 + 100 and mouseX > width // 2 - 100 and
            mouseY > height // 2 - 30 + 50 * i and mouseY < height // 2 + 30 + 50 * i): # Vérifie si la souris est situé sur le bouton
            if clic:
                boutons(jeu)
            else:
                jeu["curseur"] = i
            
