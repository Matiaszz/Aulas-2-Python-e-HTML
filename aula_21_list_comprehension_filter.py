import pprint

products = [
    {'Nome': 'Pão', 'Preço': 6.99},    
    {'Nome': 'Açucar', 'Preço': 12.00},
    {'Nome': 'Carne', 'Preço': 20.19},
]

new_products = [
    {**product, 'Preço': product['Preço'] - 2.50}
    if product['Preço'] > 15 else {**product}
    for product in products
    if product['Preço'] > 10
    # if (product['Preço'] >= 15 and product['Preço'] - 2.50) > 10
    # também posso fazer assim caso queira incluir o primeiro if
]

'''
print(products)
print('Preços em dia de promoção')
print(*new_products, sep = "\n")
'''

def p(v):
    pprint.pprint(v, sort_dicts = False, width = 40)

p(new_products)
