products = [
    {'Nome': 'Pão'},    
    {'Nome': 'Açucar'},
    {'Nome': 'Carne'},
]

new_products = [
    product
    for product in products
]

print(products)
print(*new_products, sep = "\n")