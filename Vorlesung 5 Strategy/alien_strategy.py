from abc import ABC, abstractmethod

class IBewegungsmuster(ABC):
    @abstractmethod
    def move(self, sprite):
        pass

class BewegungHorizontal(IBewegungsmuster):
    def move(self, sprite):
        sprite.x = sprite.x + 5

class BewegungVertikal(IBewegungsmuster):
    def move(self, sprite):
        sprite.y = sprite.y + 5
        sprite.x = sprite.x - 5

class Alien:
    def __init__(self, bewegungsmuster: IBewegungsmuster):
        self.x = 0
        self.y = 0
        self.bewegungsmuster = bewegungsmuster

    def changeBewegungsmuster(self, bewegungsmuster: IBewegungsmuster):
        self.bewegungsmuster = bewegungsmuster

    def update(self):
        self.bewegungsmuster.move(self)

    def draw(self):
        print(f"({self.x}, {self.y})")


alien1 = Alien(BewegungHorizontal())
for _ in range(5):
    alien1.update()
    alien1.draw()

alien1.changeBewegungsmuster(BewegungVertikal())
for _ in range(5):
    alien1.update()
    alien1.draw()
