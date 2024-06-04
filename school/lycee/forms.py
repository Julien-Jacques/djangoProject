from django import forms
from .models import Enseignant, Materiel, Passation

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['user', 'nom', 'prenom']

class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['name', 'acheteur', 'budget', 'responsable', 'localisation', 'possesseur']

class PassationForm(forms.ModelForm):
    class Meta:
        model = Passation
        fields = ['materiel', 'possesseur_precedent', 'possesseur_nouveau', 'lieu', 'occasion', 'objectif_utilisation']
