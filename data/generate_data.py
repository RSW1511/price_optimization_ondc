import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Set a seed for reproducibility
np.random.seed(42)

# Number of records to generate
num_products = 100
num_customers = 50
num_transactions = 1000
num_competitor_prices = 500
num_market_data_entries = 100

# Generate Product data
products = pd.DataFrame({
    'ProductId': range(1, num_products + 1),
    'Name': [fake.word() for _ in range(num_products)],
    'Type': np.random.choice(['good', 'service'], num_products),
    'Category': [fake.word() for _ in range(num_products)],
    'ShelfLife': [fake.random_int(min=1, max=365) if t == 'good' else None for t in np.random.choice(['good', 'service'], num_products)],
    'Inventory': np.random.randint(1, 100, num_products),
    'Price': np.random.uniform(5, 100, num_products),
    'MinimumSellingPrice': np.random.uniform(1, 5, num_products)
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
    'ProductId': np.random.choice(products['ProductId'], num_transactions),
    'CustomerId': np.random.choice(customers['CustomerId'], num_transactions),
    'Timestamp': [fake.date_time_this_year() for _ in range(num_transactions)],
    'Action': np.random.choice(transaction_actions, num_transactions, p=[0.6, 0.3, 0.1])
})

# Generate Competitor Price data
competitor_prices = pd.DataFrame({
    'Id': range(1, num_competitor_prices + 1),
    'ProductId': np.random.choice(products['ProductId'], num_competitor_prices),
    'CompetitorName': np.random.choice(['Amazon', 'Flipkart', 'Walmart'], num_competitor_prices),
    'Price': np.random.uniform(5, 100, num_competitor_prices),
    'Timestamp': [fake.date_time_this_year() for _ in range(num_competitor_prices)]
})

# Generate Market Data
market_data = pd.DataFrame({
    'ProductId': np.random.choice(products['ProductId'], num_market_data_entries),
    'TotalSales': np.random.randint(1, 100, num_market_data_entries),
    'Trends': np.random.choice(['up', 'down', 'stable'], num_market_data_entries),
    'AverageSellingPrice': np.random.uniform(10, 50, num_market_data_entries)
})

# Save DataFrames to CSV
products.to_csv('products.csv', index=False)
customers.to_csv('customers.csv', index=False)
transactions.to_csv('transactions.csv', index=False)
competitor_prices.to_csv('competitor_prices.csv', index=False)
market_data.to_csv('market_data.csv', index=False)
