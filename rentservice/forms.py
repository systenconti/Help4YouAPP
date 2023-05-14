from django import forms
from .models import OrderedService, Worker
from datetime import datetime


class PartialOrderedServiceForm(forms.ModelForm):
    profession = forms.CharField(max_length=50)

    class Meta:
        model = OrderedService
        exclude = ["order_date", "worker"]

    def save(self, commit=True):
        profession = self.cleaned_data.get("profession")
        worker = Worker.objects.filter(profession=profession).first()

        if worker:
            self.instance.worker = worker

        if commit:
            ordered_service = super().save(commit=False)
            ordered_service.order_date = datetime.now()
            ordered_service.save()

        return self.instance
