class Product:
    def __init__(self, name, price):
        self.name = str(name)
        self.price = float(price)

    def __str__(self):
        return f"{self.name:<12} ({self.price:.2f} zł)".replace(".",",")