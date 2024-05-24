import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
import os
import time
import random
import base64
import pygame
from io import BytesIO
def start_game(weapon1,weapon2,player_size, color1, color2, outline_color1, outline_color2, resize, movement_distance1, movement_distance2, health1, health2):
    class base_game:
        def __init__(self, pulsanti, resize, map_height, map_width, weapon_offset, path, weapon_coordinates, bullet_coordinates, weapon_stats, sniper_reload,sniper_shoot,burst_shoot, pistol_shoot,minigun_shoot):
            self.pulsanti = pulsanti
            self.resize = resize
            self.map_height = map_height
            self.map_width = map_width
            self.weapon_offset = weapon_offset
            self.path = path
            self.weapon_coordinates = weapon_coordinates
            self.bullet_coordinates = bullet_coordinates
            self.weapon_stats = weapon_stats
            self.sniper_reload = sniper_reload
            self.sniper_shoot = sniper_shoot
            self.burst_shoot = burst_shoot
            self.pistol_shoot = pistol_shoot
            self.minigun_shoot = minigun_shoot
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
            if "d" in self.pulsanti and x2 < self.map_width-player_size/2:
                mappa.move(p1, v_p1.movement_distance * self.resize, 0)
                mappa.move("w1", v_p1.movement_distance * self.resize, 0)
                x1, y1, x2, y2 = mappa.coords(p1)
            if "s" in self.pulsanti and y2 < self.map_height-player_size/2:
                mappa.move(p1, 0, v_p1.movement_distance * self.resize)
                mappa.move("w1", 0, v_p1.movement_distance * self.resize)
                x1, y1, x2, y2 = mappa.coords(p1)
            if "a" in self.pulsanti and x1 > player_size/2:
                mappa.move(p1, - v_p1.movement_distance * self.resize, 0)
                mappa.move("w1", - v_p1.movement_distance * self.resize, 0)
                x1, y1, x2, y2 = mappa.coords(p1)
            if "i" in self.pulsanti and y12 > player_size/2 or "Up" in self.pulsanti and y12 > player_size/2:
                mappa.move(p2, 0, - v_p2.movement_distance * self.resize)
                x1, y1, x2, y2 = mappa.coords(p2)
            if "l" in self.pulsanti and x22 < self.map_width-player_size/2 or "Right" in self.pulsanti and x22 < self.map_width-player_size/2:
                mappa.move(p2, v_p2.movement_distance * self.resize, 0)
                x1, y1, x2, y2 = mappa.coords(p2)
            if "k" in self.pulsanti and y22 < self.map_height-player_size/2 or "Down" in self.pulsanti and y22 < self.map_height-player_size/2:
                mappa.move(p2, 0, v_p2.movement_distance * self.resize)
                x1, y1, x2, y2 = mappa.coords(p2)
            if "j" in self.pulsanti and x12 > player_size/2 or "Left" in self.pulsanti and x12 > player_size/2:
                mappa.move(p2, - v_p2.movement_distance * self.resize, 0)
                x1, y1, x2, y2 = mappa.coords(p2)
            if self.pulsanti:
                if self.pulsanti[-1] == "w":
                    v_p1.gunpos = "n"
                elif self.pulsanti[-1] == "a":
                    v_p1.gunpos = "o"
                elif self.pulsanti[-1] == "s":
                    v_p1.gunpos = "s"
                elif self.pulsanti[-1] == "d":
                    v_p1.gunpos = "e"
                if self.pulsanti[-1] == "i" or self.pulsanti[-1] == "Up":
                    v_p2.gunpos = "n"
                elif self.pulsanti[-1] == "j" or self.pulsanti[-1] == "Left":
                    v_p2.gunpos = "o"
                elif self.pulsanti[-1] == "k" or self.pulsanti[-1] == "Down":
                    v_p2.gunpos = "s"
                elif self.pulsanti[-1] == "l" or self.pulsanti[-1] == "Right":
                    v_p2.gunpos = "e"
            v_p1.weapon_update()
            v_p2.weapon_update()
            base.after(50, self.sposta)
        def play_audio(self,audio):
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(BytesIO(base64.b64decode(audio)))
            pygame.mixer.music.play()
        def bullet_movement(event = None):
            for obj_id in mappa.find_withtag("bullet"):
                x1, y1, x2, y2 = mappa.coords(obj_id)
                if x1 < 0-100 or y1 < 0-100 or x2 > game.map_width+100 or y2 > game.map_height+100:
                    mappa.delete(obj_id)
            base.after(50, game.bullet_movement)
        def manual_console_control(event = None):
            cmd = input("")
            if cmd.startswith("weapon("):
                cmd = cmd[7:-1]
                list = cmd.split(',')
                x = int(list[0])
                y = int(list[1])
                if x == 1:
                    if y != v_p1.weapon and y < 4:
                        v_p1.weapon = y
                        v_p1.stats_load()
                    elif y == v_p2.weapon:
                        print("the weapon is already equipped")
                    else:
                        print("invalid weapon")
                if x == 2:
                    if y != v_p2.weapon and y < 4:
                        v_p2.weapon = y
                        v_p2.stats_load()
                    elif y == v_p2.weapon:
                        print("the weapon is already equipped")
                    else:
                        print("invalid weapon")
            base.after(50, game.manual_console_control)
        def collision_detection(self,collide,collided):
            x1, y1, x2, y2 = mappa.coords(collide)
            px1,py1,px2,py2 = mappa.coords(collided)
            if x1 >= px1 and x2 <= px2 and y1 >= py1 and y2 <= py2:
                return True
            else:
                return False
        def sniper_collision(self,collide,collided,shooter,direction):
            x1, y1, x2, y2 = mappa.coords(collide)
            px1,py1,px2,py2 = mappa.coords(collided)
            ppx1, ppy1, ppx1, ppy1 = mappa.coords(shooter)
            if (direction == "n" and px1 <= x1 <= px2 and y1+50 >= py1 >= y1 and py1 < ppy1) or \
                (direction == "e" and py1 <= y1 <= py2 and x1-50 <= px1 <= x1 and px1 > ppx1) or \
                (direction == "s" and px1 <= x1 <= px2 and y1-50 <= py1 <= y1 and py1 > ppy1) or \
                (direction == "o" and py1 <= y1 <= py2 and x1+50 >= px1 >= x1 and px1 < ppx1):
                return True
            else:
                return False
        def shoot(self, event = None):
            if "space" in game.pulsanti:
                if v_p1.weapon != 0 or v_p1.weapon == 2 and v_p1.minigun_cooldown >= 0 and v_p1.minigun_cooldown <= 30:
                    D_time = time.time() - v_p1.start_time
                    if D_time >= v_p1.reload_speed:
                        if v_p1.weapon != 3:
                            v_p1.bullet_plot()
                            if v_p1.weapon == 1:
                                game.play_audio(game.sniper_shoot)
                                base.after(int((v_p1.reload_speed-0.86)*1000),game.play_audio,game.sniper_reload)   
                            elif v_p1.weapon == 0:
                                game.play_audio(game.pistol_shoot)                             
                        else:
                            v_p1.bullet_plot()
                            game.play_audio(game.burst_shoot)
                            mappa.after(100, v_p1.bullet_plot)
                            mappa.after(100, game.play_audio,game.burst_shoot)
                            mappa.after(200, v_p1.bullet_plot)
                            mappa.after(200, game.play_audio,game.burst_shoot)
                        v_p1.start_time = time.time()
                elif v_p1.minigun_cooldown > 30:
                    v_p1.minigun_cooldown = -20
                if v_p1.weapon == 2:
                    v_p1.minigun_cooldown +=1
                    if v_p1.minigun_cooldown > 0:
                        game.play_audio(game.minigun_shoot)
            else:
                if v_p1.minigun_cooldown < -5:
                    v_p1.minigun_cooldown += 1 
                elif v_p1.minigun_cooldown > -5:
                    v_p1.minigun_cooldown -= 1
            if "Return" in game.pulsanti:
                if v_p2.minigun_cooldown >= -5 and v_p2.minigun_cooldown <= 30:
                    D_time = time.time() - v_p2.start_time
                    if D_time >= v_p2.reload_speed:
                        if v_p2.weapon != 3:
                            v_p2.bullet_plot()
                            if v_p2.weapon == 1:
                                game.play_audio(game.sniper_shoot)
                                base.after(int((v_p2.reload_speed-0.86)*1000),game.play_audio,game.sniper_reload)
                            elif v_p2.weapon == 0:
                                game.play_audio(game.pistol_shoot)        
                        else:
                            v_p2.bullet_plot()
                            game.play_audio(game.burst_shoot)
                            mappa.after(100, v_p2.bullet_plot)
                            mappa.after(100, game.play_audio,game.burst_shoot)
                            mappa.after(200, v_p2.bullet_plot)
                            mappa.after(200, game.play_audio,game.burst_shoot)
                        v_p2.start_time = time.time()
                elif v_p2.minigun_cooldown > 30:
                    v_p2.minigun_cooldown = -20
                if v_p2.weapon == 2:
                    v_p2.minigun_cooldown +=1
                    if v_p2.minigun_cooldown > 0:
                        game.play_audio(game.minigun_shoot)
            else:
                if v_p2.minigun_cooldown < -5:
                    v_p2.minigun_cooldown += 1 
                elif v_p2.minigun_cooldown > -5:
                    v_p2.minigun_cooldown -= 1
            base.after(50, game.shoot)
    class player:
        def __init__(self, pid, tpid, wid, eid, health, movement_distance, damage_taken, minigun_cooldown, gunpos, weapon, minigun, start_time, damage, bullet_speed, bullet_dropoff, reload_speed):
            self.pid = pid
            self.tpid = tpid
            self.wid = wid
            self.eid = eid
            self.health = health
            self.movement_distance = movement_distance
            self.damage_taken = damage_taken
            self.minigun_cooldown = minigun_cooldown
            self.gunpos = gunpos
            self.weapon = weapon
            self.minigun = minigun
            self.start_time = start_time    
            self.damage = damage
            self.bullet_speed = bullet_speed
            self.bullet_dropoff = bullet_dropoff
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
                mappa.create_rectangle(bx1 + x1,by1 + y1,bx1 + x2,by1 + y2, fill="#FBC540",tags=(self.gunpos,"bullet",self.tpid, self.damage)) 
        def stats_load(self):
            self.damage = game.weapon_stats[self.weapon][0]
            self.bullet_speed = game.weapon_stats[self.weapon][1]
            self.bullet_dropoff = game.weapon_stats[self.weapon][2]
            self.reload_speed = game.weapon_stats[self.weapon][3]
            self.minigun = -1
            self.minigun_cooldown = 0
        def bullet_movement(self):
            for obj_id in mappa.find_withtag(self.tpid):
                if self.weapon != 1:
                    tags = mappa.gettags(obj_id)
                    if game.collision_detection(obj_id,self.eid):
                        mappa.delete(obj_id)
                        if self.pid == p1:
                            v_p2.damage_taken = float(tags[3])
                        elif self.pid == p2:
                            v_p1.damage_taken = float(tags[3])
                else:
                    tags = mappa.gettags(obj_id)
                    if game.sniper_collision(obj_id,self.eid,self.pid,tags[0]):
                        mappa.delete(obj_id)
                        if self.pid == p1:
                            v_p2.damage_taken = float(tags[3])
                        elif self.pid == p2:
                            v_p1.damage_taken = float(tags[3])
            if self.damage_taken > 0:
                if self.pid == p1:
                    self.health -= v_p1.damage_taken
                    hp1["value"] = v_p1.health
                    v_p1.damage_taken = 0
                elif self.pid == p2:
                    self.health -= v_p2.damage_taken
                    hp2["value"] = v_p2.health
                    v_p2.damage_taken = 0
                if self.health <= 0:
                    mappa.delete(self.pid)
                    mappa.delete(self.wid)
            if mappa.find_withtag("bullet"):
                for obj_id in mappa.find_withtag(self.tpid):
                    tags = list(mappa.gettags(obj_id))
                    if tags[0] == "n":
                        mappa.move(obj_id, 0, - self.bullet_speed * game.resize)
                    elif tags[0] == "e":
                        mappa.move(obj_id, self.bullet_speed * game.resize, 0)
                    elif tags[0] == "s":
                        mappa.move(obj_id, 0, self.bullet_speed * game.resize)
                    elif tags[0] == "o":
                        mappa.move(obj_id, - self.bullet_speed * game.resize, 0)  
                    tags[3] = float(tags[3]) - float(self.bullet_dropoff)
                    if float(tags[3]) <= 0:
                        mappa.delete(obj_id)
                    else:
                        mappa.itemconfig(obj_id, tags=tuple(tags))
            base.after(10, self.bullet_movement)
    game = base_game([],
                    resize,
                    1000,
                    1000,
                    3,
                    os.path.dirname(os.path.abspath(__file__)),
                    ([[[10.5, 5.5], [12, 8], '#595758'], [[10.5, 4.5], [16, 5.5], '#807A7A'], [[12, 5.5], [16, 6], '#595758']], [[[10, 3], [11, 7], '#7F807A'], [[11, 4], [21, 6], '#D39741'], [[14, 4], [16, 3], '#323232'], [[12, 3], [18, 2], '#817C78'], [[13, 6], [15, 9], '#494748'], [[21, 4.5], [26, 5.5], '#9D9D95']], [[[9.2, 3.7], [11, 4.5], '#231F20'], [[9.5, 4.5], [10, 5], '#494949'], [[9, 5], [12, 9], '#1F1F1F'], [[12, 7], [23, 6], '#5B5B5B'], [[12, 7], [23, 8], '#666666'], [[12, 9], [23, 8], '#5B5B5B'], [[20, 6], [21, 9], '#333333'], [[17, 6], [18, 9], '#333333'], [[14, 6], [15, 9], '#333333'], [[9.5, 
    6.5], [11.5, 7], '#171717'], [[9.65, 7], [11.35, 12.35], '#63331f'], [[9.75, 7.25], [10.9, 7.75], '#FEEA3B'], [[10.9, 7.25], [11.25, 7.75], '#FEC006'], [[9.75, 8.0], [10.9, 8.5], '#FEEA3B'], [[10.9, 8.0], [11.25, 8.5], '#FEC006'], [[9.75, 8.75], [10.9, 9.25], '#FEEA3B'], [[10.9, 8.75], [11.25, 9.25], '#FEC006'], [[9.75, 9.5], [10.9, 10.0], '#FEEA3B'], [[10.9, 9.5], [11.25, 10.0], '#FEC006'], [[9.75, 10.25], [10.9, 10.75], '#FEEA3B'], [[10.9, 10.25], [11.25, 10.75], '#FEC006'], [[9.75, 11.0], [10.9, 11.5], '#FEEA3B'], [[10.9, 11.0], [11.25, 11.5], '#FEC006'], [[9.75, 11.75], [10.9, 12.25], '#FEEA3B'], [[10.9, 11.75], [11.25, 12.25], '#FEC006']], [[[10, 3], [20, 6], '#383838'], [[10, 6], [13, 7], '#383838'], [[11, 7], [12, 9], '#707070'], [[14, 6], [15, 8], '#292929'], [[13, 1], [14, 3], '#383838'], [[13, 1], [19, 2], '#383838'], [[19, 1], [18, 3], '#383838'], [[20, 4], [23, 5], '#2B2B2B']]),
                    ([[16, 4.8], [16.5, 5.2]], [[26, 4.7], [27.5, 5.3]], [[[23, 6.4], [23.3, 6.6]], [[23, 7.4], [23.3, 7.6]], [[23, 8.4], [23.3, 8.6]]], [[23, 4.25], [24, 4.75]]),
                    (
                    #pistol stats
                    [10, 5, 0.14, 0.2],
                    #sniper stats
                    [70, 15, 1.05, 3],
                    #minigun stats
                    [6, 5, 0.11, 0.05],
                    #burst assault
                    [15, 10, 0.1, 0.5]),
                    """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S0xBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/7gMTugA5JBVX08wALgrIovzOAEFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//sQxNYDwAAB/hwAACAAADSAAAAEVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVU=""",
                    """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""",
                    """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""",
                    """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""",
                    """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"""
                    )
    base = tk.Tk()
    base.geometry('1500x1000')
    base.title("call of pixels")
    base.attributes("-fullscreen",True)
    base.focus_force()
    mappa = tk.Canvas(base, width=game.map_width, height=game.map_height, bg="white")
    mappa.pack()
    mappa.focus_force()
    p1 = mappa.create_rectangle(3, 3, 3 + player_size * game.resize, 3 + player_size * game.resize, fill=color1, outline=outline_color1, width=2)
    p2 = mappa.create_rectangle(1001 - player_size * game.resize, 1001 - player_size * game.resize, 1001, 1001, fill=color2, outline=outline_color2, width=2)
    v_p1 = player(p1,"p1","w1",p2, health1, movement_distance1, 0,0, "e", weapon1, 0, time.time(),0,0,0,0)
    v_p2 = player(p2,"p2","w2",p1, health2,movement_distance2, 0,0, "o", weapon2, 0, time.time(),0,0,0,0)
    game.sposta()
    game.bullet_movement()
    game.shoot()
    v_p1.weapon_update()
    v_p1.stats_load()
    v_p1.bullet_movement()
    v_p2.weapon_update()
    v_p2.stats_load()
    v_p2.bullet_movement()
    hp1 = ttk.Progressbar(base, orient="horizontal", length=200, mode="determinate")
    hp1.place(x=50, y = 50)
    hp2 = ttk.Progressbar(base, orient="horizontal", length= 200, mode="determinate")
    hp2.place(x=base.winfo_screenwidth()-50, y = 50)
    hp1["value"] = v_p1.health
    hp2["value"] = v_p2.health
    base.bind("<Escape>", game.esci)
    base.bind("<KeyPress>", game.premuto)
    base.bind("<KeyRelease>", game.rilasciato)
    game.manual_console_control()
    base.mainloop()
def start_menu(color1,color2,outline_color1,outline_color2,resize,movement_distance1,movement_distance2,health1,health2):
    def close_window(event):
        main.destroy()
        select_menu(color1,color2,outline_color1,outline_color2,resize,movement_distance1,movement_distance2,health1,health2)
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    main = tk.Tk()
    main.title("call of pixels")
    main.geometry(f"{width}x{height}")
    main.attributes("-fullscreen",True)
    bgcanv = tk.Canvas(main,width=width, height= height, bg="#ffffff")
    bgcanv.pack()
    bgcanv.focus_set()
    player1 = bgcanv.create_rectangle(width*(1/16),height-width*(3/16), width*(1/16)+width*(3/16), height-(width*(3/16) + width*(3/16)), fill=color1, outline=outline_color1, width=20)    
    player2 = bgcanv.create_rectangle(width-width*(1/16),height-width*(3/16), width -(width*(1/16)+width*(3/16)), height-(width*(3/16) + width*(3/16)), fill=color2, outline=outline_color2, width=20)  
    bgcanv.create_rectangle(width*(6/16)-20,height-height*(3/16)+20,width-width*(6/16)+20,height-height*(5/16)-20, fill="#000000", tags="start")
    bgcanv.create_rectangle(width*(6/16),height-height*(3/16)-(height*(2/16))/3*2,width-width*(8/16),height-height*(3/16)-(height*(2/16))/3, fill=color1, width=0, tags="start")
    bgcanv.create_rectangle(width-width*(6/16),height-height*(3/16)-(height*(2/16))/3*2,width-width*(8/16),height-height*(3/16)-(height*(2/16))/3, fill=color2, width=0, tags="start")
    bgcanv.create_rectangle(width*(6/16),height-height*(3/16),width-width*(7.5/16),height-height*(3/16)-(height*(2/16))/3, fill=color1, width=0, tags="start")
    bgcanv.create_rectangle(width-width*(6/16),height-height*(3/16),width-width*(7.5/16),height-height*(3/16)-(height*(2/16))/3, fill=color2, width=0, tags="start")
    bgcanv.create_rectangle(width*(6/16),height-height*(3/16)-(height*(2/16))/3*2,width*(7.5/16),height-height*(3/16)-(height*(2/16)), fill=color1, width=0, tags="start")
    bgcanv.create_rectangle(width-width*(6/16),height-height*(3/16)-(height*(2/16))/3*2,width*(7.5/16),height-height*(3/16)-(height*(2/16)), fill=color2, width=0, tags="start")
    bgcanv.create_text((width*(6/16) + width-width*(6/16)) / 2, (height-height*(3/16) + height-height*(5/16)) / 2, text="START", fill="#000000", font=("Small Fonts", 70,"bold"), tags="start")
    for item in bgcanv.find_withtag("start"):
        bgcanv.tag_bind(item, '<ButtonPress-1>', close_window)
    titolo = tk.Label(main, text="CALL OF PIXELS", font=("Small Fonts", 100, "bold"), fg="#000000", background="#ffffff")
    titolo.place(x=width/2 - titolo.winfo_reqwidth()/2, y=100)
    build = tk.Label(main, text = "Build 8.13", fg="#bebebe", background="#ffffff")
    build.place(x=3,y=height -build.winfo_reqheight()-3)
    bx1, by1, bx2, by2 = bgcanv.coords(player1)
    bgcanv.create_rectangle(bx1 +300,by1 +130,bx1+320,by1+210, fill="#7F807A")
    bgcanv.create_rectangle(bx1 +320,by1 +150,bx1+520,by1+190, fill="#D39741")
    bgcanv.create_rectangle(bx1 +380,by1 +150,bx1+420,by1+130, fill="#323232")
    bgcanv.create_rectangle(bx1 +340,by1 +130,bx1+460,by1+110, fill="#817C78")
    bgcanv.create_rectangle(bx1 +360,by1 +190,bx1+400,by1+250, fill="#494748")
    bgcanv.create_rectangle(bx1 +520,by1 +160.0,bx1+620,by1+180.0, fill="#9D9D95")
    bx1, by1, bx2, by2 = bgcanv.coords(player2)
    bgcanv.create_rectangle(bx1 +60,by1 +130,bx1+-140,by1+190, fill="#383838")
    bgcanv.create_rectangle(bx1 +60,by1 +190,bx1+0,by1+210, fill="#383838")
    bgcanv.create_rectangle(bx1 +40,by1 +210,bx1+20,by1+250, fill="#707070")
    bgcanv.create_rectangle(bx1 +-20,by1 +190,bx1+-40,by1+230, fill="#292929")
    bgcanv.create_rectangle(bx1 +0,by1 +90,bx1+-20,by1+130, fill="#383838")
    bgcanv.create_rectangle(bx1 +0,by1 +90,bx1+-120,by1+110, fill="#383838")
    bgcanv.create_rectangle(bx1 +-120,by1 +90,bx1+-100,by1+130, fill="#383838")
    bgcanv.create_rectangle(bx1 +-140,by1 +150,bx1+-200,by1+170, fill="#2B2B2B")
    def bullet_plot1():
        bx1, by1, bx2, by2 = bgcanv.coords(player1)
        bgcanv.create_rectangle(bx1 + 620,by1 +170.0-0.3*20,bx1+620+1.5*20,by1+170.0+0.3*20, fill="#FBC540", tags="bullet1")  
        bullet_movement1()  
    def bullet_movement1():
        bgcanv.move("bullet1", 45, 0)
        for obj_id in bgcanv.find_withtag("bullet1"):
            x1, y1, x2, y2 = bgcanv.coords(obj_id)
            if x1 > width - (width/8):
                bgcanv.delete(obj_id)
        bgcanv.after(10,bullet_movement1)
    def bullet_plot2():
        bx1, by1, bx2, by2 = bgcanv.coords(player2)
        bgcanv.create_rectangle(bx1 +-200,by1 +160-0.2*20,bx1+-200-0.8*20,by1+160+0.2*20, fill="#FBC540",tags="bullet2")
    def bullet_movement2():
        bgcanv.move("bullet2", -25, 0)
        for obj_id in bgcanv.find_withtag("bullet2"):
            x1, y1, x2, y2 = bgcanv.coords(obj_id)
            if x1 < width*(1/16)+width*(3/16):
                bgcanv.delete(obj_id)
        bgcanv.after(10,bullet_movement2)
    def p1_shoot():        
        bgcanv.after(1000,bullet_plot1)
        bgcanv.after(int(random.uniform(3.5,5)*1000), p1_shoot)  
    def p2_shoot():
        bullet_movement2()
        bullet_plot2()
        bgcanv.after(100,bullet_plot2)
        bgcanv.after(200,bullet_plot2)
        bgcanv.after(int(random.uniform(1,3)*1000), p2_shoot) 
    p1_shoot()
    p2_shoot() 
    main.mainloop()
def select_menu(color1,color2,outline_color1,outline_color2,resize,movement_distance1,movement_distance2,health1,health2):
    class Game:
        def __init__(self):
            self.color1 = color1
            self.color2 = color2
            self.outline_color1 = outline_color1
            self.outline_color2 = outline_color2
            self.resize = resize
            self.movement_distance1 = movement_distance1
            self.movement_distance2 = movement_distance2
            self.health1 = health1
            self.health2 = health2  
        def update_variable(self, variable, value):
            if variable.startswith("color") or variable.startswith("outline_color"):
                self.__dict__[variable] = value
            elif variable.startswith("movement_distance") or variable.startswith("health"):
                try:
                    value = int(value)
                    if value >= 0:
                        self.__dict__[variable] = value
                    else:
                        raise ValueError("Value must be positive")
                except ValueError:
                    print("Invalid value. Please enter a positive integer.")
            else:
                print("Invalid variable name.")     
    class SelectWindow:
        def __init__(self, master,id, weapon):
            self.master = master
            self.current_selection = 0
            self.options = ["P", "S", "M", "B"]
            self.font_size_selected = 24
            self.font_size_unselected = 14
            self.id = id
            self.weapon = weapon
            self.label_p = tk.Label(master, text="P", font=("Small Fonts", self.font_size_unselected),bg="#ffffff")
            self.label_p.grid(row=0, column=1, padx=10)
            self.label_s = tk.Label(master, text="S", font=("Small Fonts", self.font_size_unselected),bg="#ffffff")
            self.label_s.grid(row=0, column=2, padx=10)
            self.label_m = tk.Label(master, text="M", font=("Small Fonts", self.font_size_unselected),bg="#ffffff")
            self.label_m.grid(row=0, column=3, padx=10)
            self.left_arrow_button = tk.Button(master, text="<",font=("Small Fonts", 20), command=self.move_left,bg="#ffffff")
            self.left_arrow_button.grid(row=0, column=0, pady=10)
            self.right_arrow_button = tk.Button(master, text=">",font=("Small Fonts", 20), command=self.move_right,bg="#ffffff")
            self.right_arrow_button.grid(row=0, column=4, pady=10)
            self.update_labels()
        def move_left(self):
            self.current_selection = (self.current_selection - 1) % len(self.options)
            self.update_labels()
        def move_right(self):
            self.current_selection = (self.current_selection + 1) % len(self.options)
            self.update_labels()
        def weapon_update(self):
            weapon_coordinates =([[[10.5, 5.5], [12, 8], '#595758'], [[10.5, 4.5], [16, 5.5], '#807A7A'], [[12, 5.5], [16, 6], '#595758']], [[[10, 3], [11, 7], '#7F807A'], [[11, 4], [21, 6], '#D39741'], [[14, 4], [16, 3], '#323232'], [[12, 3], [18, 2], '#817C78'], [[13, 6], [15, 9], '#494748'], [[21, 4.5], [26, 5.5], '#9D9D95']], [[[9.2, 3.7], [11, 4.5], '#231F20'], [[9.5, 4.5], [10, 5], '#494949'], [[9, 5], [12, 9], '#1F1F1F'], [[12, 7], [23, 6], '#5B5B5B'], 
[[12, 7], [23, 8], '#666666'], [[12, 9], [23, 8], '#5B5B5B'], [[20, 6], [21, 9], '#333333'], [[17, 6], [18, 9], '#333333'], [[14, 6], [15, 9], '#333333'], [[9.5, 6.5], [11.5, 7], '#171717'], [[9.65, 7], [11.35, 12.35], '#63331f'], [[9.75, 7.25], [10.9, 7.75], '#FEEA3B'], [[10.9, 7.25], [11.25, 7.75], '#FEC006'], [[9.75, 8.0], [10.9, 8.5], '#FEEA3B'], [[10.9, 8.0], [11.25, 8.5], '#FEC006'], [[9.75, 8.75], [10.9, 9.25], '#FEEA3B'], [[10.9, 8.75], [11.25, 9.25], '#FEC006'], [[9.75, 9.5], [10.9, 10.0], '#FEEA3B'], [[10.9, 9.5], [11.25, 10.0], '#FEC006'], [[9.75, 10.25], [10.9, 10.75], '#FEEA3B'], [[10.9, 10.25], [11.25, 10.75], '#FEC006'], [[9.75, 11.0], [10.9, 11.5], '#FEEA3B'], [[10.9, 11.0], [11.25, 11.5], '#FEC006'], [[9.75, 11.75], [10.9, 12.25], '#FEEA3B'], [[10.9, 11.75], [11.25, 12.25], '#FEC006']], [[[10, 3], [20, 6], '#383838'], [[10, 6], [13, 7], '#383838'], [[11, 7], [12, 9], '#707070'], [[14, 6], [15, 8], '#292929'], [[13, 1], [14, 3], '#383838'], [[13, 1], [19, 2], '#383838'], [[19, 1], [18, 3], '#383838'], [[20, 4], [23, 5], '#2B2B2B']])
            if self.id == "menu1":
                if self.current_selection == 0:
                    weapon1 = 1
                    self.weapon = 1
                elif self.current_selection == 1:
                    weapon1 = 2
                    self.weapon = 2
                elif self.current_selection == 2:
                    weapon1 = 3 
                    self.weapon = 3      
                elif self.current_selection == 3:
                    weapon1 = 0
                    self.weapon = 0
                bgcanv.delete("weapon1")
                def coord_get(x):
                        c = weapon_coordinates[weapon1]
                        x1 = c[x][0][0] * 20 - 3 * 20 + 160
                        y1 = c[x][0][1] * 20 + 75
                        x2 = c[x][1][0] * 20 - 3 * 20+ 160
                        y2 = c[x][1][1] * 20+ 75
                        col = c[x][2]
                        return x1, x2, y1, y2, col
                bx1, by1, bx2, by2 = bgcanv.coords(player1)
                for num in range(len(weapon_coordinates[weapon1])):
                    x1, x2, y1, y2, col = coord_get(num)
                    bgcanv.create_rectangle(bx1 + x1,by1 + y1,bx1 + x2,by1 + y2, fill=col,tags="weapon1")   
            elif self.id == "menu2":
                if self.current_selection == 0:
                    weapon2 = 1
                    self.weapon = 1
                elif self.current_selection == 1:
                    weapon2 = 2
                    self.weapon = 2
                elif self.current_selection == 2:
                    weapon2 = 3     
                    self.weapon = 3 
                elif self.current_selection == 3:
                    weapon2 = 0
                    self.weapon = 0
                bgcanv.delete("weapon2")
                def coord_get(x):
                        c = weapon_coordinates[weapon2]
                        x1 = player_size * 20 + c[x][0][0] * 20 * -1 + 3 * 20
                        y1 = c[x][0][1] * 20 +75
                        x2 = player_size * 20 + c[x][1][0] * 20 * -1 + 3 * 20
                        y2 = c[x][1][1] * 20 +75
                        col = c[x][2]
                        return x1, x2, y1, y2, col
                bx1, by1, bx2, by2 = bgcanv.coords(player2)
                for num in range(len(weapon_coordinates[weapon2])):
                    x1, x2, y1, y2, col = coord_get(num)
                    bgcanv.create_rectangle(bx1 + x1,by1 + y1,bx1 + x2,by1 + y2, fill=col,tags="weapon2")        
        
        def update_labels(self):
            for i in range(3):
                index = (self.current_selection + i) % len(self.options)
                font_size = self.font_size_selected if i == 1 else self.font_size_unselected
                if i == 0:
                    self.label_p.config(text=self.options[index], font=("Small Fonts", font_size,"bold"))
                elif i == 1:
                    self.label_s.config(text=self.options[index], font=("Small Fonts", font_size,"bold"))
                elif i == 2:
                    self.label_m.config(text=self.options[index], font=("Small Fonts", font_size,"bold"))
            self.weapon_update()
        def get_stats(self,weapon,type):
            if type == "weapon":
                if weapon== 0:
                    return "Pistol"
                if weapon == 1:
                    return "Sniper"
                elif weapon == 2:
                    return "Minigun"
                elif weapon == 3:
                    return "Burst Assault Rifle"
            if type == "damage":
                if weapon== 0:
                    return 10
                if weapon == 1:
                    return 70
                elif weapon == 2:
                    return 6
                elif weapon == 3:
                    return 15
            elif type == "speed":
                if weapon== 0:
                    return "low"
                if weapon == 1:
                    return "high"
                elif weapon == 2:
                    return "low"
                elif weapon == 3:
                    return "medium"
            elif type == "dropoff":
                if weapon== 0:
                    return "medium"
                if weapon == 1:
                    return "high"
                elif weapon == 2:
                    return "medium"
                elif weapon == 3:
                    return "high"
            elif type == "reload":
                if weapon== 0:
                    return 0.2
                if weapon == 1:
                    return 3
                elif weapon == 2:
                    return 0.05
                elif weapon == 3:
                    return 0.5  
    def goback():
        main.destroy
        start_menu(game.color1,game.color2,game.outline_color1,game.outline_color2,game.resize,game.movement_distance1,game.movement_distance2,game.health1,game.health2)
    def close_window(event):
        main.destroy()
        start_game(menu1.weapon,menu2.weapon,player_size, game.color1, game.color2, game.outline_color1, game.outline_color2, game.resize, game.movement_distance1, game.movement_distance2, game.health1, game.health2)
    def open_settings():
        def choose_color(variable):
            color = colorchooser.askcolor()[1]
            if color:
                setattr(game, variable, color)

        def update_variable(variable, entry):
            value = entry.get()
            if variable.startswith("color") or variable.startswith("outline_color"):
                choose_color(variable)
            elif variable.startswith("movement_distance") or variable.startswith("health"):
                try:
                    value = int(value)
                    if value >= 0:
                        setattr(game, variable, value)
                    else:
                        raise ValueError("Value must be positive")
                except ValueError:
                    print("Invalid value. Please enter a positive integer.")
            else:
                print("Invalid variable name.")
        root = tk.Tk()
        root.title("Menu Variabili")
        options_frame = tk.Frame(root)
        options_frame.pack(padx=10, pady=10)
        color1_label = tk.Label(options_frame, text="color player 1:",font=("Small Fonts",17))
        color1_label.grid(row=0, column=0, padx=5, pady=5)
        color1_entry = tk.Entry(options_frame)
        color1_entry.insert(tk.END, game.color1)
        color1_entry.grid(row=0, column=1, padx=5, pady=5)
        color1_button = tk.Button(options_frame, text="change",font=("Small Fonts",17), command=lambda: update_variable("color1", color1_entry))
        color1_button.grid(row=0, column=2, padx=5, pady=5)
        color2_label = tk.Label(options_frame, text="color player 2:",font=("Small Fonts",17))
        color2_label.grid(row=1, column=0, padx=5, pady=5)
        color2_entry = tk.Entry(options_frame)
        color2_entry.insert(tk.END, game.color2)
        color2_entry.grid(row=1, column=1, padx=5, pady=5)
        color2_button = tk.Button(options_frame, text="change",font=("Small Fonts",17), command=lambda: update_variable("color2", color2_entry))
        color2_button.grid(row=1, column=2, padx=5, pady=5)
        outline_color1_label = tk.Label(options_frame, text="outline color player 1:",font=("Small Fonts",17))
        outline_color1_label.grid(row=2, column=0, padx=5, pady=5)
        outline_color1_entry = tk.Entry(options_frame)
        outline_color1_entry.insert(tk.END, game.outline_color1)
        outline_color1_entry.grid(row=2, column=1, padx=5, pady=5)
        outline_color1_button = tk.Button(options_frame, text="change",font=("Small Fonts",17), command=lambda: update_variable("outline_color1", outline_color1_entry))
        outline_color1_button.grid(row=2, column=2, padx=5, pady=5)
        outline_color2_label = tk.Label(options_frame, text="outline color player 2:",font=("Small Fonts",17))
        outline_color2_label.grid(row=3, column=0, padx=5, pady=5)
        outline_color2_entry = tk.Entry(options_frame)
        outline_color2_entry.insert(tk.END, game.outline_color2)
        outline_color2_entry.grid(row=3, column=1, padx=5, pady=5)
        outline_color2_button = tk.Button(options_frame, text="change",font=("Small Fonts",17), command=lambda: update_variable("outline_color2", outline_color2_entry))
        outline_color2_button.grid(row=3, column=2, padx=5, pady=5)
        movement_distance1_label = tk.Label(options_frame, text="movement distance player 1:",font=("Small Fonts",17))
        movement_distance1_label.grid(row=4, column=0, padx=5, pady=5)
        movement_distance1_entry = tk.Entry(options_frame)
        movement_distance1_entry.insert(tk.END, game.movement_distance1)
        movement_distance1_entry.grid(row=4, column=1, padx=5, pady=5)
        movement_distance1_button = tk.Button(options_frame, text="change",font=("Small Fonts",17), command=lambda: update_variable("movement_distance1", movement_distance1_entry))
        movement_distance1_button.grid(row=4, column=2, padx=5, pady=5)
        movement_distance2_label = tk.Label(options_frame, text="movement distance player 2:",font=("Small Fonts",17))
        movement_distance2_label.grid(row=5, column=0, padx=5, pady=5)
        movement_distance2_entry = tk.Entry(options_frame)
        movement_distance2_entry.insert(tk.END, game.movement_distance2)
        movement_distance2_entry.grid(row=5, column=1, padx=5, pady=5)
        movement_distance2_button = tk.Button(options_frame, text="change",font=("Small Fonts",17), command=lambda: update_variable("movement_distance2", movement_distance2_entry))
        movement_distance2_button.grid(row=5, column=2, padx=5, pady=5)
        health1_label = tk.Label(options_frame, text="health player 1:",font=("Small Fonts",17))
        health1_label.grid(row=6, column=0, padx=5, pady=5)
        health1_entry = tk.Entry(options_frame)
        health1_entry.insert(tk.END, game.health1)
        health1_entry.grid(row=6, column=1, padx=5, pady=5)
        health1_button = tk.Button(options_frame, text="change",font=("Small Fonts",17), command=lambda: update_variable("health1", health1_entry))
        health1_button.grid(row=6, column=2, padx=5, pady=5)
        health2_label = tk.Label(options_frame, text="health player 2:",font=("Small Fonts",17))
        health2_label.grid(row=7, column=0, padx=5, pady=5)
        health2_entry = tk.Entry(options_frame)
        health2_entry.insert(tk.END, game.health2)
        health2_entry.grid(row=7, column=1, padx=5, pady=5)
        health2_button = tk.Button(options_frame, text="change",font=("Small Fonts",17), command=lambda: update_variable("health2", health2_entry))
        health2_button.grid(row=7, column=2, padx=5, pady=5)
        root.mainloop()
    game = Game()
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    main = tk.Tk()
    main.title("call of pixels")
    main.geometry(f"{width}x{height}")
    main.attributes("-fullscreen",True)
    bgcanv = tk.Canvas(main,width=width, height= height, bg="#ffffff")
    bgcanv.pack()
    bgcanv.focus_set()
    player1 = bgcanv.create_rectangle(width*(1/16),height-width*(1/16), width*(1/16)+width*(3/16), height-(width*(1/16) + width*(3/16)), fill=color1, outline=outline_color1, width=20)    
    player2 = bgcanv.create_rectangle(width-width*(1/16),height-width*(1/16), width -(width*(1/16)+width*(3/16)), height-(width*(1/16) + width*(3/16)), fill=color2, outline=outline_color2, width=20)  
    bgcanv.create_rectangle(width*(6/16)-20,height-height*(3/16)+20+height*(2/16),width-width*(6/16)+20,height-height*(5/16)-20+height*(2/16), fill="#000000", tags="start")
    bgcanv.create_rectangle(width*(6/16),height-height*(3/16)-(height*(2/16))/3*2+height*(2/16),width-width*(8/16),height-height*(3/16)-(height*(2/16))/3+height*(2/16), fill=color1, width=0, tags="start")
    bgcanv.create_rectangle(width-width*(6/16),height-height*(3/16)-(height*(2/16))/3*2+height*(2/16),width-width*(8/16),height-height*(3/16)-(height*(2/16))/3+height*(2/16), fill=color2, width=0, tags="start")
    bgcanv.create_rectangle(width*(6/16),height-height*(3/16)+height*(2/16),width-width*(7.5/16),height-height*(3/16)-(height*(2/16))/3+height*(2/16), fill=color1, width=0, tags="start")
    bgcanv.create_rectangle(width-width*(6/16),height-height*(3/16)+height*(2/16),width-width*(7.5/16),height-height*(3/16)-(height*(2/16))/3+height*(2/16), fill=color2, width=0, tags="start")
    bgcanv.create_rectangle(width*(6/16),height-height*(3/16)-(height*(2/16))/3*2+height*(2/16),width*(7.5/16),height-height*(3/16)-(height*(2/16))+height*(2/16), fill=color1, width=0, tags="start")
    bgcanv.create_rectangle(width-width*(6/16),height-height*(3/16)-(height*(2/16))/3*2+height*(2/16),width*(7.5/16),height-height*(3/16)-(height*(2/16))+height*(2/16), fill=color2, width=0, tags="start")
    bgcanv.create_text((width*(6/16) + width-width*(6/16)) / 2, (height-height*(3/16) + height-height*(5/16)) / 2 +height*(2/16), text="START", fill="#000000", font=("Small Fonts", 70,"bold"), tags="start")
    menu1_frame = tk.Frame(main,bg="#ffffff")
    menu1_frame.place(x=width*(1/16)+ (width*(3/16)-menu1_frame.winfo_width())/2, y=height-(width*(1/16) + width*(3/16))-1/16*height, anchor="center")
    menu1 = SelectWindow(menu1_frame, id="menu1", weapon=1)
    menu2_frame = tk.Frame(main,bg="#ffffff")
    menu2_frame.place(x=width-(width*(1/16)+ (width*(3/16)-menu1_frame.winfo_width())/2), y=height-(width*(1/16) + width*(3/16))-1/16*height, anchor="center")
    menu2 = SelectWindow(menu2_frame, id="menu2", weapon=1)
    for item in bgcanv.find_withtag("start"):
        bgcanv.tag_bind(item, '<ButtonPress-1>', close_window)          
    name1 = tk.Label(bgcanv, text=f"{menu1.get_stats(1,"weapon")}", font=("Small Fonts", 27,"bold"),bg="#ffffff", fg=color1)
    name1.place(x=width*4/16,y=height*2.3/16)
    damage1 = tk.Label(bgcanv, text=f"damage: {menu1.get_stats(1,"damage")}", font=("Small Fonts",20),bg="#ffffff", fg=color1)
    damage1.place(x=width*4/16,y=height*3.3/16)
    bullet_speed1 = tk.Label(bgcanv, text=f"bullet speed: {menu1.get_stats(1,"speed")}", font=("Small Fonts",20),bg="#ffffff", fg=color1)
    bullet_speed1.place(x=width*4/16,y=height*4/16)
    reload_speed1 = tk.Label(bgcanv, text=f"reload speed: {menu1.get_stats(1,"reload")}", font=("Small Fonts",20),bg="#ffffff", fg=color1)
    reload_speed1.place(x=width*4/16,y=height*4.7/16)
    bullet_dropoff1 = tk.Label(bgcanv, text=f"range: {menu1.get_stats(1,"dropoff")}", font=("Small Fonts",20),bg="#ffffff", fg=color1)
    bullet_dropoff1.place(x=width*4/16,y=height*5.5/16)
    name2 = tk.Label(bgcanv, text=f"{menu1.get_stats(1,"weapon")}", font=("Small Fonts", 27,"bold"),bg="#ffffff", fg=color1)
    name2.place(x=width-width*6.2/16,y=height*2.3/16)
    damage2 = tk.Label(bgcanv, text=f"damage: {menu1.get_stats(1,"damage")}", font=("Small Fonts",20),bg="#ffffff", fg=color1)
    damage2.place(x=width-width*6.2/16,y=height*3.3/16)
    bullet_speed2 = tk.Label(bgcanv, text=f"bullet speed: {menu1.get_stats(1,"speed")}", font=("Small Fonts",20),bg="#ffffff", fg=color1)
    bullet_speed2.place(x=width-width*6.2/16,y=height*4/16)
    reload_speed2 = tk.Label(bgcanv, text=f"reload speed: {menu1.get_stats(1,"reload")}", font=("Small Fonts",20),bg="#ffffff", fg=color1)
    reload_speed2.place(x=width-width*6.2/16,y=height*4.7/16)
    bullet_dropoff2 = tk.Label(bgcanv, text=f"range: {menu1.get_stats(1,"dropoff")}", font=("Small Fonts",20),bg="#ffffff", fg=color1)
    bullet_dropoff2.place(x=width-width*6.2/16,y=height*5.5/16)
    impostazioni = tk.Button(bgcanv,text = "⚙️", font = ("Small Fonts",20),command=open_settings)
    impostazioni.place(x=width-100,y=50)
    back = tk.Button(bgcanv,text = "<-", font = ("Small Fonts",20),command=goback)
    back.place(x=50,y=50)
    def update_stats():
        name1.config(text= menu1.get_stats(menu1.weapon,"weapon"))
        damage1.config(text= f"damage: {menu1.get_stats(menu1.weapon,"damage")}")
        bullet_speed1.config(text= f"bullet speed: {menu1.get_stats(menu1.weapon,"speed")}")
        reload_speed1.config(text = f"reload speed: {menu1.get_stats(menu1.weapon,"reload")}")
        bullet_dropoff1.config(text= f"range: {menu1.get_stats(menu1.weapon,"dropoff")}")
        name2.config(text= menu2.get_stats(menu2.weapon,"weapon"))
        damage2.config(text= f"damage: {menu2.get_stats(menu2.weapon,"damage")}")
        bullet_speed2.config(text= f"bullet speed: {menu2.get_stats(menu2.weapon,"speed")}")
        reload_speed2.config(text = f"reload speed: {menu2.get_stats(menu2.weapon,"reload")}")
        bullet_dropoff2.config(text= f"range: {menu2.get_stats(menu2.weapon,"dropoff")}")
        main.after(100,update_stats)
    update_stats()
    main.mainloop()
weapon1 = 1
weapon2 = 1
player_size = 10
color1 = "#ed3419"
color2 = "#023e8a"
outline_color1 = "#c61a39"
outline_color2 = "#03045e"
resize = 3
movement_distance1 = 4
movement_distance2 = 4
health1 = 100
health2 = 100
start_menu(color1,color2,outline_color1,outline_color2,resize,movement_distance1,movement_distance2,health1,health2)