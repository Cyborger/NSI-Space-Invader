# -*- coding: utf-8 -*- voir https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding
import json


def verification_integrite():
    """Permet de s'assurer que le fichier de sauvegarde data/sauvegarde.json existe pour le créer le cas échéant."""
    fichier_sauvegarde = open("data/sauvegarde.json", "a")
    fichier_sauvegarde.close()


def charger():
    """Permet de charger le fichier de sauvegarde data/sauvegarde.json en de le convertir du format json en
    dictionnaire.

    Retourne:
        - dict: Dictionnaire comportant les valeurs de data/sauvegarde.json
    """
    verification_integrite()

    # Récupération de la valeur record dans le fichier data/record.txt
    fichier_sauvegarde = open("data/sauvegarde.json", "r+")
    sauvegarde = fichier_sauvegarde.read()  # Permet de récupérer le contenu du fichier

    if sauvegarde == "":  # Permet d'initialiser le fichier s'il est vide
        sauvegarde = {  # Valeurs du fichier sauvegarde par défaut
            "record": 0,
            "couleur": "vert",
            "vies": 3,
            "max_ennemis": 3,
            "vitesse": 1,
            "debug": False
        }
        json.dump(sauvegarde, fichier_sauvegarde)
    else:
        sauvegarde = json.loads(sauvegarde)  # Permet de charger les valeurs du fichier en dictionnaire

    fichier_sauvegarde.close()
    return sauvegarde


def sauvegarder(dictionnaire):
    """Permet de sauvegarder le dictionnaire en paramètre dans le fichier de sauvegarde data/sauvegarde.json en le
    convertissant d'un dictionnaire au format json. Cette fonction réécrit le contenu du fichier sans en prendre compte.

    Paramètre:
        - dict dictionnaire: Dictionnaire à sauvegarde dans le fichier.
    """
    verification_integrite()

    fichier_sauvegarde = open("data/sauvegarde.json", "w")
    json.dump(dictionnaire, fichier_sauvegarde)

    fichier_sauvegarde.close()