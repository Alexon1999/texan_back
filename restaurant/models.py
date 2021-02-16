from django.db import models

# Create your models here.


class Ingredient_info(models.Model):
    description = models.TextField(null=True)


class Ingredient(models.Model):
    nom = models.CharField(max_length=50)
    ingredient_info = models.ForeignKey(
        Ingredient_info, on_delete=models.CASCADE)


class Categorie(models.Model):
    nom = models.CharField(max_length=50)


class Produit(models.Model):
    nom = models.CharField(max_length=20, unique=True)
    description = models.TextField(null=True)
    image_url = models.CharField(max_length=2048)
    categorie = models.ForeignKey(
        Categorie, on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(Ingredient)


class Menu(models.Model):
    nom = models.CharField(max_length=20, unique=True)
    description = models.TextField(null=True)
    image_url = models.CharField(max_length=2048)
    produits = models.ManyToManyField(Produit)
