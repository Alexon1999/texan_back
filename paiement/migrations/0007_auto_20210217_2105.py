# Generated by Django 3.1.6 on 2021-02-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0006_auto_20210217_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panier',
            name='panier_items',
        ),
        migrations.AlterField(
            model_name='panier',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='menus',
            field=models.ManyToManyField(blank=True, to='paiement.Panier_menu'),
        ),
        migrations.AlterField(
            model_name='panier',
            name='produits',
            field=models.ManyToManyField(blank=True, to='paiement.Panier_produit'),
        ),
        migrations.DeleteModel(
            name='Panier_item',
        ),
    ]
