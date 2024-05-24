import tkinter as tk
from tkinter import ttk
import os
import time
class base_game:
    def __init__(self, pulsanti, resize, map_height, map_width, weapon_offset, path, weapon_coordinates, bullet_coordinates, weapon_stats):
        self.pulsanti = pulsanti
        self.resize = resize
        self.map_height = map_height
        self.map_width = map_width
        self.weapon_offset = weapon_offset
        self.path = path
        self.weapon_coordinates = weapon_coordinates
        self.bullet_coordinates = bullet_coordinates
        self.weapon_stats = weapon_stats
    def esci(self, Event = None):
        base.destroy()
    def premuto(self, event):
        if event.keysym not in self.pulsanti:
            self.pulsanti.append(event.keysym)
    def rilasciato(self,event):
        if event.keysym in self.pulsanti:
            self.pulsanti.remove(event.keysym)
    def sposta(self, Event = None):
        x1, y1, x2, y2 = mappa.coords(p1)
        x12, y12, x22, y22 = mappa.coords(p2)
        if "w" in self.pulsanti and y1 > player_size/2:
            mappa.move(p1, 0, - v_p1.movement_distance * self.resize)
            mappa.move("w1", 0, - v_p1.movement_distance * self.resize)
            x1, y1, x2, y2 = mappa.coords(p1)
            v_p1.gunpos = "n"
        if "d" in self.pulsanti and x2 < self.map_width-player_size/2:
            mappa.move(p1, v_p1.movement_distance * self.resize, 0)
            mappa.move("w1", v_p1.movement_distance * self.resize, 0)
            x1, y1, x2, y2 = mappa.coords(p1)
            v_p1.gunpos = "e"
        if "s" in self.pulsanti and y2 < self.map_height-player_size/2:
            mappa.move(p1, 0, v_p1.movement_distance * self.resize)
            mappa.move("w1", 0, v_p1.movement_distance * self.resize)
            x1, y1, x2, y2 = mappa.coords(p1)
            v_p1.gunpos = "s"
        if "a" in self.pulsanti and x1 > player_size/2:
            mappa.move(p1, - v_p1.movement_distance * self.resize, 0)
            mappa.move("w1", - v_p1.movement_distance * self.resize, 0)
            x1, y1, x2, y2 = mappa.coords(p1)
            v_p1.gunpos = "o"
        if "i" in self.pulsanti and y12 > player_size/2 or "Up" in self.pulsanti and y12 > player_size/2:
            mappa.move(p2, 0, - v_p2.movement_distance * self.resize)
            x1, y1, x2, y2 = mappa.coords(p2)
            v_p2.gunpos = "n"
        if "l" in self.pulsanti and x22 < self.map_width-player_size/2 or "Right" in self.pulsanti and x22 < self.map_width-player_size/2:
            mappa.move(p2, v_p2.movement_distance * self.resize, 0)
            x1, y1, x2, y2 = mappa.coords(p2)
            v_p2.gunpos = "e"
        if "k" in self.pulsanti and y22 < self.map_height-player_size/2 or "Down" in self.pulsanti and y22 < self.map_height-player_size/2:
            mappa.move(p2, 0, v_p2.movement_distance * self.resize)
            x1, y1, x2, y2 = mappa.coords(p2)
            v_p2.gunpos = "s"
        if "j" in self.pulsanti and x12 > player_size/2 or "Left" in self.pulsanti and x12 > player_size/2:
            mappa.move(p2, - v_p2.movement_distance * self.resize, 0)
            x1, y1, x2, y2 = mappa.coords(p2)
            v_p2.gunpos = "o"
        v_p1.weapon_update()
        v_p2.weapon_update()
        base.after(50, self.sposta)
    def bullet_movement(event = None):
        for obj_id in mappa.find_withtag("bullet"):
            x1, y1, x2, y2 = mappa.coords(obj_id)
            if x1 < 0-100 or y1 < 0-100 or x2 > game.map_width+100 or y2 > game.map_height+100:
                mappa.delete(obj_id)
        base.after(50, game.bullet_movement)
game = base_game([],
                 3,
                 1000,
                 1000,
                 3,
                 os.path.dirname(os.path.abspath(__file__)),
                 ([[[10.5, 5.5], [12, 8], '#595758'], [[10.5, 4.5], [16, 5.5], '#807A7A'], [[12, 5.5], [16, 6], '#595758']], [[[10, 3], [11, 7], '#7F807A'], [[11, 4], [21, 6], '#D39741'], [[14, 4], [16, 3], '#323232'], [[12, 3], [18, 2], '#817C78'], [[13, 6], [15, 9], '#494748'], [[21, 4.5], [26, 5.5], '#9D9D95']], [[[9.2, 3.7], [11, 4.5], '#231F20'], [[9.5, 4.5], [10, 5], '#494949'], [[9, 5], [12, 9], '#1F1F1F'], [[12, 7], [23, 6], '#5B5B5B'], [[12, 7], [23, 8], '#666666'], [[12, 9], [23, 8], '#5B5B5B'], [[20, 6], [21, 9], '#333333'], [[17, 6], [18, 9], '#333333'], [[14, 6], [15, 9], '#333333'], [[9.5, 
6.5], [11.5, 7], '#171717'], [[9.65, 7], [11.35, 12.35], '#63331f'], [[9.75, 7.25], [10.9, 7.75], '#FEEA3B'], [[10.9, 7.25], [11.25, 7.75], '#FEC006'], [[9.75, 8.0], [10.9, 8.5], '#FEEA3B'], [[10.9, 8.0], [11.25, 8.5], '#FEC006'], [[9.75, 8.75], [10.9, 9.25], '#FEEA3B'], [[10.9, 8.75], [11.25, 9.25], '#FEC006'], [[9.75, 9.5], [10.9, 10.0], '#FEEA3B'], [[10.9, 9.5], [11.25, 10.0], '#FEC006'], [[9.75, 10.25], [10.9, 10.75], '#FEEA3B'], [[10.9, 10.25], [11.25, 10.75], '#FEC006'], [[9.75, 11.0], [10.9, 11.5], '#FEEA3B'], [[10.9, 11.0], [11.25, 11.5], '#FEC006'], [[9.75, 11.75], [10.9, 12.25], '#FEEA3B'], [[10.9, 11.75], [11.25, 12.25], '#FEC006']], [[[10, 3], [20, 6], '#383838'], [[10, 6], [13, 7], '#383838'], [[11, 7], [12, 9], '#707070'], [[14, 6], [15, 8], '#292929'], [[13, 1], [14, 3], '#383838'], [[13, 1], [19, 2], '#383838'], [[19, 1], [18, 3], '#383838'], [[20, 4], [23, 5], '#2B2B2B']]),
                 ([[16, 4.8], [16.5, 5.2]], [[26, 4.7], [27.5, 5.3]], [[[23, 6.4], [23.3, 6.6]], [[23, 7.4], [23.3, 7.6]], [[23, 8.4], [23.3, 8.6]]], [[23, 4.25], [24, 4.75]]),
                 (
                #pistol stats
                  [10, 5, 100, 0.2],
                #sniper stats
                  [70, 15, 1000, 3],
                #minigun stats
                  [5, 5, 250, 0.05],
                #burst assault
                  [15, 10, 350, 0.5])
                 )
class player:
    def __init__(self, pid, tpid, wid, eid, health, movement_distance, damage_taken, gunpos, weapon, minigun, start_time, damage, bullet_speed, reload_speed):
        self.pid = pid
        self.tpid = tpid
        self.wid = wid
        self.eid = eid
        self.health = health
        self.movement_distance = movement_distance
        self.damage_taken = damage_taken
        self.gunpos = gunpos
        self.weapon = weapon
        self.minigun = minigun
        self.start_time = start_time    
        self.damage = damage
        self.bullet_speed = bullet_speed
        self.reload_speed = reload_speed
    def weapon_update(self):
        mappa.delete(self.wid)
        def coord_get(x):
            c = game.weapon_coordinates[self.weapon]
            if self.gunpos == "e":
                x1 = c[x][0][0] * game.resize - game.weapon_offset * game.resize
                y1 = c[x][0][1] * game.resize 
                x2 = c[x][1][0] * game.resize - game.weapon_offset * game.resize
                y2 = c[x][1][1] * game.resize
            elif self.gunpos == "n":
                y1 = c[x][0][0] * game.resize * -1 + player_size * game.resize + game.weapon_offset * game.resize
                x1 = c[x][0][1] * game.resize
                y2 = c[x][1][0] * game.resize * -1 + player_size * game.resize + game.weapon_offset * game.resize
                x2 = c[x][1][1] * game.resize
            elif self.gunpos == "s":
                y1 = c[x][0][0] * game.resize - game.weapon_offset * game.resize
                x1 = player_size * game.resize + c[x][0][1] * game.resize * -1
                y2 = c[x][1][0] * game.resize - game.weapon_offset * game.resize
                x2 = player_size * game.resize + c[x][1][1] * game.resize * -1
            elif self.gunpos == "o":
                x1 = player_size * game.resize + c[x][0][0] * game.resize * -1 + game.weapon_offset * game.resize
                y1 = c[x][0][1] * game.resize
                x2 = player_size * game.resize + c[x][1][0] * game.resize * -1 + game.weapon_offset * game.resize
                y2 = c[x][1][1] * game.resize
            col = c[x][2]
            return x1, x2, y1, y2, col
        bx1, by1, bx2, by2 = mappa.coords(self.pid)
        for num in range(len(game.weapon_coordinates[self.weapon])):
            x1, x2, y1, y2, col = coord_get(num)
            mappa.create_rectangle(bx1 + x1,by1 + y1,bx1 + x2,by1 + y2, fill=col,tags=self.wid)  
    def shoot(self, event = None):
        D_time = time.time() - self.start_time
        if D_time >= self.reload_speed:
            if self.weapon != 3:
                self.bullet_plot()
            else:
                self.bullet_plot()
                mappa.after(100, self.bullet_plot)
                mappa.after(200, self.bullet_plot)
            self.start_time = time.time()
    def bullet_plot(self):
        c = game.bullet_coordinates
        if self.weapon != 2:
            if self.gunpos == "e":
                x1 = c[self.weapon][0][0] * game.resize
                y1 = c[self.weapon][0][1] * game.resize 
                x2 = c[self.weapon][1][0] * game.resize
                y2 = c[self.weapon][1][1] * game.resize
            elif self.gunpos == "n":
                y1 = c[self.weapon][0][0] * game.resize * -1 + player_size * game.resize
                x1 = c[self.weapon][0][1] * game.resize
                y2 = c[self.weapon][1][0] * game.resize * -1 + player_size * game.resize
                x2 = c[self.weapon][1][1] * game.resize
            elif self.gunpos == "s":
                y1 = c[self.weapon][0][0] * game.resize
                x1 = player_size * game.resize + c[self.weapon][0][1] * game.resize * -1
                y2 = c[self.weapon][1][0] * game.resize
                x2 = player_size * game.resize + c[self.weapon][1][1] * game.resize * -1
            elif self.gunpos == "o":
                x1 = player_size * game.resize + c[self.weapon][0][0] * game.resize * -1
                y1 = c[self.weapon][0][1] * game.resize
                x2 = player_size * game.resize + c[self.weapon][1][0] * game.resize * -1
                y2 = c[self.weapon][1][1] * game.resize  
        else:
            if self.minigun >= 2:
                self.minigun = 0
            else:
                self.minigun += 1
            if self.gunpos == "e":
                x1 = c[self.weapon][self.minigun][0][0] * game.resize
                y1 = c[self.weapon][self.minigun][0][1] * game.resize 
                x2 = c[self.weapon][self.minigun][1][0] * game.resize
                y2 = c[self.weapon][self.minigun][1][1] * game.resize
            elif self.gunpos == "n":
                y1 = c[self.weapon][self.minigun][0][0] * game.resize * -1 + player_size * game.resize
                x1 = c[self.weapon][self.minigun][0][1] * game.resize
                y2 = c[self.weapon][self.minigun][1][0] * game.resize * -1 + player_size * game.resize
                x2 = c[self.weapon][self.minigun][1][1] * game.resize
            elif self.gunpos == "s":
                y1 = c[self.weapon][self.minigun][0][0] * game.resize
                x1 = player_size * game.resize + c[self.weapon][self.minigun][0][1] * game.resize * -1
                y2 = c[self.weapon][self.minigun][1][0] * game.resize
                x2 = player_size * game.resize + c[self.weapon][self.minigun][1][1] * game.resize * -1
            elif self.gunpos == "o":
                x1 = player_size * game.resize + c[self.weapon][self.minigun][0][0] * game.resize * -1
                y1 = c[self.weapon][self.minigun][0][1] * game.resize
                x2 = player_size * game.resize + c[self.weapon][self.minigun][1][0] * game.resize * -1
                y2 = c[self.weapon][self.minigun][1][1] * game.resize       
        bx1, by1, bx2, by2 = mappa.coords(self.pid)
        for x in range(len(game.bullet_coordinates[self.weapon])):
            mappa.create_rectangle(bx1 + x1,by1 + y1,bx1 + x2,by1 + y2, fill="#FBC540",tags=(self.gunpos,"bullet",self.tpid,bx1+x1,by1+y1)) 
    def stats_load(self):
        self.damage = game.weapon_stats[self.weapon][0]
        self.bullet_speed = game.weapon_stats[self.weapon][1]
        self.reload_speed = game.weapon_stats[self.weapon][3]
    def bullet_movement(self):
        for obj_id in mappa.find_withtag(self.tpid):
            if self.weapon != 1:
                x1, y1, x2, y2 = mappa.coords(obj_id)
                px1,py1,px2,py2 = mappa.coords(self.eid)
                if x1 >= px1 and x2 <= px2 and y1 >= py1 and y2 <= py2:
                    mappa.delete(obj_id)
                    if self.pid == p1:
                        v_p2.damage_taken = True
                    elif self.pid == p2:
                        v_p1.damage_taken = True
            else:
                x1, y1, x2, y2 = mappa.coords(obj_id)
                px1,py1,px2,py2 = mappa.coords(self.eid)
                ppx1, ppy1, ppx1, ppy1 = mappa.coords(self.pid)
                tags = mappa.gettags(obj_id)
                if (tags[0] == "n" and px1 <= x1 <= px2 and py1 >= y1 and py1 < ppy1) or \
                    (tags[0] == "e" and py1 <= y1 <= py2 and px1 <= x1 and px1 > ppx1) or \
                    (tags[0] == "s" and px1 <= x1 <= px2 and py1 <= y1 and py1 > ppy1) or \
                    (tags[0] == "o" and py1 <= y1 <= py2 and px1 >= x1 and px1 < ppx1):
                    mappa.delete(obj_id)
                    if self.pid == p1:
                        v_p2.damage_taken = True
                    elif self.pid == p2:
                        v_p1.damage_taken = True
        if self.damage_taken == True:
            if self.pid == p1:
                self.health -= v_p2.damage
                hp1["value"] = v_p1.health
            elif self.pid == p2:
                self.health -= v_p1.damage
                hp2["value"] = v_p2.health
            self.damage_taken = False
            if self.health <= 0:
                mappa.delete(self.pid)
                mappa.delete(self.wid)
        if mappa.find_withtag("bullet"):
            for obj_id in mappa.find_withtag(self.tpid):
                tags = mappa.gettags(obj_id)
                if tags[0] == "n":
                    mappa.move(obj_id, 0, - self.bullet_speed * game.resize)
                elif tags[0] == "e":
                    mappa.move(obj_id, self.bullet_speed * game.resize, 0)
                elif tags[0] == "s":
                    mappa.move(obj_id, 0, self.bullet_speed * game.resize)
                elif tags[0] == "o":
                    mappa.move(obj_id, - self.bullet_speed * game.resize, 0)  
        base.after(10, self.bullet_movement)
player_size = 10
base = tk.Tk()
base.geometry('1500x1000')
base.title("back to square one")
base.attributes("-fullscreen",True)
mappa = tk.Canvas(base, width=game.map_width, height=game.map_height, bg="white")
mappa.pack()
mappa.focus_set()
p1 = mappa.create_rectangle(3, 3, 3 + player_size * game.resize, 3 + player_size * game.resize, fill="#ed3419", outline="#c61a39", width=2)
p2 = mappa.create_rectangle(1001 - player_size * game.resize, 1001 - player_size * game.resize, 1001, 1001, fill="#023e8a", outline="#03045e", width=2)
v_p1 = player(p1,"p1","w1",p2, 100, 4, False, "e", 1, -1, time.time(),0,0,0)
v_p2 = player(p2,"p2","w2",p1, 100,4, False, "o", 3, -1, time.time(),0,0,0)
game.sposta()
game.bullet_movement()
v_p1.weapon_update()
v_p1.stats_load()
v_p1.bullet_movement()
v_p2.weapon_update()
v_p2.stats_load()
v_p2.bullet_movement()
hp1 = ttk.Progressbar(base, orient="horizontal", length=200, mode="determinate")
hp1.pack(side="left")
hp2 = ttk.Progressbar(base, orient="horizontal", length= 200, mode="determinate")
hp2.pack(side="right")
hp1["value"] = v_p1.health
hp2["value"] = v_p2.health
base.bind("<Escape>", game.esci)
base.bind("<KeyPress>", game.premuto)
base.bind("<KeyRelease>", game.rilasciato)
base.bind("<space>", v_p1.shoot)
base.bind("<Return>", v_p2.shoot)
base.mainloop()