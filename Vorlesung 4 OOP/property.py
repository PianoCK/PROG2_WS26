class Auto:
    ''' Autoklasse mit autotyp: str und preis: float '''
    def __init__(self, autotyp: str, preis: float):        
        self.__autotyp = autotyp
        self.__preis = preis

    @property
    def preis(self):
        return self.__preis

    @preis.setter
    def preis(self, neuerPreis):
        if neuerPreis > 0:
            self.__preis = neuerPreis
        else:
            print("Keine Änderung. Preis muss eine positive Zahl sein.")
        
car = Auto("VW", 30_000)
car.preis = -1000
print(car.preis)
