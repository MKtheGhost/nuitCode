import pyxel, random

class Jeu:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code", fps = 60)
        pyxel.load("images.pyxres")
        self.x = 0
        self.player_x = 60
        self.player_y = 60
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 8)
        pyxel.run(self.update, self.draw)

    def update(self) :
        if pyxel.btnp(pyxel.KEY_Q) :
            pyxel.quit()
        self.vaisseau_deplacement()
        
    def draw(self) :
        pyxel.cls(0)
        pyxel.rect(self.player_x, self.player_y, 8, 8, 9)

    def vaisseau_deplacement(self):
        """déplacement du personnage"""
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x<120:
            self.player_x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.player_x>0:
            self.player_x -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.player_y<120:
            self.player_y += 1
        if pyxel.btn(pyxel.KEY_UP) and self.player_y>0:
            self.player_y -= 1


class Perso :
    def __init__(self) :
        player_img = pyxel.blt(121, 11, 0, 6, 8)

    

Jeu()