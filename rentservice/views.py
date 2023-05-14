from django.shortcuts import render, redirect
from .models import Profession, Worker, OrderedService, Service
from django.http import JsonResponse
from .forms import PartialOrderedServiceForm
from datetime import datetime


def home_view(request):
    professions = Profession.objects.all()
    if request.method == "POST":
        form = PartialOrderedServiceForm(request.POST)
        if form.is_valid():
            form.save()
            print("form was submitted")
            return redirect("home")
    else:
            form = PartialOrderedServiceForm()
    context = {"professions": professions, "form": form}
    return render(request, "home.html", context)


def get_services_view(request, profession_id):
    services = Service.objects.filter(profession_id=profession_id).order_by("service")
    services_list = [
        {"id": service.id, "service": service.service} for service in services
    ]
    data = {"services": services_list}
    return JsonResponse(data)


def about_view(request):
    return render(request, "about.html")


def contact_view(request):
    return render(request, "contact.html")


def services_view(request):
    return render(request, "services.html")
