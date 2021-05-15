import menu_module
import jeu_module
import sauvegarde_module
import json  # Pour afficher la variable jeu dans un fichier json externe lors du debug (data/debug.json)


def debug(output):
    """Affiche la valeur du paramètre output dans la console et l'écrit, après conversion au format JSON, dans le
    fichier data/debug.json.
    
    Paramètre:
        - output Any: Valeur à afficher. Peut être de tout type. Pas de valeur par défaut.
    """
    debug = open("data/debug.json", "w")  # Mode d'écriture écrasant pour éviter une taille de fichier élevée
    json.dump(output, debug, skipkeys=True, sort_keys=True, indent=4,
              default=lambda o: str(o))  # Indique comment convertir les valeurs objet en str
    debug.close()


def setup():
    """https://py.processing.org/reference/setup.html
    Initialise la variable jeu qui contient toutes les propriétés utilisées dans le jeu.
    """
    global jeu

    sauvegarde = sauvegarde_module.charger()   # Récupération de la valeur record dans le fichier data/sauvegarde.json

    jeu = {
        "statut": 0,
        "images": {},
        "polices": {
            "retro": createFont("data/polices/retro.ttf", 28)
        },
        "couleurs": {
            "rouge": (139, 0, 0),  # RGB inexact intentionnel
            "vert": (65, 255, 0),
            "bleu": (46, 207, 255),
            "blanc": (255, 255, 255)
        },
        "sauvegarde": sauvegarde
    }

    # Partie qui s'occupe du chargement des images de différentes couleurs
    images = ["ennemi", "joueur", "projectile"]  # Possibilité d'utiliser os.path mais non nécessaire pour 3 images...
    for couleur in jeu["couleurs"].keys():  # Permet d'itérer sur ["vert", "bleu", "blanc"]
        jeu["images"][couleur] = {}
        for image in images:
            jeu["images"][couleur][image] = loadImage("data/images/" + couleur + "/" + image + ".png")

    size(600, 650)


def draw():
    """https://py.processing.org/reference/draw.html"""
    if jeu["sauvegarde"]["debug"]:  # Utilisation d'une option modifiable par l'utilisateur car coûteuse en performances
        debug(jeu)

    if jeu["statut"] == 1:
        jeu_module.afficher(jeu)
    else:
        menu_module.interface(jeu)


def keyPressed():
    """https://py.processing.org/reference/keyPressed.html
    Permet au joueur d'interagir avec ses touches du clavier.
    """
    if jeu["statut"] == 1:
        jeu_module.clavier(jeu)
    else:
        menu_module.clavier(jeu)


def mouseMoved():
    """https://py.processing.org/reference/mouseMoved.html
    Permet au joueur d'interagir en bougeant sa souris.
    """
    if jeu["statut"] != 1:
        menu_module.souris(jeu, False)


def mouseClicked():
    """https://py.processing.org/reference/mouseClicked.html
    Permet au joueur d'interagir en cliquant avec sa souris.
    """
    if jeu["statut"] != 1:
        menu_module.souris(jeu, True)
