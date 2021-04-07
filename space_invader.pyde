from menu_module import *

def setup():
    """https://py.processing.org/reference/setup.html"""
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
    """https://py.processing.org/reference/draw.html"""
    if jeu["statut"] == 0:
        menu_interface(jeu) # Affichage des éléments de l'interface du menu
    elif jeu["statut"] == 1:
        pass
    elif jeu["statut"] == 2:
        pass
    else:
        pass

def keyPressed():
    """https://py.processing.org/reference/keyPressed.html"""
    if jeu["statut"] == 0:
        menu_key(jeu)

def mouseMoved():
    """https://py.processing.org/reference/mouseMoved.html"""
    if jeu["statut"] == 0:
        menu_souris(jeu, False)

def mouseClicked():
    """https://py.processing.org/reference/mouseClicked.html"""
    if jeu["statut"] == 0:
        menu_souris(jeu, True)
