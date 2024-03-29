import pyxel, random

T_OBS = (2,1)
T_ESP = (2,4)

T_M = (2,2)
T_A = (2,3)
TRANSPARENT = 5

class Jeu:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du Code", fps = 60)
        pyxel.load(filename = "images.pyxres")
        self.x = 0
        self.player_x = 60
        self.player_y = 80
        self.pas = 0
        self.start = False
        self.fond = 1920

        self.vie = 1
        self.scroll_y = 1080
        pyxel.blt(self.player_x, self.player_y, 0, 0, 0, 8, 8, TRANSPARENT)
        self.obstacles = []

        pyxel.run(self.update, self.draw)

    def update(self) :
        if pyxel.btnp(pyxel.KEY_Q) :
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_SPACE)  :
            self.start = not self.start


        if self.start :
            pyxel.bltm(0, 0, 0, 0, self.fond, 128, 128)
            self.fond -= 1

            if self.player_y <= 115 :
                self.player_y += 0.5
            if self.player_y == 115 :
                self.vie = 0

            self.vaisseau_deplacement()
            self.compteur_de_pas()
            self.obstacles_creation()
            #self.obstacles_sup()
            self.obstacles_dep()
            self.detect_coll()
            
    def draw(self) :
        pyxel.cls(0)

        if self.vie == 1:
            pyxel.camera
            pyxel.bltm(0, 0, 0, 0, self.fond, 128, 128)
           # self.fond -= 1
            pyxel.bltm(0, 0, 0, 0, self.scroll_y,  128, 128, TRANSPARENT)
            pyxel.blt(self.player_x, self.player_y, 0, 122, 12, 6, 8, TRANSPARENT)
            self.obstacles_creation()
            #self.obstacles_sup()
            pyxel.text(5,120, 'PAS:'+ str(pyxel.ceil(self.pas)), 7)
            
            # obstacles
            for o in self.obstacles:
                pyxel.blt(o[0], o[1], 0, 130, 64, 8, 8, TRANSPARENT)
        else:
            pyxel.camera(0, self.scroll_y)
            pyxel.text(50,64+self.scroll_y, 'GAME OVER', 7)



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
            o[1] += 2
            if  o[1]>128:
                self.obstacles.remove(o)
    """
        def obstacles_sup(self):
            for o in self.obstacles:
                if o[0] <= self.player_x+8 and o[1] <= self.player_y+8 >= self.player_x and o[1]+8 >= self.player_y:
                    self.obstacles.remove(o)
                    self.vie = 0
    """
    def scroll(self):
        if self.scroll_y>0:
            self.scroll_y -= 1
        else :
            self.scroll_y =1080
        self.appa_obs(self.scroll_y,self.scroll_y+1)

    def appa_obs(self,y1, y2):
         yt1 = pyxel.floor(y1 / 8)
         yt2 = pyxel.ceil(y2 / 8)
         
         for y in range(yt1, yt2 + 1):
             for x in range(16):
                 t = pyxel.tilemap(0).pget(x, y)
                 if t == T_M:
                     pyxel.tilemap(0).pset(x, y, T_ESP)
                     self.obstacles.append([x*8,y*8-y1])

    def detect_coll(self):
        for elt in self.obstacles : 
            dx = (elt[0] - self.player_x)**2
            dy = (elt[1] - self.player_y)**2

            if (dx < 64) and (dy < 64) :
                self.vie = 0
                break
      




Jeu()