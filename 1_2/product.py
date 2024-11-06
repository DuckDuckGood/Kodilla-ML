class Product:
    def __init__(self, name, price, grams):
        self.name = str(name)
        self.price = float(price)
        self.grams = float(grams)

    def __str__(self):
        return f"{self.name + ",":<12}{self.grams / 1000:.2f} kg, ({self.price * self.grams / 1000:.2f} zł)".replace(".",",")