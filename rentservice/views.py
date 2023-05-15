from django.shortcuts import render, redirect
from .models import Profession, Worker, OrderedService, Service
from django.http import JsonResponse
from .forms import PartialOrderedServiceForm
from datetime import datetime
from django.core import serializers


def home_view(request):
    professions = Profession.objects.all()
    if request.method == "POST":
        form = PartialOrderedServiceForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            form_data = serializers.serialize("json", [form.instance])
            request.session["form_data"] = form_data
            return redirect("confirm")
    else:
        form = PartialOrderedServiceForm()
    context = {"professions": professions, "form": form}
    return render(request, "home.html", context)


def confirm_view(request):
    if "form_data" not in request.session:
        return redirect("home")

    form_data = request.session["form_data"]
    deserialized_data = serializers.deserialize("json", form_data)
    ordered_service = next(deserialized_data).object

    service_id = ordered_service.service.id
    client_address = ordered_service.client_address
    client_fullname = ordered_service.client_fullname
    client_email = ordered_service.client_email
    client_mobile = ordered_service.client_mobile
    service_date = ordered_service.service_date

    if request.method == "POST":
        confirmed = request.POST.get("confirm")
        if confirmed == "yes":
            ordered_service.confirmed = True
            ordered_service.save()

            del request.session["form_data"]
            return redirect("success")

        elif confirmed == "no":
            del request.session["form_data"]
            return redirect("dismiss")
    context = {
        "service_id": service_id,
        "client_address": client_address,
        "client_fullname": client_fullname,
        "client_email": client_email,
        "client_mobile": client_mobile,
        "service_date": service_date,
    }
    return render(request, "confirmation.html", context)


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


def success_view(request):
    return render(request, "success.html")


def dismiss_view(request):
    return render(request, "dismiss.html")
