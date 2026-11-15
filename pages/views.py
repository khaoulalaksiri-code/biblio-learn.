from django.shortcuts import render

def accueil(request):
    contexte = {
        "nom_projet": "BiblioLearn",
        "modules": ["Catalogue", "Comptes et rôles", "Emprunts", "Mini-cours"],
    }
    return render(request, "pages/accueil.html", contexte)

def a_propos(request):
    contexte = {
        "version_projet": "Version 1.0 - TP1"
    }
    return render(request, "pages/a_propos.html", contexte)
