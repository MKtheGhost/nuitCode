import pyxel, random


class Jeu:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code", fps = 60)
        pyxel.load("images.pyxres")
        self.x = 0
        self.player_x = 60
        self.player_y = 100
        self.pas = 0
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 8)
        pyxel.run(self.update, self.draw)

    def update(self) :
        if pyxel.btnp(pyxel.KEY_Q) :
            pyxel.quit()

        self.vaisseau_deplacement()
        self.compteur_de_pas()
        
    def draw(self) :
        pyxel.cls(0)
        #pyxel.rect(self.player_x, self.player_y, 8, 8, 9)
        pyxel.blt(self.player_x, self.player_y, 0, 122, 12, 6, 8)
        pyxel.text(5,5, 'PAS:'+ str(pyxel.ceil(self.pas)), 7)

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


    def compteur_de_pas(self) :
        if pyxel.btn(pyxel.KEY_UP) and self.player_y > 0 :
            self.pas += 0.1




Jeu()