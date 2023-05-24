import pyxel, random

#test

player_x, player_y = 
class Jeu:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code")
        pyxel.run(self.update(), self.draw())

    def update() :
        global vaisseau_x, vaisseau_y, tirs_liste
        pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

        if pyxel.btpn(pyxel.KEY_Q) :
            pyxel.quit()

    def draw() :
        pyxel.cls(0)

        pyxel.rect(10, 10, 20, 20, 11)
        


class Perso :
    def __init__(x, y) :
        player_img = pyxel.blt(121, 11, 0, 6, 8)
        player_x = x
        player_y = y

    def vaisseau_deplacement(x, y):

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

#pyxel.load(filename="images.pyxres")

Jeu()