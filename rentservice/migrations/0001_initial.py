# Generated by Django 4.2.1 on 2023-05-12 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_starttime', models.TimeField()),
                ('work_endtime', models.TimeField()),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentservice.profession')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('cost', models.SmallIntegerField()),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentservice.profession')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_fullname', models.CharField(max_length=50)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_mobile', models.CharField(max_length=15)),
                ('client_address', models.CharField()),
                ('order_date', models.DateTimeField()),
                ('service_date', models.DateTimeField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentservice.service')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentservice.worker')),
            ],
        ),
    ]
