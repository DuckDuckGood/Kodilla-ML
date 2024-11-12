# names
names = ["John", "Michael", "Terry", "Eric", "Graham"]
namesDictionary = dict()
for name in names:
    namesDictionary[name] = len(name)

print(namesDictionary)


# prime numbers
def isPrimeNumber(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

numbers = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
primeNumbers = [number for number in numbers if isPrimeNumber(number)]
print(primeNumbers)


# days of the week
daysOfTheWeek = ["monday", "wednesday", "friday", "saturday"]
daysOfTheWeek += ["tuesday", "thursday", "sunday"]
print(daysOfTheWeek)


# tea algorithm
tea_making_steps = [
    "turn on the kettle",
    "find the tea box",
    "pour water into the tea",
    "prepare the cup",
    "put the tea bag into a cup"
]

tea_making_steps.append(tea_making_steps[2])
del tea_making_steps[2]

print(tea_making_steps)
