# Generated by Django 4.1.3 on 2022-11-07 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Clinic_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="appointment_datetime",
            field=models.DateTimeField(),
        ),
    ]
