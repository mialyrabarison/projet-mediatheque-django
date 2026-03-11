from datetime import timedelta
from django.test import TestCase
from django.utils import timezone

from .models import Membre, Livre, Emprunt


class VueTests(TestCase):
    def test_page_accueil(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenue sur l'application de gestion de médiathèque")

    def test_page_medias(self):
        Livre.objects.create(titre="Harry Potter", auteur="J.K. Rowling", disponible=True)
        response = self.client.get("/medias/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")

    def test_page_membres(self):
        Membre.objects.create(
            nom="Dupont",
            prenom="Marie",
            email="marie@test.com",
            bloque=False
        )
        response = self.client.get("/membres/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Marie Dupont")


class EmpruntTests(TestCase):
    def setUp(self):
        self.membre = Membre.objects.create(
            nom="Martin",
            prenom="Paul",
            email="paul@test.com",
            bloque=False
        )
        self.livre = Livre.objects.create(
            titre="Le Petit Prince",
            auteur="Saint-Exupéry",
            disponible=True
        )

    def test_date_retour_prevue_automatique(self):
        emprunt = Emprunt.objects.create(membre=self.membre, media=self.livre)
        self.assertEqual(
            emprunt.date_retour_prevue,
            timezone.now().date() + timedelta(days=7)
        )

    def test_est_en_retard(self):
        emprunt = Emprunt.objects.create(membre=self.membre, media=self.livre)
        emprunt.date_retour_prevue = timezone.now().date() - timedelta(days=1)
        emprunt.save()
        self.assertTrue(emprunt.est_en_retard())
