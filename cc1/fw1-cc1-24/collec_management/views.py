from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .form import *
from django.shortcuts import get_object_or_404, render
from .models import Collec

def collection_detail(request, id):
    collection = get_object_or_404(Collec, id=id)
    return render(request, 'collec_management/collection_detail.html', {'collection': collection})


def collection_list(request):
    collections = Collec.objects.all()
    return render(request, 'collec_management/collection_list.html', {'collections': collections})
from collec_management.models import *

def presentation (request):
    return render (request,'collec_management/Presentation.html')#pas besoins de présiser templates 

def nouvelle_collec(request):
    if request.method == "POST":
        form = CollecForm(request.POST)
        if form.is_valid():
            collec = form.save(commit=False)  
            collec.creation_date = timezone.now()  
            collec.save()  
            return HttpResponseRedirect(f"/collec/{collec.id}")  
    else:
        form = CollecForm()  

    return render(request, "collec_management/formulaire.html", {"form": form, "button_add" : "Ajouter"})

def check_save(form):
    if form.is_valid():
        collec = form.save(commit = False)
        collec.creation_date = timezone.now()
        collec.save()
    return collec.id

def edit_collec (request, collec_id) :
    collec = get_object_or_404(Collec, pk=collec_id)
    if request.method == "POST" :
        form = CollecForm(request.POST, instance=collec)
        id = check_save(form)
        return HttpResponseRedirect(f"/change/{collec.id}")
    else:
        form = CollecForm(instance = collec)
    return render(
        request,
        "collec_management/modificationCollec.html",
        {"form":form, "button_label" : "Modifier"}
    )

def delete_collection(request, id):
    collec = get_object_or_404(Collec, id=id)
    if request.method == "POST":
        collec.delete()
        return HttpResponseRedirect("/all")

    return render(request, "collec_management/delete_collection.html", {"collec": collec, "button_del" : "Suprimer"})

def principal (request):
    return render (request,'collec_management/Principal.html')#pas besoins de présiser templates 
