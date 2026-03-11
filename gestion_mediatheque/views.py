import logging
from django.http import HttpResponse
from .models import Livre, Dvd, Cd, Membre
logger = logging.getLogger(__name__)

def accueil(request):
    logger.info("Accès à la page d'accueil")
    contenu = """
    <h1>Bienvenue sur l'application de gestion de médiathèque</h1>
    <ul>
        <li><a href="/bibliothecaire/">Espace bibliothécaire</a></li>
        <li><a href="/membre/">Espace membre</a></li>
        <li><a href="/medias/">Liste des médias</a></li>
        <li><a href="/membres/">Liste des membres</a></li>
    </ul>
    """
    return HttpResponse(contenu)


def menu_bibliothecaire(request):
    logger.info("Accès à l'espace bibliothécaire")
    contenu = """
    <h1>Espace bibliothécaire</h1>
    <ul>
        <li><a href="/medias/">Afficher la liste des médias</a></li>
        <li><a href="/membres/">Afficher la liste des membres</a></li>
    </ul>
    """
    return HttpResponse(contenu)


def menu_membre(request):
    logger.info("Accès à l'espace membre")
    contenu = """
    <h1>Espace membre</h1>
    <ul>
        <li><a href="/medias/">Consulter la liste des médias</a></li>
    </ul>
    """
    return HttpResponse(contenu)


def liste_medias(request):
    logger.info("Consultation de la liste des médias")
    livres = Livre.objects.all()
    dvds = Dvd.objects.all()
    cds = Cd.objects.all()

    contenu = "<h1>Liste des médias</h1>"

    contenu += "<h2>Livres</h2><ul>"
    for livre in livres:
        contenu += f"<li>{livre.titre} - {livre.auteur}</li>"
    contenu += "</ul>"

    contenu += "<h2>DVD</h2><ul>"
    for dvd in dvds:
        contenu += f"<li>{dvd.titre} - {dvd.realisateur}</li>"
    contenu += "</ul>"

    contenu += "<h2>CD</h2><ul>"
    for cd in cds:
        contenu += f"<li>{cd.titre} - {cd.artiste}</li>"
    contenu += "</ul>"

    contenu += '<p><a href="/bibliothecaire/">Retour espace bibliothécaire</a></p>'
    return HttpResponse(contenu)


def liste_membres(request):
    logger.info("Consultation de la liste des médias")
    membres = Membre.objects.all()

    contenu = "<h1>Liste des membres</h1><ul>"
    for membre in membres:
        contenu += f"<li>{membre.prenom} {membre.nom} - {membre.email}</li>"
    contenu += "</ul>"

    contenu += '<p><a href="/bibliothecaire/">Retour espace bibliothécaire</a></p>'
    return HttpResponse(contenu)