# Generated by Django 4.1.5 on 2023-06-02 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0035_rename_normaloct_operation_normal"),
    ]

    operations = [
        migrations.RenameField(
            model_name="operation",
            old_name="Normal",
            new_name="NormalOCT",
        ),
    ]