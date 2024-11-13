# cubes
cubes = [number**3 for number in range(1, 11)]
for cube in [cube for cube in cubes if cube % 2 != 0]:
    print(cube)
print('\n')

# numbers
numbers = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
zeros = [number for number in numbers if number == 0]
nonZeros = [number for number in numbers if number != 0]
print(f'{'zeros':<10}', zeros)
print(f'{'nonZeros':<10}', nonZeros)
