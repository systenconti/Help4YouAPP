from django.contrib import admin
from .models import Worker, Service, OrderedService

# Register your models here.
admin.site.register(Worker)
admin.site.register(Service)
admin.site.register(OrderedService)
