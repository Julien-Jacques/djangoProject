from django.db import models
from django.utils import timezone

class Cursus(models.Model):
    name = models.CharField(max_length=255)
    year_from_bac = models.IntegerField()
    scholar_year = models.CharField(max_length=9)

    def __str__(self):
        return self.name

class Student(models.Model):
    cursus = models.ForeignKey(Cursus, on_delete=models.CASCADE, default="")
    last_name = models.CharField(max_length=255, default="")
    first_name = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=10, default="")
    email = models.EmailField(default="")
    birth_date = models.DateTimeField(default=timezone.now)
    comments = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Budget(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Enseignant(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Materiel(models.Model):
    name = models.CharField(max_length=100)
    acheteur = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='acheteur')
    budget = models.CharField(max_length=100, default='')
    responsable = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='responsable')
    localisation = models.CharField(max_length=100)
    possesseur = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='possesseur')

    def __str__(self):
        return self.name

class Passation(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    possesseur_precedent = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='possesseur_precedent')
    possesseur_nouveau = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='possesseur_nouveau')
    date = models.DateTimeField(auto_now_add=True)
    lieu = models.CharField(max_length=100)
    occasion = models.CharField(max_length=100)
    objectif_utilisation = models.TextField()

    def __str__(self):
        return f"Passation de {self.materiel.name} de {self.possesseur_precedent} à {self.possesseur_nouveau}"


class Emprunt(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE, related_name='emprunts')
    possesseur_precedent = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, blank=True, related_name='emprunts_realises')
    possesseur_nouveau = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, blank=True, related_name='emprunts_recus')
    date_emprunt = models.DateTimeField(default=timezone.now)
    lieu = models.CharField(max_length=255)
    occasion = models.CharField(max_length=255)
    objectif_utilisation = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.materiel.nom} emprunté par {self.possesseur_nouveau} le {self.date_emprunt}"