from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cursus_id>/', views.detail, name='detail'),
    path('student/<int:student_id>/', views.detail_student, name='detail_student'),
    path('ajouter_enseignant/', views.ajouter_enseignant, name='ajouter_enseignant'),
    path('ajouter_materiel/', views.ajouter_materiel, name='ajouter_materiel'),
    path('enregistrer_passation/', views.enregistrer_passation, name='enregistrer_passation'),
    path('liste_materiel/', views.liste_materiel, name='liste_materiel'),
]