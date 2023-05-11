from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=40)
    work_starttime = models.TimeField()
    work_endtime = models.TimeField()

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

    def get_profession(self):
        return self.profession

    def get_start_time(self):
        return self.work_starttime

    def get_end_time(self):
        return self.work_starttime


class Service(models.Model):
    service = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    cost = models.IntegerField()

    def __str__(self) -> str:
        return self.service

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class OrderedService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    client_fullname = models.CharField(max_length=50)
    client_email = models.EmailField()
    client_mobile = models.CharField(max_length=15)
    client_address = models.CharField()
    order_date = models.DateTimeField()
    service_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.service} {self.worker}"

    def get_client_name(self):
        return self.client_fullname

    def get_client_email(self):
        return self.client_email

    def get_client_mobile(self):
        return self.client_mobile

    def get_client_address(self):
        return self.client_address

    def get_orderdate(self):
        return self.order_date

    def get_servicedate(self):
        return self.service_date
