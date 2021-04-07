from menu_module import *

def setup():
    """https://processing.org/reference/setup_.html"""
    global jeu
    
    # Statut du jeu:
    # 0 = Menu principal
    # 1 = Jeu
    # 2 = "Game Over"
    # 3 = Options
    
    # Initialisation d'un dictionnaire contenant toutes les valeurs associé au jeu
    jeu = {
        "statut": 0, # Voir "Statut du jeu"
        "curseur": 0, # Permet la sélection des boutons dans les menu
        "polices": { # Pour les polices d'écriture
            "retro": createFont("data/fonts/retro.ttf", 28)
        }
    }
    
    size(600, 650)
    
    
def draw():
    """https://processing.org/reference/draw_.html"""
    if jeu["statut"] == 0:
        menu_interface(jeu) # Affichage des éléments de l'interface du menu
    elif jeu["statut"] == 1:
        pass
    elif jeu["statut"] == 2:
        pass
    else:
        pass

def keyPressed():
    """https://processing.org/reference/keyPressed_.html"""
    if jeu["statut"] == 0:
        menu_key(jeu)
