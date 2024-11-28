def isPalindrom(value):
    return value == value[::-1]

values = [
    'Karol',
    'Home',
    'LoL',
    'Lol',
    'RAR',
    'Billie Eilish',
    'GOG',
    'RRRRRRRRRRRRR',
]

for value in values:
    print(f'{value:<15} is {"not " if not isPalindrom(value) else ""}a palindrom')