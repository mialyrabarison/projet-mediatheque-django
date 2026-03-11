from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta


class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bloque = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Media(models.Model):
    titre = models.CharField(max_length=200)
    disponible = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Média"
        verbose_name_plural = "Médias"

    def __str__(self):
        return self.titre


class Livre(Media):
    auteur = models.CharField(max_length=150)

    def __str__(self):
        return f"Livre : {self.titre} - {self.auteur}"


class Dvd(Media):
    realisateur = models.CharField(max_length=150)

    def __str__(self):
        return f"DVD : {self.titre} - {self.realisateur}"


class Cd(Media):
    artiste = models.CharField(max_length=150)

    def __str__(self):
        return f"CD : {self.titre} - {self.artiste}"


class JeuDePlateau(models.Model):
    titre = models.CharField(max_length=200)
    createur = models.CharField(max_length=150)
    disponible_consultation = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Jeu de plateau : {self.titre} - {self.createur}"


class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE, related_name="emprunts")
    media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name="emprunts")
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour_prevue = models.DateField(blank=True)
    date_retour_effective = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.date_retour_prevue:
            self.date_retour_prevue = timezone.now().date() + timedelta(days=7)
        super().save(*args, **kwargs)

    def est_en_retard(self):
        return self.date_retour_effective is None and timezone.now().date() > self.date_retour_prevue

    def clean(self):
        if self.membre.bloque:
            raise ValidationError("Ce membre est bloqué et ne peut pas emprunter.")

        if self.media.disponible is False:
            raise ValidationError("Ce média n'est pas disponible.")

        emprunts_actifs = Emprunt.objects.filter(
            membre=self.membre,
            date_retour_effective__isnull=True
        ).count()

        if self.pk is None and emprunts_actifs >= 3:
            raise ValidationError("Un membre ne peut pas avoir plus de 3 emprunts à la fois.")

        emprunt_en_retard = Emprunt.objects.filter(
            membre=self.membre,
            date_retour_effective__isnull=True,
            date_retour_prevue__lt=timezone.now().date()
        ).exists()

        if emprunt_en_retard:
            raise ValidationError("Ce membre a un emprunt en retard et ne peut plus emprunter.")
    def __str__(self):
        return f"{self.membre} emprunte {self.media}"