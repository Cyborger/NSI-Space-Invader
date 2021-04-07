# NSI - Projet n°3
*Instructions de projet*

L'objectif de ce projet est de réaliser un jeu "Space Invader" en langage Python sur Processing.

Votre programme devra comporter:

- Un écran d'accueil pour démarrer le jeu
- Le jeu
- Un écran de sortie à la fin du jeu

## Le jeu
*Une vidéo est jointe au projet pour vous permettre de mieux comprendre les attendus*

1. Le vaisseau du joueur

    - se déplace horizontalement en bas de la fenêtre graphique à l'aide des flèches du clavier.
    - tire des balles pour détruire le vaisseau ennemi.

2. Le vaisseau ennemi

    - apparaît en haut de la fenêtre graphique : horizontalement, sa position est aléatoire.
    - descend en rebondissant sur les bords verticaux de la fenêtre graphique.

3. Le vaisseau du joueur tire des balles pour détruire le vaisseau ennemi.

4. Le vaisseau du joueur, le vaisseau ennemi et les balles devront être implémentés à l'aide de dictionnaires. Vous devrez définir les caractéristiques de chacun de ces objets. Le vaisseau du joueur et le vaisseau ennemi devront comporter la caractéristique "est_vivant", la valeur associée sera un booléen.

5. Si le vaisseau ennemi est touché, il explose et disparaît.

6. Dès qu'un vaisseau ennemi arrive en bas de la fenêtre graphique ou est détruit, un nouveau vaisseau ennemi apparaît en haut de la fenêtre graphique.

7. Si le vaisseau ennemi percute le vaisseau du joueur, celui-ci explose et disparaît : c'est la fin de la partie.

8. Améliorations possibles *(facultatif)*:

    - affichage du score du joueur
    - nombre de balles limité
    - le joueur a plusieurs vies
    - les vaisseaux ennemis vont de plus en plus vite
    - il y a plusieurs vaisseaux ennemis simultanément
    - les vaisseaux ennemis lâchent des bombes pour détruire le joueur, le joueur peut détruire les bombes en tirant des balles
    - écran de fin : possibilité de rejouer...

Toutes les images sont disponibles au format png dans le dossier compressé zip.

Vous devrez également rédiger un rapport d'une page environ au format pdf pour répondre aux trois questions suivantes :

1. Préciser les caractéristiques utilisées dans vos dictionnaires pour définir le vaisseau du joueur, le vaisseau ennemi et une balle.

2. Décrire l'arborescence de votre programme.

3. Expliquer comment vous avez défini la "collision de deux images".

## Critères

- Résultat final
- Implication en classe durant les séances de projet
- Respet des consignes
- Organisation et propreté du code informatique
- Présence de commentaires dans le code (avec #)
- Spécifications des fonctions (\"""....\""")
- Rapport clair avec un contenu significatif

Remarque :
Une question orale portant sur le code informatique pourra être posée à certains élèves à l'issue du projet.

## Délai

Remise du projet au format compressé au plus tard le 10/05/2021 sur l'espace pédagogique de Toutatice.