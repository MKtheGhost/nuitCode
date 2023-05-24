import pyxel, random

#test

class Jeu:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code")
        pyxel.run(self.update, self.draw)
        
 


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