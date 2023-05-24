import pyxel, random

class Perso :
    def __init__(self, x, y) :
        self.player_x = x
        self.player_y = y

    def draw(self) :
        pyxel.cls(0)
        pyxel.rect(60, 0, 8, 8, 9)


    def perso_deplacement(x, y):

        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x < 120) :
                x = x + 1
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 0) :
                x = x - 1
        if pyxel.btn(pyxel.KEY_DOWN):
            if (y < 120) :
                y = y + 1
        if pyxel.btn(pyxel.KEY_UP):
            if (y > 0) :
                y = y - 1
        return x, y


class Jeu:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code", fps = 60)
        pyxel.load(filename = "images.pyxres")
        self.perso = Perso(60, 60)
        pyxel.run(self.update(), self.draw())


    def update(self) :
        if pyxel.btnp(pyxel.KEY_Q) :
            pyxel.quit()

    def draw(self) :
        pyxel.cls(0)
        pyxel.rect(60, 0, 8, 8, 9)
        self.perso.draw()
        
#pyxel.load(filename="images.pyxres")

Jeu()