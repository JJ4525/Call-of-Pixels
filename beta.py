import tkinter as tk
from tkinter import ttk
import pickle
import os
import subprocess
import time

def esci(event=None):
    base.destroy()

# -----controllo----- #
def tc(tag):
    oggetto = mappa.find_withtag(tag)
    if oggetto:
        tag_check = True
    else:
        tag_check = False
    return tag_check

# -----movimento----- #
def premuto(event):
    if event.keysym not in pulsanti:
        pulsanti.append(event.keysym)
def rilasciato(event):
    if event.keysym in pulsanti:
        pulsanti.remove(event.keysym)
def sposta():
    global gp1, gp2
    global weapon1, weapon2
    x1, y1, x2, y2 = mappa.coords(p1)
    x12, y12, x22, y22 = mappa.coords(p2)
    if "w" in pulsanti and y1 > player_size/2:
        mappa.move(p1, 0, - movement_distance * resize)
        mappa.move("w1", 0, - movement_distance * resize)
        x1, y1, x2, y2 = mappa.coords(p1)
        gp1 = "n"
    if "d" in pulsanti and x2 < map_width:
        mappa.move(p1, movement_distance * resize, 0)
        mappa.move("w1", movement_distance * resize, 0)
        x1, y1, x2, y2 = mappa.coords(p1)
        gp1 = "e"
    if "s" in pulsanti and y2 < map_height:
        mappa.move(p1, 0, movement_distance * resize)
        mappa.move("w1", 0, movement_distance * resize)
        x1, y1, x2, y2 = mappa.coords(p1)
        gp1 = "s"
    if "a" in pulsanti and x1 > player_size/2:
        mappa.move(p1, -movement_distance * resize, 0)
        mappa.move("w1", -movement_distance * resize, 0)
        x1, y1, x2, y2 = mappa.coords(p1)
        gp1 = "o"
    if "i" in pulsanti and y12 > player_size/2 or "Up" in pulsanti and y12 > player_size/2:
        mappa.move(p2, 0, -movement_distance * resize)
        x1, y1, x2, y2 = mappa.coords(p2)
        gp2 = "n"
    if "l" in pulsanti and x22 < map_width or "Right" in pulsanti and x22 < map_width:
        mappa.move(p2, movement_distance * resize, 0)
        x1, y1, x2, y2 = mappa.coords(p2)
        gp2 = "e"
    if "k" in pulsanti and y22 < map_height or "Down" in pulsanti and y22 < map_height:
        mappa.move(p2, 0, movement_distance * resize)
        x1, y1, x2, y2 = mappa.coords(p2)
        gp2 = "s"
    if "j" in pulsanti and x12 > player_size/2 or "Left" in pulsanti and x12 > player_size/2:
        mappa.move(p2, -movement_distance * resize, 0)
        x1, y1, x2, y2 = mappa.coords(p2)
        gp2 = "o"
    weapon_update(weapon1,p1,gp1,"p1")    
    weapon_update(weapon2,p2,gp2,"p2")
    base.after(50, sposta)
# -----stat loading----- #
def stats_load(weapon):
    with open(spath, "rb") as f:
            c = pickle.load(f)
    dmg = stats[weapon][0]
    speed = stats[weapon][1]
    range = stats[weapon][2]
    rs = stats[weapon][3]
    return dmg,speed,range,rs
# -----weapon plot----- #
def weapon_update(weapon,player,pose,wpl):
    if wpl == "p1":
        mappa.delete("w1")
    elif wpl == "p2":
        mappa.delete("w2")
    def cob(x,weapon,pose):
        with open(cpath, "rb") as f:
            c = pickle.load(f)[weapon]
            if pose == "e":
                x1 = c[x][0][0] * resize - weapon_offset * resize
                y1 = c[x][0][1] * resize 
                x2 = c[x][1][0] * resize - weapon_offset * resize
                y2 = c[x][1][1] * resize
            elif pose == "n":
                y1 = c[x][0][0] * resize * -1 + player_size * resize + weapon_offset * resize
                x1 = c[x][0][1] * resize
                y2 = c[x][1][0] * resize * -1 + player_size * resize + weapon_offset * resize
                x2 = c[x][1][1] * resize
            elif pose == "s":
                y1 = c[x][0][0] * resize - weapon_offset * resize
                x1 = player_size * resize + c[x][0][1] * resize * -1
                y2 = c[x][1][0] * resize - weapon_offset * resize
                x2 = player_size * resize + c[x][1][1] * resize * -1
            elif pose == "o":
                x1 = player_size * resize + c[x][0][0] * resize * -1 + weapon_offset * resize
                y1 = c[x][0][1] * resize
                x2 = player_size * resize + c[x][1][0] * resize * -1 + weapon_offset * resize
                y2 = c[x][1][1] * resize
            col = c[x][2]
            return x1, x2, y1, y2, col

    bx1, by1, bx2, by2 = mappa.coords(player)
    if wpl == "p1":
        for x in range(len(dcoord[weapon])):
            x1, x2, y1, y2, col = cob(x,weapon,pose)
            mappa.create_rectangle(bx1 + x1,by1 + y1,bx1 + x2,by1 + y2, fill=col,tags="w1")           
    elif wpl == "p2":
        for x in range(len(dcoord[weapon])):
            x1, x2, y1, y2, col = cob(x,weapon,pose)
            mappa.create_rectangle(bx1 + x1,by1 + y1,bx1 + x2,by1 + y2, fill=col,tags="w2")
# -----bullet plot----- #
def bullet_plot(x,player,pose,wpl):
    if x != 2:
        with open(bpath, "rb") as f:
            c = pickle.load(f)
        if pose == "e":
            x1 = c[x][0][0] * resize
            y1 = c[x][0][1] * resize 
            x2 = c[x][1][0] * resize
            y2 = c[x][1][1] * resize
        elif pose == "n":
            y1 = c[x][0][0] * resize * -1 + player_size * resize
            x1 = c[x][0][1] * resize
            y2 = c[x][1][0] * resize * -1 + player_size * resize
            x2 = c[x][1][1] * resize
        elif pose == "s":
            y1 = c[x][0][0] * resize
            x1 = player_size * resize + c[x][0][1] * resize * -1
            y2 = c[x][1][0] * resize
            x2 = player_size * resize + c[x][1][1] * resize * -1
        elif pose == "o":
            x1 = player_size * resize + c[x][0][0] * resize * -1
            y1 = c[x][0][1] * resize
            x2 = player_size * resize + c[x][1][0] * resize * -1
            y2 = c[x][1][1] * resize
    else:
        global minigun1, minigun2
        with open(bpath,"rb") as f:
            c = pickle.load(f)        
        if wpl == "p1":
            if minigun1 >= 2:
                minigun1 = 0
            else:
                minigun1 += 1
            if pose == "e":
                x1 = c[x][minigun1][0][0] * resize
                y1 = c[x][minigun1][0][1] * resize 
                x2 = c[x][minigun1][1][0] * resize
                y2 = c[x][minigun1][1][1] * resize
            elif pose == "n":
                y1 = c[x][minigun1][0][0] * resize * -1 + player_size * resize
                x1 = c[x][minigun1][0][1] * resize
                y2 = c[x][minigun1][1][0] * resize * -1 + player_size * resize
                x2 = c[x][minigun1][1][1] * resize
            elif pose == "s":
                y1 = c[x][minigun1][0][0] * resize
                x1 = player_size * resize + c[x][minigun1][0][1] * resize * -1
                y2 = c[x][minigun1][1][0] * resize
                x2 = player_size * resize + c[x][minigun1][1][1] * resize * -1
            elif pose == "o":
                x1 = player_size * resize + c[x][minigun1][0][0] * resize * -1
                y1 = c[x][minigun1][0][1] * resize
                x2 = player_size * resize + c[x][minigun1][1][0] * resize * -1
                y2 = c[x][minigun1][1][1] * resize
        elif wpl == "p2":
            
            if minigun2 >= 2:
                minigun2 = 0
            else:
                minigun2 += 1
            if pose == "e":
                x1 = c[x][minigun2][0][0] * resize
                y1 = c[x][minigun2][0][1] * resize 
                x2 = c[x][minigun2][1][0] * resize
                y2 = c[x][minigun2][1][1] * resize
            elif pose == "n":
                y1 = c[x][minigun2][0][0] * resize * -1 + player_size * resize  * resize
                x1 = c[x][minigun2][0][1] * resize
                y2 = c[x][minigun2][1][0] * resize * -1 + player_size * resize  * resize
                x2 = c[x][minigun2][1][1] * resize
            elif pose == "s":
                y1 = c[x][minigun2][0][0] * resize
                x1 = player_size * resize + c[x][minigun2][0][1] * resize * -1
                y2 = c[x][minigun2][1][0] * resize
                x2 = player_size * resize + c[x][minigun2][1][1] * resize * -1
            elif pose == "o":
                x1 = player_size * resize + c[x][minigun2][0][0] * resize * -1
                y1 = c[x][minigun2][0][1] * resize
                x2 = player_size * resize + c[x][minigun2][1][0] * resize * -1
                y2 = c[x][minigun2][1][1] * resize
    bx1, by1, bx2, by2 = mappa.coords(player)
    if wpl == "p1":
        for x in range(len(bcoord[x])):
            mappa.create_rectangle(bx1 + x1,by1 + y1,bx1 + x2,by1 + y2, fill="#FBC540",tags=(pose,"bullet","p1",bx1+x1,by1+y1))           
    elif wpl == "p2":
        for x in range(len(bcoord[x])):
            mappa.create_rectangle(bx1 + x1,by1 + y1,bx1 + x2,by1 + y2, fill="#FBC540",tags=(pose,"bullet","p2",bx1+x1,by1+y1))
    ftag_check = tc("bullet")
    bullet_movement(ftag_check)
# -----bullet movement----- #
def bullet_movement(tag_check):
    global health1, health2, damage_taken1, damage_taken2, hp1, hp2, dmg1, dmg2, speed1, speed2, weapon1, weapon2
    for obj_id in mappa.find_withtag("bullet"):
        x1, y1, x2, y2 = mappa.coords(obj_id)
        if x1 < 0-100 or y1 < 0-100 or x2 > map_width+100 or y2 > map_height+100:
            mappa.delete(obj_id)
    for obj_id in mappa.find_withtag("p1"):
        if weapon1 != 1:
            x1, y1, x2, y2 = mappa.coords(obj_id)
            px1,py1,px2,py2 = mappa.coords(p2)
            if x1 >= px1 and x2 <= px2 and y1 >= py1 and y2 <= py2:
                mappa.delete(obj_id)
                damage_taken2 = True
        else:
            x1, y1, x2, y2 = mappa.coords(obj_id)
            px1,py1,px2,py2 = mappa.coords(p2)
            ppx1, ppy1, ppx1, ppy1 = mappa.coords(p1)
            tags = mappa.gettags(obj_id)
            if (tags[0] == "n" and px1 <= x1 <= px2 and py1 >= y1 and py1 < ppy1) or \
                (tags[0] == "e" and py1 <= y1 <= py2 and px1 <= x1 and px1 > ppx1) or \
                (tags[0] == "s" and px1 <= x1 <= px2 and py1 <= y1 and py1 > ppy1) or \
                (tags[0] == "o" and py1 <= y1 <= py2 and px1 >= x1 and px1 < ppx1):
                mappa.delete(obj_id)
                damage_taken2 = True
    for obj_id in mappa.find_withtag("p2"):
        if weapon2 != 1:
            x1, y1, x2, y2 = mappa.coords(obj_id)
            px1,py1,px2,py2 = mappa.coords(p1)
            if x1 >= px1 and x2 <= px2 and y1 >= py1 and y2 <= py2:
                mappa.delete(obj_id)
                damage_taken1 = True
        else:
            x1, y1, x2, y2 = mappa.coords(obj_id)
            px1,py1,px2,py2 = mappa.coords(p1)
            ppx1, ppy1, ppx1, ppy1 = mappa.coords(p2)
            tags = mappa.gettags(obj_id)
            if (tags[0] == "n" and px1 <= x1 <= px2 and py1 >= y1 and py1 < ppy1) or \
                (tags[0] == "e" and py1 <= y1 <= py2 and px1 <= x1 and px1 > ppx1) or \
                (tags[0] == "s" and px1 <= x1 <= px2 and py1 <= y1 and py1 > ppy1) or \
                (tags[0] == "o" and py1 <= y1 <= py2 and px1 >= x1 and px1 < ppx1):
                mappa.delete(obj_id)
                damage_taken1 = True
                       
    if damage_taken1 == True:
        health1 -= dmg2
        damage_taken1 = False
        hp1["value"] = health1
        if health1 <= 0:
            mappa.delete(p1)
            mappa.delete("w1")
    if damage_taken2 == True:
        health2 -= dmg1
        damage_taken2 = False
        hp2["value"] = health2
        if health2 <= 0:
            mappa.delete(p2)
            mappa.delete("w2")
    for obj_id in mappa.find_withtag("p1"):
        tags = mappa.gettags(obj_id)
        if tags[0] == "n":
            mappa.move(obj_id, 0, - speed1 * resize)
        elif tags[0] == "e":
            mappa.move(obj_id, speed1 * resize, 0)
        elif tags[0] == "s":
            mappa.move(obj_id, 0, speed1 * resize)
        elif tags[0] == "o":
            mappa.move(obj_id, - speed1 * resize, 0)  
    for obj_id in mappa.find_withtag("p2"):
        tags = mappa.gettags(obj_id)
        if tags[0] == "n":
            mappa.move(obj_id, 0, - speed2 * resize)
        elif tags[0] == "e":
            mappa.move(obj_id, speed2 * resize, 0)
        elif tags[0] == "s":
            mappa.move(obj_id, 0, speed2 * resize)
        elif tags[0] == "o":
            mappa.move(obj_id, - speed2 * resize, 0)  
    tag_check = tc("bullet")
    if tag_check:
        base.after(10, bullet_movement, tag_check)
# -----shoot----- #
def p1_shoot(Event):
    global st1, rs1
    et1 = time.time()- st1
    if et1 >= rs1:
        if weapon1 != 3:
            bullet_plot(weapon1,p1,gp1,"p1")
            st1 = time.time()
        else:
            bullet_plot(weapon1,p1,gp1,"p1")
            mappa.after(100,bullet_plot,weapon1,p1,gp1,"p1")
            mappa.after(150,bullet_plot,weapon1,p1,gp1,"p1")
        st1 = time.time()
def p2_shoot(Event):
    global st2, rs2
    et2 = time.time()- st2
    if et2 >= rs2:
        if weapon2 != 3:
            bullet_plot(weapon2,p2,gp2,"p2")
            st2 = time.time()
        else:
            bullet_plot(weapon2,p2,gp2,"p2")
            mappa.after(100,bullet_plot,weapon2,p2,gp2,"p2")
            mappa.after(150,bullet_plot,weapon2,p2,gp2,"p2")
        st2 = time.time()
# -----general variables-----#
pulsanti = []
resize = 3
# -----player variables----- #
health1 = 100
health2 = 100
# *****graphic***** #
player_size = 10
p1_color = "#ed3419"
p1_outline = "#c61a39"
p2_color = "#023e8a"
p2_outline = "#03045e"
outline_width = 2
# *****coordinates***** #
p1_startx = 100
p1_starty = 500
p2_startx = 900
p2_starty = 500
movement_distance = 5
# -----weapon coords-----#
path = os.path.dirname(os.path.abspath(__file__))
# *****update pkl***** #
wscrpath = os.path.join(path, "game coordinates/weapon coordinates/packer.py")
bscrpath = os.path.join(path, "game coordinates/bullet coordinates/packer.py")
sscrpath = os.path.join(path, "game coordinates/weapon stats/packer.py")
subprocess.run(["python", wscrpath])
subprocess.run(["python", bscrpath])
subprocess.run(["python", sscrpath])
cpath = os.path.join(path, "game coordinates/weapon coordinates/coordinate.pkl")
bpath = os.path.join(path, "game coordinates/bullet coordinates/coordinate.pkl")
spath = os.path.join(path, "game coordinates/weapon stats/stats.pkl")
with open(spath, "rb") as f:
    stats = pickle.load(f)
with open(cpath, "rb") as f:
    dcoord = pickle.load(f)
with open(bpath, "rb") as f:
    bcoord = pickle.load(f)
# -----map variables----- #
map_height = 1000
map_width = 1000
# -----weapon variables----- #
gp1 = "e"
gp2 = "o"
weapon1 = 2
weapon2 = 1
weapon_offset = 3
minigun1 = -1
minigun2 = -1
damage_taken1 = False
damage_taken2 = False
st1 = time.time()
st2 = time.time()
# -----base----- #
base = tk.Tk()
base.geometry('1500x1000')
base.title("back to square one")
base.attributes("-fullscreen",True)
# -----mappa----- #
mappa = tk.Canvas(base, width=map_width, height=map_height, bg="white")
mappa.pack()
mappa.focus_set()
# -----p1 1----- #
p1 = mappa.create_rectangle(p1_startx - player_size / 2 * resize, p1_starty - player_size / 2 * resize, p1_startx + player_size / 2 * resize, p1_starty + player_size / 2 * resize, fill=p1_color, outline=p1_outline, width=outline_width)
weapon_update(weapon1,p1,gp1,"p1")
dmg1,speed1,range1,rs1 = stats_load(weapon1)
# -----p1 2----- #
p2 = mappa.create_rectangle(p2_startx - player_size / 2 * resize, p2_starty - player_size / 2 * resize, p2_startx + player_size / 2 * resize, p2_starty + player_size / 2 * resize, fill=p2_color, outline=p2_outline, width=outline_width)
weapon_update(weapon2,p2,gp2,"p2")
dmg2,speed2,range2,rs2 = stats_load(weapon2)
# -----barra vita----- #
hp1 = ttk.Progressbar(base, orient="horizontal", length=200, mode="determinate")
hp1.pack(side="left")
hp2 = ttk.Progressbar(base, orient="horizontal", length= 200, mode="determinate")
hp2.pack(side="right")
hp1["value"] = health1
hp2["value"] = health2
# -----control binds----- #
base.bind("<Escape>", esci)
base.bind("<KeyPress>", premuto)
base.bind("<KeyRelease>", rilasciato)
base.bind("<space>", p1_shoot)
base.bind("<Return>", p2_shoot)
sposta()
# -----mainloop----- #
base.mainloop()