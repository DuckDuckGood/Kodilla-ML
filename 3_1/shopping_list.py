# 1
print('Shopping list')

shopsAndProducts = {
    'bakery':          ['Bread', 'Donut', 'Rolls'],
    'vegetable shop':  ['Carrot', 'Celery', 'Rucola'],
}

productsSum = 0
for name, products in shopsAndProducts.items():
    print(f"I'm going to {name}, where I'll buy {products}")
    productsSum += len(products)
print(f'I buy {productsSum} in total')

print()

# 2
numbers = [i for i in range(101) if i % 5 == 0]
for i in numbers:
    print(f'{i:<8}', end='|')
print()
for i in numbers:
    print(f'{i**3:<8}', end='|')
