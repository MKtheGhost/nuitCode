import pyxel, random

<<<<<<< HEAD
=======
T_OBS = (2,1)
T_ESC = (2,4)
>>>>>>> fc19f24e09d90cc73012c539a101ff9f9c5a55ad

class Jeu:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code", fps = 60)
        pyxel.load(filename = "images.pyxres")
        self.x = 0
        self.player_x = 60
<<<<<<< HEAD
        self.player_y = 100
        self.pas = 0
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 8)
=======
        self.player_y = 110
        self.obstacles = []
>>>>>>> fc19f24e09d90cc73012c539a101ff9f9c5a55ad
        pyxel.run(self.update, self.draw)

    def update(self) :
        if pyxel.btnp(pyxel.KEY_Q) :
            pyxel.quit()

        self.vaisseau_deplacement()
<<<<<<< HEAD
        self.compteur_de_pas()
        
    def draw(self) :
        pyxel.cls(0)
        #pyxel.rect(self.player_x, self.player_y, 8, 8, 9)
        pyxel.blt(self.player_x, self.player_y, 0, 122, 12, 6, 8)
        pyxel.text(5,5, 'PAS:'+ str(pyxel.ceil(self.pas)), 7)
=======
        self.obstacles_creation()
        self.obstacles_sup()
        
    def draw(self) :
        pyxel.cls(0)
        pyxel.blt(self.player_x, self.player_y, 0, 122, 12, 6, 8)
        # obstacles
        for o in self.obstacles:
            pyxel.blt(o[0], o[1], 0, 0, 8, 8, 8)
>>>>>>> fc19f24e09d90cc73012c539a101ff9f9c5a55ad

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
<<<<<<< HEAD


    def compteur_de_pas(self) :
        if pyxel.btn(pyxel.KEY_UP) and self.player_y > 0 :
            self.pas += 0.1



=======
    
    def obstacles_creation(self):
        if (pyxel.frame_count % 30 == 0):
            self.obstacles.append([random.randint(0, 120), 0])

    def obstacles_sup(self):
        for o in self.obstacles:
            if o[0] <= self.player_x+8 and o[1] <= self.player_y+8 >= self.player_x and o[1]+8 >= self.player_y:
                self.obstacles.remove(o)

    def apparition_obst(self, y1, y2):
        yt1 = pyxel(y1 / 8)
        yt2 = pyxel(y2 / 8)

        for y in range(yt1, yt2 + 1):
            for x in range(16):
                t = pyxel.tilemap(0).pget(x, y)
                if t == T_OBS:
                    pyxel.tilemap(0).pset(x, y, T_ESP)
                    self.obstacles.append([x*8, y*8-y1])
>>>>>>> fc19f24e09d90cc73012c539a101ff9f9c5a55ad

Jeu()