from django.db import models

#class Product(models.Model):
 #       name=models.CharField(max_length=300)
  #      price=models.FloatField()
   #     description=models.TextField()
    #    count=models.IntegerField()
     #   def __str__(self):
      #      return self.name
        

#class Category(models.Model):
 #       name = models.CharField(max_length=300)
  #      def __str__(self):
   #         return self.name


class Category(models.Model):
    name = models.CharField(max_length=400)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    category_id = models.IntegerField(default=1)
    name = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField(max_length=4000)
    count = models.IntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'category_id': self.category_id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count
        }    

