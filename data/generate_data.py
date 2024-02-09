import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# Set a seed for reproducibility
np.random.seed(42)

# Define common grocery items and services
grocery_items = [
    'Milk', 'Eggs', 'Bread', 'Bananas', 'Chicken', 'Rice', 'Cheese', 'Apples', 'Tomatoes', 'Potatoes',
    'Pasta', 'Ground Beef', 'Butter', 'Cereal', 'Onions', 'Carrots', 'Spinach', 'Orange Juice', 'Yogurt', 'Coffee',
    'Salmon', 'Lettuce', 'Strawberries', 'Broccoli', 'Peanut Butter', 'Almond Milk', 'Oatmeal', 'Grapes', 'Avocado',
    'Cucumber', 'Cheddar Cheese', 'Bell Peppers', 'Honey', 'Sausages', 'Shrimp', 'Bacon', 'Canned Beans', 'Olive Oil',
    'Frozen Peas', 'Lemon', 'Watermelon', 'Ice Cream', 'Asparagus', 'Soy Sauce', 'Ground Turkey', 'Walnuts', 'Blueberries'
]

services = [
    'Plumbing Service', 'Web Design', 'Consultation', 'Home Cleaning', 'Graphic Design', 'Legal Advice',
    'Fitness Training', 'Event Planning', 'Photography Session', 'Tutoring', 'Massage Therapy', 'Software Development',
    'Financial Consulting', 'Landscaping Service', 'Language Translation', 'Personal Chef', 'Car Detailing',
    'Virtual Assistance', 'Interior Design'
]

# Number of records to generate
num_groceries = len(grocery_items)
num_services = len(services)
num_customers = 50
num_transactions = 1000
num_competitor_prices = 200
num_market_data_entries = 100

# Generate Product data including grocery items and services
products_data = []
categories = ['Groceries', 'Services']

# Goods data
for _ in range(num_groceries):
    product_name = np.random.choice(grocery_items)
    price = round(np.random.uniform(150, 1000))
    minimum_selling_price = round(0.8 * price)  
    products_data.append({
        'ProductId': len(products_data) + 1,
        'Name': product_name,
        'Type': 'good',
        'Category': 'Groceries',
        'ShelfLife': round(np.random.randint(1, 365)),
        'Inventory': round(np.random.randint(1, 100)),
        'Price': price,
        'MinimumSellingPrice': minimum_selling_price
    })

# Services data
for _ in range(num_services):
    service_name = np.random.choice(services)
    products_data.append({
        'ProductId': len(products_data) + 1,
        'Name': service_name,
        'Type': 'service',
        'Category': 'Services',
        'ShelfLife': None,
        'Inventory': None,
        'Price': np.random.uniform(20, 200),
        'MinimumSellingPrice': np.random.uniform(10, 50)
    })

# Generate Customer data
customers = pd.DataFrame({
    'CustomerId': range(1, num_customers + 1),
    'Name': [fake.name() for _ in range(num_customers)],
    'AverageTimeToBuy': np.random.uniform(1, 60, num_customers)
})

# Generate Transaction data
transaction_actions = ['search', 'addtocart', 'purchase']

transactions = pd.DataFrame({
    'ProductId': np.random.choice([p['ProductId'] for p in products_data], num_transactions),
    'CustomerId': np.random.choice(customers['CustomerId'], num_transactions),
    'Timestamp': [fake.date_time_this_year() for _ in range(num_transactions)],
    'Action': np.random.choice(transaction_actions, num_transactions, p=[0.6, 0.3, 0.1])
})

# Generate Competitor Price data
competitor_prices = pd.DataFrame({
    'Id': range(1, num_competitor_prices + 1),
    'ProductId': np.random.choice([p['ProductId'] for p in products_data], num_competitor_prices),
    'CompetitorName': np.random.choice(['Amazon', 'Flipkart', 'Walmart'], num_competitor_prices),
    'Timestamp': [fake.date_time_this_year() for _ in range(num_competitor_prices)]
})

# Ensure competitor prices are within +-40% of product prices
product_prices = {p['ProductId']: p['Price'] for p in products_data}
competitor_prices['Price'] = [round(np.random.uniform(0.6 * product_prices[pid], 1.4 * product_prices[pid])) for pid in competitor_prices['ProductId']]

# Generate Market Data
market_data = pd.DataFrame({
    'ProductId': np.random.choice([p['ProductId'] for p in products_data], num_market_data_entries),
    'TotalSales': np.random.randint(1, 100, num_market_data_entries),
    'Trends': np.random.choice(['up', 'down', 'stable'], num_market_data_entries),
    'AverageSellingPrice': np.random.uniform(10, 50, num_market_data_entries)
})

# Save DataFrames to CSV
products = pd.DataFrame(products_data)
products.to_csv('products.csv', index=False)
customers.to_csv('customers.csv', index=False)
transactions.to_csv('transactions.csv', index=False)
competitor_prices.to_csv('competitor_prices.csv', index=False)
market_data.to_csv('market_data.csv', index=False)
