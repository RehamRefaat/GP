# Generated by Django 4.1.5 on 2023-05-01 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0031_alter_operation_opid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='OPID',
        ),
    ]