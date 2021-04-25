import menu_module
import jeu_module
import json  # Pour afficher la variable jeu dans un fichier json externe (debug.json)

if False:  # Me permet d'intégrer les fonctions Processing à mon éditeur
    from lib.Processing3 import *


def debug(output):
    """Affiche la valeur du paramètre output dans la console et l'écrit, après conversion au format JSON, dans le
    fichier debug.json.
    
    Paramètre:
        - output Any: Valeur à afficher. Peut être de tout type. Pas de valeur par défaut.
    """
    debug = open("debug.json", "w")  # Mode d'écriture écrasant pour éviter une taille de fichier élevée
    debug.write(json.dumps(output, skipkeys=True, sort_keys=True, indent=4,
                           default=lambda o: str(o)))  # Indique comment convertir les valeurs objet en str
    debug.close()


def setup():
    """https://py.processing.org/reference/setup.html
    Initialise et globalise la valeur jeu qui contient toutes les valeurs utilisés dans le jeu.
    
    Structure du dictionnaire jeu:
        Valeurs principales:
            - statut: Nombre entier qui défini le statut du jeu
                (0 = Menu principal; 1 = Jeu en cours; 2 = "Game Over"; 3 = Options)
            - scores: Dictionnaire qui comprend les deux scores du jeu
                ("actuel": Utilisé pendant le jeu; "record": Stocke le record dans cette valeur et aussi dans un fichier
            - images: Dictionnaire qui charge les images du jeu
            - polices: Dictionnaire qui charge les polices d'écriture du jeu
            - couleurs: Dictionnaire qui indique les couleurs utilisés
        Valeurs utilisés pour l'affichage du menu:
            - boutons: Liste qui indique les boutons du menu
            - curseur: Nombre entier qui indique le bouton sélectionné par l'utilisateur
        Valeurs utilisés pour le fonctionnement du jeu:
            - joueur: Dictionnaire qui contient les propriétés du joueur
            - ennemis: Liste qui contient les propriétés de chaque ennemi séparé dans leur dictionnaire respectif
            - projectiles: Liste qui contient les propriétés de chaque projectile (joueurs ou ennemis) dans leur
                dictionnaire respectif
        
    Propriétés des entités (joueur, ennemis et projectiles):
        Propriétés partagées entre tous:
            - largeur / longueur: Nombres décimaux qui indiquent la largeur et la longueur de l'entité
                (pour les collisions et la taille de l'image associé)
            - x / y: Nombres décimaux qui indiquent la position de l'entité dans l'espace
        Propriétés pour le joueur:
            - vies: Nombre entier qui indique le nombre de vies restantes au joueur
        Propriété partagée entre le joueur et les ennemis:
            - est_vivant: Booléen qui indique l'état de l'entité
        Propriétés partagées entre les ennemis et les projectiles:
            - orientation: Nombre entier qui défini le sens vers lequel se dirige l'entité
                (ennemis: -1 pour la gauche, 1 pour la droite; projectiles: -1 pour le haut, 1 pour le bas)
            - vitesse: Nombre entier choisi aléatoirement entre 0.5 et 1 qui indique la vitesse de déplacement de
                l'entité dans l'espace
    """
    global jeu

    # Récupération de la valeur record dans le fichier data/record.txt
    fichier_record = open("data/record.txt", "r+")
    record = fichier_record.read()
    if record == "":  # Permet d'initialiser le fichier
        fichier_record.write("0")
        record = 0

    jeu = {
        "statut": 0,
        "scores": {
            "actuel": 0,
            "record": int(record)
        },
        "images": {
            "joueur": loadImage("data/images/joueur.png"),
            "projectile": loadImage("data/images/projectile.png"),
            "ennemi": loadImage("data/images/ennemi.png")
        },
        "polices": {
            "retro": createFont("data/polices/retro.ttf", 28)
        },
        "couleurs": {
            "terminal": (65, 255, 0)
        }
    }

    fichier_record.close()
    size(600, 650)


def draw():
    """https://py.processing.org/reference/draw.html"""
    debug(jeu)

    if jeu["statut"] == 0 or jeu["statut"] == 2:
        menu_module.interface(jeu)
    elif jeu["statut"] == 1:
        jeu_module.afficher(jeu)
    else:
        pass


def keyPressed():
    """https://py.processing.org/reference/keyPressed.html
    Permet au joueur d'intéragir avec ses touches du clavier.
    """
    if jeu["statut"] == 0 or jeu["statut"] == 2:
        menu_module.clavier(jeu)
    elif jeu["statut"] == 1:
        jeu_module.clavier(jeu)


def mouseMoved():
    """https://py.processing.org/reference/mouseMoved.html
    Permet au joueur d'intéragir en bougeant sa souris.
    """
    if jeu["statut"] == 0 or jeu["statut"] == 2:
        menu_module.souris(jeu, False)


def mouseClicked():
    """https://py.processing.org/reference/mouseClicked.html
    Permet au joueur d'intéragir en cliquant avec sa souris.
    """
    if jeu["statut"] == 0 or jeu["statut"] == 2:
        menu_module.souris(jeu, True)
