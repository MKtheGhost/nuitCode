import pyxel, random



T_OBS = (2,1)
T_ESP = (2,4)


class Jeu:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code", fps = 60)
        pyxel.load(filename = "images.pyxres")
        self.x = 0
        self.player_x = 60
        self.player_y = 100
        self.pas = 0
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 8)
        self.obstacles = []

        pyxel.run(self.update, self.draw)

    def update(self) :
        if pyxel.btnp(pyxel.KEY_Q) :
            pyxel.quit()

        if self.player_y <= 115 :
            self.player_y += 0.5

        self.vaisseau_deplacement()
        self.compteur_de_pas()
        self.obstacles_creation()
        self.obstacles_sup()
        self.obstacles_dep()
        
    def draw(self) :
        pyxel.cls(0)
        pyxel.blt(self.player_x, self.player_y, 0, 122, 12, 6, 8)
        self.obstacles_creation()
        self.obstacles_sup()
        pyxel.text(5,120, 'PAS:'+ str(pyxel.ceil(self.pas)), 7)
        
        # obstacles
        for o in self.obstacles:
            pyxel.blt(o[0], o[1], 0, 130, 64, 8, 8)

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

    
    def obstacles_creation(self):
        if (pyxel.frame_count % 80 == 0):
            self.obstacles.append([random.randint(0, 120), 0])

    def obstacles_dep(self):
        for o in self.obstacles:
            o[1] += 1
            if  o[1]>128:
                self.obstacles.remove(o)

    def obstacles_sup(self):
        for o in self.obstacles:
            if o[0] <= self.player_x+8 and o[1] <= self.player_y+8 >= self.player_x and o[1]+8 >= self.player_y:
                self.obstacles.remove(o)

Jeu()