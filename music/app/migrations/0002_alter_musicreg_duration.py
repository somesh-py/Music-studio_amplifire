# Generated by Django 4.1.5 on 2023-04-27 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicreg',
            name='duration',
            field=models.CharField(max_length=50),
        ),
    ]
