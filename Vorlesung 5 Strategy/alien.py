class Alien:
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        self.x = self.x + 5

    def draw(self):
        print(f"({self.x}, {self.y})")

alien1 = Alien()

for _ in range(5):
    alien1.update()
    alien1.draw()

