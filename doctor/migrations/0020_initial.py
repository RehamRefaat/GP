# Generated by Django 4.1.1 on 2023-02-03 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("doctor", "0019_delete_doctor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                ("Name", models.CharField(max_length=80)),
                ("Gender", models.CharField(max_length=6)),
                ("Region", models.CharField(max_length=50)),
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Phone", models.CharField(max_length=15)),
                ("Password", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "ordering": ["Name"],
            },
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
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("Input", models.ImageField(upload_to="input/%y/%m/%d")),
                ("Output", models.CharField(max_length=500)),
                ("Processnumber", models.CharField(max_length=500)),
                (
                    "Doctors",
                    models.ManyToManyField(
                        through="doctor.Relation", to="doctor.doctor"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="relation",
            name="SerId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="doctor.service"
            ),
        ),
        migrations.AddField(
            model_name="relation",
            name="UserId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="doctor.doctor"
            ),
        ),
    ]