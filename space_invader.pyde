import menu_module
import jeu_module
import json # Pour afficher la variable jeu dans un fichier json externe (debug)

def setup():
    """https://py.processing.org/reference/setup.html"""
    global jeu
    
    # Statut du jeu:
    # 0 = Menu principal
    # 1 = Jeu en cours
    # 2 = "Game Over"
    # 3 = Options
    
    # Initialisation d'un dictionnaire contenant toutes les valeurs associé au jeu
    jeu = {
        "statut": 0, # Voir "Statut du jeu"
        "images": { # Préchargement des images
            "joueur": loadImage("data/images/joueur.png"),
            "projectile": loadImage("data/images/projectile.png"),
            "ennemi": loadImage("data/images/ennemi.png")
        },
        "polices": { # Préchargement des polices d'écriture
            "retro": createFont("data/polices/retro.ttf", 28)
        }
    }
    
    size(600, 650)

def debug(output):
    """Affiche la variable du paramètre output dans la console et l'écrit, après conversion au format JSON, dans le fichier debug.json."""
    print(output)
    debug = open("debug.json", "w")
    debug.write(json.dumps(jeu, skipkeys=True, sort_keys=True, indent=4, default=lambda o: str(o)))
    debug.close()
    
def draw():
    """https://py.processing.org/reference/draw.html"""
    debug(jeu)
    
    if jeu["statut"] == 0:
        menu_module.interface(jeu) # Affichage des éléments de l'interface du menu
    elif jeu["statut"] == 1:
        jeu_module.afficher(jeu)
    elif jeu["statut"] == 2:
        pass
    else:
        pass

def keyPressed():
    """https://py.processing.org/reference/keyPressed.html"""
    if jeu["statut"] == 0:
        menu_module.clavier(jeu)
    elif jeu["statut"] == 1:
        jeu_module.clavier(jeu)

def mouseMoved():
    """https://py.processing.org/reference/mouseMoved.html"""
    if jeu["statut"] == 0:
        menu_module.souris(jeu, False)

def mouseClicked():
    """https://py.processing.org/reference/mouseClicked.html"""
    if jeu["statut"] == 0:
        menu_module.souris(jeu, True)
