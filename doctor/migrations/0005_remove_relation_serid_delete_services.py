# Generated by Django 4.1.1 on 2023-01-16 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0004_relation_services_delete_operations_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="relation",
            name="SerId",
        ),
        migrations.DeleteModel(
            name="Services",
        ),
    ]