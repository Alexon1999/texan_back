# Generated by Django 3.1.6 on 2021-02-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_auto_20210217_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='libelle',
            field=models.CharField(max_length=50),
        ),
    ]
