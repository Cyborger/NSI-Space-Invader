# -*- coding: utf-8 -*- Pour que l'interpréteur Python utilise l'encodage UTF-8 plutôt que l'encodage ASCII, voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
def interface(jeu):
    """Permet l'affichage des éléments de l'interface du menu.
    
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    background(0)
    fill(65, 255, 0)
    textAlign(CENTER) # Permet de centrer le texte (https://py.processing.org/reference/textAlign.html)
    
    # Titre
    textFont(jeu["polices"]["retro"], 48)
    text("Space Invader", width // 2, height // 2 - 100)

    # Boutons
    jeu["boutons"] = ["Jouer", "Options", "Quitter"] # Utilisation d'un dictionnaire afin d'éviter le placement manuel et individuel des boutons
    textFont(jeu["polices"]["retro"])
    
    for i in range(len(jeu["boutons"])):
        text(jeu["boutons"][i], width // 2, height // 2 + 50 * i)
    
    # Curseur
    if not "curseur" in jeu: # Initialisation du curseur
        jeu["curseur"] = 0
    
    text("<", width // 2 + 100, height // 2 + 50 * jeu["curseur"])
    text(">", width // 2 - 100, height // 2 + 50 * jeu["curseur"])
    
def boutons(jeu):
    """Fonction appelée lorsque l'un des boutons a été sélectionné par l'utilisateur.
    
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if jeu["curseur"] == 0: # Bouton Jouer
        jeu.pop("curseur") # Retrait des variables liées à l'affichage du menu
        jeu.pop("boutons")
        
        jeu["statut"] = 1
    elif jeu["curseur"] == 1: # Bouton Options
        #jeu["statut"] = 3
        pass
    else: # Bouton Quitter
        exit()
    
def clavier(jeu):
    """Permet à l'utilisateur d'interagir avec les boutons du menu par les touches du clavier:
        - DOWN
        - UP
        - ENTER
        - RIGHT
        
    Paramètre:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
    """
    if keyCode == DOWN:
        jeu["curseur"] += 1 if jeu["curseur"] < 2 else -2 # Incrémentation de 1 au curseur si celui-ci est inférieur à 2 sinon retour à 0
    elif keyCode == UP:
        jeu["curseur"] += -1 if jeu["curseur"] > 0 else 2 # Retrait de 1 au curseur si celui-ci est supérieur à 0 sinon ajoute 2 (nombre de boutons du menu - 1)
    elif key == ENTER or keyCode == RIGHT:
        boutons(jeu)

def souris(jeu, clic):
    """Permet à l'utilisateur d'interagir avec les boutons du menu par la souris.
    
    Paramètres:
        - dict jeu: Dictionnaire contenant les valeurs associé au jeu.
        - bool clic: Permet d'indiquer ou non que la souris a été cliqué.
    """
    for i in range(len(jeu["boutons"])):
        if (mouseX < width // 2 + 100 and mouseX > width // 2 - 100 and
            mouseY > height // 2 - 30 + 50 * i and mouseY < height // 2 + 30 + 50 * i): # Vérifie si la souris est situé sur le bouton
            if clic:
                boutons(jeu)
            else:
                jeu["curseur"] = i
            
