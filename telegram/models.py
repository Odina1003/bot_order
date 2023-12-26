from django.db import models

class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30, blank=False)

    def str(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    photo = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    column_5 = models.CharField(max_length=100)

    def str(self):
        return self.name

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)

    def str(self):
        return self.owner

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def str(self):
        return self.product

class Location(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitute = models.FloatField()