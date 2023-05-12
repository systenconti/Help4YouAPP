from django.contrib import admin
from .models import Worker, Service, OrderedService, Profession

admin.site.register(Worker)
admin.site.register(Profession)
admin.site.register(Service)
admin.site.register(OrderedService)
