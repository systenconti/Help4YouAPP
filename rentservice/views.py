from django.shortcuts import render
from .models import Profession, Worker, OrderedService, Service
from django.http import JsonResponse


def home_view(request):
    professions = Profession.objects.all()
    context = {"professions": professions}
    return render(request, "home.html", context)


def get_services_view(request, profession_id):
    services = Service.objects.filter(profession_id=profession_id).order_by("service")
    services_list = [
        {"id": service.id, "service": service.service} for service in services
    ]
    data = {"services": services_list}
    return JsonResponse(data)
