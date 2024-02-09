from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    shelf_life = models.IntegerField()
    inventory = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    min_selling_price = models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
    customer_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    avg_time_to_buy = models.FloatField()

class Transaction(models.Model):
    product_id = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    action = models.CharField(max_length=50)

class CompetitorPrice(models.Model):
    price_id = models.CharField(max_length=50, primary_key=True)
    product_id = models.CharField(max_length=50)
    competitor_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class MarketData(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True)
    total_sales = models.IntegerField()
    trends = models.CharField(max_length=100)
    avg_selling_price = models.DecimalField(max_digits=10, decimal_places=2)
