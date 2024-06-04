from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import EnseignantForm, MaterielForm, PassationForm
from .models import Cursus, Student

from django.shortcuts import render, get_object_or_404
from .models import Materiel, Emprunt


def detail(request, cursus_id):
    resp = 'result for cursus {}'.format(cursus_id)
    return HttpResponse(resp)

def index(request):
    result_list = Cursus.objects.order_by('name')
    template = loader.get_template('lycee/index.html')
    context = {
        'list': result_list,
    }
    return HttpResponse(template.render(context, request))

def detail_student(request, student_id):
    result_list = Student.objects.get(pk=student_id)
    context = {'liste': result_list}
    return render(request, 'lycee/student/detail_student.html', context)

def ajouter_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EnseignantForm()
    return render(request, 'lycee/ajouter_enseignant.html', {'form': form})

def ajouter_materiel(request):
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MaterielForm()
    return render(request, 'lycee/ajouter_materiel.html', {'form': form})

def enregistrer_passation(request):
    if request.method == 'POST':
        form = PassationForm(request.POST)
        if form.is_valid():
            passation = form.save()
            materiel = passation.materiel
            materiel.possesseur = passation.possesseur_nouveau
            materiel.save()
            return redirect('index')
    else:
        form = PassationForm()
    return render(request, 'lycee/enregistrer_passation.html', {'form': form})


def liste_materiel(request):
    materiel_list = Materiel.objects.select_related('possesseur').all()
    context = {
        'materiel_list': materiel_list
    }
    return render(request, 'lycee/liste_materiel.html', context)
