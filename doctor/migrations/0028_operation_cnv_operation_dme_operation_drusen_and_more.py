# Generated by Django 4.1.5 on 2023-04-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0027_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='CNV',
            field=models.CharField(default='0', max_length=5),
        ),
        migrations.AddField(
            model_name='operation',
            name='DME',
            field=models.CharField(default='0', max_length=5),
        ),
        migrations.AddField(
            model_name='operation',
            name='Drusen',
            field=models.CharField(default='0', max_length=5),
        ),
        migrations.AddField(
            model_name='operation',
            name='Normal',
            field=models.CharField(default='0', max_length=5),
        ),
        migrations.AlterField(
            model_name='operation',
            name='Processnumber',
            field=models.CharField(default='1', max_length=5),
        ),
    ]