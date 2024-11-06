from product import Product

products = [
    Product("roquefort", 12.5, 2000),
    Product("stilton", 11.24, 1000),
    Product("brie", 9.3, 1000),
    Product("gouda", 8.55, 1000),
    Product("edam", 11, 1000),
    Product("parmezan", 16.5, 1000),
    Product("mozzarella", 14, 1300),
    Product("hit", 122.32, 2200),
]

line = "--------------------------------"

print("Raport z zakupów:")
print(line)
productsSum = 0
for product in products:
    print(product)
    productsSum += float(product.price * product.grams / 1000)

print(line)
print(f"{"Suma z zakupów:":<22}{productsSum:.2f} zł")