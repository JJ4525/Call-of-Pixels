import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser
import os
import time
import random
def start_game(weapon1,weapon2,player_size, color1, color2, outline_color1, outline_color2, resize, movement_distance1, movement_distance2, health1, health2):
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
        def shoot(self, event = None):
            if "space" in game.pulsanti:
                if v_p1.minigun_cooldown >= 0 and v_p1.minigun_cooldown <= 30:
                    D_time = time.time() - v_p1.start_time
                    if D_time >= v_p1.reload_speed:
                        if v_p1.weapon != 3:
                            v_p1.bullet_plot()
                        else:
                            v_p1.bullet_plot()
                            mappa.after(100, v_p1.bullet_plot)
                            mappa.after(200, v_p1.bullet_plot)
                        v_p1.start_time = time.time()
                elif v_p1.minigun_cooldown > 30:
                    v_p1.minigun_cooldown = -20
                if v_p1.weapon == 2:
                    v_p1.minigun_cooldown +=1
            else:
                if v_p1.minigun_cooldown < 0:
                    v_p1.minigun_cooldown += 1 
                elif v_p1.minigun_cooldown > 0:
                    v_p1.minigun_cooldown -= 1
            if "Return" in game.pulsanti:
                if v_p2.minigun_cooldown >= 0 and v_p2.minigun_cooldown <= 30:
                    D_time = time.time() - v_p2.start_time
                    if D_time >= v_p2.reload_speed:
                        if v_p2.weapon != 3:
                            v_p2.bullet_plot()
                        else:
                            v_p2.bullet_plot()
                            mappa.after(100, v_p2.bullet_plot)
                            mappa.after(200, v_p2.bullet_plot)
                        v_p2.start_time = time.time()
                elif v_p2.minigun_cooldown > 30:
                    v_p2.minigun_cooldown = -20
                if v_p2.weapon == 2:
                    v_p2.minigun_cooldown +=1
            else:
                if v_p2.minigun_cooldown < 0:
                    v_p2.minigun_cooldown += 1 
                elif v_p2.minigun_cooldown > 0:
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
                    x1, y1, x2, y2 = mappa.coords(obj_id)
                    px1,py1,px2,py2 = mappa.coords(self.eid)
                    if x1 >= px1 and x2 <= px2 and y1 >= py1 and y2 <= py2:
                        mappa.delete(obj_id)
                        if self.pid == p1:
                            v_p2.damage_taken = float(tags[3])
                        elif self.pid == p2:
                            v_p1.damage_taken = float(tags[3])
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
                    [15, 10, 0.1, 0.5]))
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
    hp1.pack(side="left")
    hp2 = ttk.Progressbar(base, orient="horizontal", length= 200, mode="determinate")
    hp2.pack(side="right")
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
    build = tk.Label(main, text = "Build 5.1423", fg="#bebebe", background="#ffffff")
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