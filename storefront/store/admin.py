from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Customer, Transaction, CompetitorPrice, MarketData

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'name', 'type', 'category', 'shelf_life', 'inventory', 'price', 'min_selling_price']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'name', 'avg_time_to_buy']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'customer_id', 'timestamp', 'action']

@admin.register(CompetitorPrice)
class CompetitorPriceAdmin(admin.ModelAdmin):
    list_display = ['price_id', 'product_id', 'competitor_name', 'timestamp', 'price']

@admin.register(MarketData)
class MarketDataAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'total_sales', 'trends', 'avg_selling_price']
