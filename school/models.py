# authentication/models.py
from contextlib import nullcontext
from email.policy import default
from turtle import title
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings



class etablissement(models.Model):
    nom=models.CharField(max_length=100, null=True)
    Telephone=models.IntegerField(null=True)
    def __str__(self):
        return self.nom

class User(AbstractUser):
    
    prof = 'prof'
    eleve = 'eleve'
    tuteur='tuteur'

    ROLE_CHOICES = (
        (prof, 'prof'),
        (eleve, 'eleve'),
        (tuteur, 'tuteur'),

    )
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    etablissement=models.OneToOneField(etablissement, null=True, on_delete=models.CASCADE)

class Matiere(models.Model):
    nom=models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nom





class Eleve(models.Model):
    username=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    nom=models.CharField(max_length=100, null=False)
    prenom=models.CharField(max_length=100, null=False)
    tel=models.IntegerField(null=False, default=0)
    addresse=models.CharField(max_length=100, null=False)
    date_birth=models.DateTimeField()
    Cne=models.IntegerField(null=False)
    etablissement=models.OneToOneField(etablissement, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nom} {self.prenom}'


class Devoir(models.Model):
    matiere=models.ForeignKey(Matiere, on_delete=models.CASCADE)
    date=models.DateTimeField(null=False)
    # def note(self):
    #     eleve =models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    note = models.IntegerField(null=True, default='0')

    def __str__(self):
        return f"devoir de {self.matiere}: {self.note}"

class Note(models.Model):
    matiere=models.ForeignKey(Matiere.__name__, on_delete=models.CASCADE)
    eleve=models.ForeignKey(User, on_delete=models.CASCADE)
    valeur=models.IntegerField(null=True, default='0')

    def __str__(self):
        return f" {self.matiere} | {self.eleve.first_name} {self.eleve.last_name} : {self.valeur}"


class Professeur(models.Model):
    nom=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prenom=models.CharField(max_length=100, null=False)
    tel=models.IntegerField(null=False, default=0)
    addresse=models.CharField(max_length=100, null=False)




class Info(models.Model):
    titre=models.CharField(max_length=100, null=False)
    datePub=models.DateField(auto_now_add=True)
    content=models.CharField(max_length=200, null=False)
    date=models.DateTimeField(null=True, blank=True)

    def str(self):
        return self.titre

class Cour(models.Model):
    titre=models.CharField(max_length=100,null=False)
    chapitre=models.CharField(max_length=100, null=False)
    contenu=models.FileField(null=True)
