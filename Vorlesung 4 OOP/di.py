from abc import ABC, abstractmethod

# Interface Werkzeug
class IWerkzeug(ABC):
    @abstractmethod
    def benutze(self):
        pass

class Spaten(IWerkzeug):
    def benutze(self):
        print("...graben...")

class Bagger(IWerkzeug):
    def benutze(self):
        print("... tief graben...")

class Spitzhacke(IWerkzeug):
    def benutze():
        print("... hacken ...")

class Knecht:
    def __init__(self):
        self.werkzeug = None

    def gibWerkzeug(self, werkzeug: IWerkzeug):
        self.werkzeug = werkzeug

    def benutzeWerkzeug(self):
        self.werkzeug.benutze()


spaten = Spaten()
bagger = Bagger()
hein = Knecht()
hein.gibWerkzeug(bagger)
hein.benutzeWerkzeug()
