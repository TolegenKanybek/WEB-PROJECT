from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }


class Manager(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }


class Category(models.Model):
    name = models.CharField(max_length=300)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class NewProductManager(models.Manager):
    def get_new_clothes(self):
        return super(NewProductManager, self).get_queryset().filter(new=True)


class Products(models.Model):
    name = models.CharField(max_length=600)
    price = models.CharField(max_length=300)
    description = models.TextField(default="description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = NewProductManager()

    def to_json(self):
        return {
            'id': self.id,
            'price': self.price,
            'description': self.description,
            'category': self.category.id,
        }


class User(models.Model):
    username = models.CharField(max_length=400)
    password = models.CharField(max_length=100)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }


class Manager(models.Model):
    username = models.CharField(max_length=400)
    password = models.CharField(max_length=100)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }


class Basket(models.Model):
    products = models.ManyToManyField(Products)