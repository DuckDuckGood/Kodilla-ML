directionsOfTheWorld = ["north", "south"]
directionsOfTheWorld += ["west"]
directionsOfTheWorld.append("east")
print(f"{"directionsOfTheWorld (appending):":<35}", directionsOfTheWorld, end="\n\n")

del directionsOfTheWorld[0:2]
directionsOfTheWorld.remove("west")
print(f"{"directionsOfTheWorld (removing):":<35}", directionsOfTheWorld, end="\n\n")

numbers = [3, 6, 17, 4, 0, -20, 20, 100]
print(f"{"numbers sorting:":<35}", sorted(numbers), end="\n\n")

someSet = {"monday", "tuesday", "wednesday", "thursday", "friday"}
someSet.add("saturday") # it works ;)
someSet.update({"sunday"})
print(f"{"set updating:":<35}", someSet, end="\n\n")

salads = {
    "fruit": ["pineapple", "strawberry", "blueberry"],
    "beetroot": ["beetroot", "goat cheese", "rucola"],
    "mom's": ["peas", "corn", "mayo", "potatoes"]
}

salads["meat"] = ["ham", "chicken", "rice", "cucumber"]
salads["fruit"].append("sugar")
del salads["mom's"]

print("dictionary keys & value printing:")
for saladName, ingredients in salads.items():
    print(f"\t{saladName}:")
    for ingredient in ingredients:
        print(f"\t\t{ingredient}")
