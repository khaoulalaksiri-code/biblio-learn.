
from django.shortcuts import render
from .forms import ContactForm
from catalogue.models import Ressource


def accueil(request):
    contexte = {
        "nom_projet": "BiblioLearn",
        "modules": ["Catalogue", "Comptes et rôles", "Emprunts", "Mini-cours"],
        "nb_ressources": Ressource.objects.count(),
    }
    return render(request, "pages/accueil.html", contexte)


def a_propos(request):
    contexte = {
        "version_projet": "Version 1.0 - TP1",
        "equipe": [
            {"nom": "Khaoula", "role": "Développeuse"},
            {"nom": "khaoula1", "role": "Designer"},
            {"nom": "khaoula2", "role": "Chef de projet"},
        ]
    }
    return render(request, "pages/a_propos.html", contexte)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            nom = form.cleaned_data["nom"]
            return render(request, "pages/contact.html", {
                "form": form,
                "nom": nom,
                "envoye": True
            })
    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})
