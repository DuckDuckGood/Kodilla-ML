products = []

while(True):
    product = input("Enter a product name: ")
    if product.upper() == 'EXIT':
        break
    products.append(product)

print(type(input()))