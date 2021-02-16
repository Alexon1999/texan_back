from django.db import models
from restaurant.models import Menu, Produit
# Create your models here.


class Panier_item(models.Model):
    menu = models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    quantite = models.IntegerField()
    prix = models.FloatField()


class Panier(models.Model):
    id = models.AutoField(primary_key=True)
    panier_items = models.ManyToManyField(Panier_item)


class Commande(models.Model):
    date_commande = models.DateTimeField(auto_now_add=True)
    commentaire = models.TextField(null=True)
    panier = models.ForeignKey(Panier, on_delete=models.SET_NULL, null=True)
