# Generated by Django 4.2.12 on 2024-07-12 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='Cédula o RUC'),
        ),
    ]