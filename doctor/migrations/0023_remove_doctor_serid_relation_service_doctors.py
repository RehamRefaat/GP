# Generated by Django 4.1.1 on 2023-02-04 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0022_remove_service_doctors_doctor_serid_delete_relation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="SerId",
        ),
        migrations.CreateModel(
            name="Relation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Date", models.DateTimeField(auto_now_add=True)),
                (
                    "SerId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="doctor.service"
                    ),
                ),
                (
                    "UserId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="doctor.doctor"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="service",
            name="Doctors",
            field=models.ManyToManyField(through="doctor.Relation", to="doctor.doctor"),
        ),
    ]