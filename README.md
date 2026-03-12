# Application de gestion de médiathèque

## Présentation

Ce projet est une application web développée avec le framework Django.
Elle permet de gérer une médiathèque avec des médias (livres, DVD, CD),
des membres et des emprunts.

## Fonctionnalités

- gestion des médias
- gestion des membres
- gestion des emprunts
- interface d’administration Django
- consultation des médias
- règles métier pour les emprunts
- tests automatiques
### Interface bibliothécaire

- afficher la liste des membres
- ajouter un membre
- modifier un membre
- supprimer un membre
- afficher la liste des médias
- ajouter un média
- créer un emprunt
- enregistrer le retour d’un emprunt

### Interface membre

- consulter la liste des médias disponibles

## Technologies utilisées

- Python
- Django
- SQLite

## Installation

Installer Django :

pip install django

## Initialiser la base de données

python manage.py migrate

## Lancer le serveur

python manage.py runserver

Puis ouvrir :

http://127.0.0.1:8000/

## Accès administration

http://127.0.0.1:8000/admin/

## Documentation du projet

Le rapport complet du projet (analyse, conception et explications du code) est disponible dans le document suivant :

➡️ [Voir le rapport du projet](docs/Rapport_projet_mediatheque.pdf)