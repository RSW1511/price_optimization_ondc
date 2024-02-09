from django.db import models

class Product:
    def __init__(self, product_id, name, type_, category, shelf_life, inventory, price, min_selling_price):
        self.product_id = product_id
        self.name = name
        self.type = type_
        self.category = category
        self.shelf_life = shelf_life
        self.inventory = inventory
        self.price = price
        self.min_selling_price = min_selling_price

class Customer:
    def __init__(self, customer_id, name, avg_time_to_buy):
        self.customer_id = customer_id
        self.name = name
        self.avg_time_to_buy = avg_time_to_buy

class Transaction:
    def __init__(self, product_id, customer_id, timestamp, action):
        self.product_id = product_id
        self.customer_id = customer_id
        self.timestamp = timestamp
        self.action = action

class CompetitorPrice:
    def __init__(self, price_id, product_id, competitor_name, timestamp, price):
        self.price_id = price_id
        self.product_id = product_id
        self.competitor_name = competitor_name
        self.timestamp = timestamp
        self.price = price

class MarketData:
    def __init__(self, product_id, total_sales, trends, avg_selling_price):
        self.product_id = product_id
        self.total_sales = total_sales
        self.trends = trends
        self.avg_selling_price = avg_selling_price