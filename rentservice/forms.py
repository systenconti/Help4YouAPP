from django import forms
from .models import OrderedService, Worker
from django.core.exceptions import ValidationError
from datetime import datetime
import random


class PartialOrderedServiceForm(forms.ModelForm):
    profession = forms.CharField(max_length=50)

    class Meta:
        model = OrderedService
        exclude = ["order_date", "worker", "confirmed"]

    def save(self, request=None, commit=True):
        profession = self.cleaned_data.get("profession")
        selected_date = self.cleaned_data.get("service_date")
        selected_time = selected_date.time()
        workers = Worker.objects.filter(profession=profession)
        available_workers = []

        for worker in workers:
            already_ordered_service = OrderedService.objects.filter(
                worker=worker, service_date=selected_date, confirmed=True
            )
            if already_ordered_service or (
                selected_time > worker.work_endtime
                or selected_time < worker.work_starttime
            ):
                continue
            else:
                if worker.work_starttime <= selected_time < worker.work_endtime:
                    available_workers.append(worker)

        if available_workers:
            worker = self.choose_worker(available_workers)
            ordered_service = super().save(commit=False)
            ordered_service.worker = worker
            ordered_service.order_date = datetime.now()
            ordered_service.confirmed = False
            if commit:
                ordered_service.save()
            return ordered_service
        else:
            raise ValidationError(
                """
                There was a problem with settling your service.
                Either our specialists are unavailable for the preferred date or you chose out-of-range working hours.
                Remember that we're available from 8 to 22.
                Please choose another date.
                """
            )

    def choose_worker(self, workers):
        return random.choice(workers)
