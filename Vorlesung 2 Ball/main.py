#########################################################################
# Import:     Alle Abhängigkeiten werden am Anfang eingebunden
#########################################################################

import pygame   # die Spiele-Engine
import random   # Zufallszahlen brauchen wir immer...
import os       # Das Dateisystem

#########################################################################
# Settings:   Hier stehen alle Konstanten Variablen für das Spiel.
#             Diese könnten auch ausgelagert werden in settings.py
#             und per import eingebunden werden
#########################################################################

WIDTH = 400       # Breite des Bildschirms in Pixeln
HEIGHT = 300       # Höhe des Bildschirms in Pixeln
FPS = 60        # Frames per Second (30 oder 60 FPS sind üblicher Standard)

#########################################################################
# Initialisierung:    pygame wird gestartet
#                     und eine Bildschirm-Ausgabe wird generiert
#########################################################################

pygame.init()           # pygame Initialisierung
pygame.mixer.init()     # Die Sound-Ausgabe wird initialisiert
pygame.display.set_caption("My Game")   # Überschrift des Fensters

#########################################################################
# Das Clock-Objekt:    Damit lassen sich Frames und Zeiten messen
#                      Sehr wichtig für Animationen etc.
#########################################################################

clock = pygame.time.Clock()

#########################################################################
# Das screen-Objekt:    Auf dem screen werden alle Grafiken gerendert
# Cooles Feature: pygame.SCALED(verdoppelte Auflösung für einen Retro-Effekt)
#########################################################################

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)

#########################################################################
# Grafiken:    Das Einbinden von Grafiken kann auch ausgelagert werden
#########################################################################

# Das Dateisystem ermittelt das aktuelle Verzeichnis
game_folder = os.path.dirname(__file__)

# Flyweight-Pattern Dictionary von Sprites-Images
sprite_images = {}
sprite_images["ball"] = pygame.image.load(os.path.join(game_folder, 'ball.png')).convert_alpha()
for i in range(1,9,1):
    sprite_images["coin"+str(i)] = pygame.image.load(os.path.join(game_folder, '_images/coin'+str(i)+'.png')).convert_alpha()

# Wir binden eine Grafik (Ball) ein
# convert_alpha lässt eine PNG-Datei transparent erscheinen

class Ball():
    def __init__(self, x, y, sx, sy):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.image = sprite_images["coin1"]
        self.imageRect = self.image.get_rect()
        self.timer = 0
        self.anim_frames = 8
        self.act_frame = 1
        self.max_ticks_anim = 0.6 * FPS / self.anim_frames # in 2 sec einmal drehen

    def update(self):
        # Animation
        self.timer += 1
        if self.timer >= self.max_ticks_anim:
            self.timer = 0
            self.act_frame += 1
            if self.act_frame > self.anim_frames:
                self.act_frame = 1
            self.image = sprite_images["coin" + str(self.act_frame)]

        self.x = self.x + self.sx
        self.y = self.y + self.sy
        self.imageRect.topleft = (self.x,self.y)

        if self.imageRect.right >= WIDTH or self.imageRect.left <= 0:
            self.sx *= -1

        if self.imageRect.bottom >= HEIGHT or self.imageRect.top <= 0:
            self.sy *= -1


sprites = []
# Sprite Factory
for _ in range(3):
    sprites.append(Ball(random.randint(64, WIDTH - 64),
                        random.randint(64, HEIGHT - 64),
                        random.choice([-3, -2, -1, 1, 2, 3]),
                        random.choice([-3, -2, -1, 1, 2, 3])))


#########################################################################
# Game Loop:  Hier ist das Herzstück des Templates
# Im Game Loop laufen immer 5 Phasen ab:
# 1. Wait: Die Zeit zwischen 2 Frames wird mit Wartezeit gefüllt
# 2. Input: Alle (Input-)Events werden verarbeitet (Maus, Tastatur, etc.)
# 3. Update: Alle Sprites werden aktualisert inkl. Spiellogik
# 4. Render: Alle Sprites werden auf den Bildschirm gezeichnet
# 5. Double Buffering: Der Screen wird geswitcht und angezeigt
#########################################################################
running = True

while running:
    #########################################################################
    # 1. Wait-Phase:
    # Die pygame-interne Funktion clock.tick(FPS) berechnet die
    # tatsächliche Zeit zwischen zwei Frames und limitiert diese
    # auf einen Wert(z. B. 1/60). Diese tatsächliche verbrauchte
    # Zeit wird dann bei der Aktualisierung des Spiels benötigt,
    # um dieGeschwindigkeit der Objekte anzupassen.

    dt = clock.tick(FPS) / 1000

    #########################################################################
    # 2. Input-Phase:
    # Mit pygame.event.get() leeren wir den Event-Speicher.
    # Das ist wichtig, sonst läuft dieser voll und das Spiel stürzt ab.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Windows Close Button?
            running = False             # dann raus aus dem Game Loop

    #########################################################################
    # 3. Update-Phase: Hier ist die komplette Game Logik untergebracht.
    for sprite in sprites:
        sprite.update()

    #########################################################################
    # 4. Render-Phase: Zeichne alles auf den Bildschirm

    # Hintergrund
    screen.fill((255, 255, 255))    # RGB Weiß

    # Zeichne Objekte an Position auf den Screen
    for sprite in sprites:
        screen.blit(sprite.image, sprite.imageRect)

    #########################################################################
    # 5. Double Buffering

    pygame.display.flip()

###########################
# Spiel verlassen: quit

pygame.quit()
