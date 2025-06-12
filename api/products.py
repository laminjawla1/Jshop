import random

products = []

names = ["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch", "Monitor", "Keyboard", "Mouse", "Camera", "Printer"]
categories = ["Electronics", "Accessories", "Office", "Gadgets"]

for i in range(1, 11):
    product = {
        "name": random.choice(names),
        "price": round(random.uniform(50, 2000), 2),
        "category": random.choice(categories),
        "stock": random.randint(0, 100)
    }
    products.append(product)
print(products)