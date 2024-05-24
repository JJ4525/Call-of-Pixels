import tkinter as tk
def healthcheck():
    global health
    global health2
    if god2 == 0: 
        if health2 <= 0:
            gameover = tk.Tk()
            gameover.title("risultato della partita")
            label_player1 = tk.Label(gameover, text="Player 1 Victory", font=("Helvetica", 48, "bold"), fg="gold")
            label_player1.pack()
            label_player2 = tk.Label(gameover, text="Player 2 Game Over", font=("Helvetica", 24, "bold"), fg="red")
            label_player2.pack()
            gameover.geometry('{}x{}'.format(max(label_player1.winfo_reqwidth(), label_player2.winfo_reqwidth()), label_player1.winfo_reqheight() + label_player2.winfo_reqheight()))
            gameover.mainloop()
    if god == 0:
        if health <= 0:
            gameover = tk.Tk()
            gameover.title("Risultato della partita")
            label_player1 = tk.Label(gameover, text="Player 2 Victory", font=("Helvetica", 48, "bold"), fg="gold")
            label_player1.pack()
            label_player2 = tk.Label(gameover, text="Player 1 Game Over", font=("Helvetica", 24, "bold"), fg="red")
            label_player2.pack()
            gameover.geometry('{}x{}'.format(max(label_player1.winfo_reqwidth(), label_player2.winfo_reqwidth()), label_player1.winfo_reqheight() + label_player2.winfo_reqheight()))
            gameover.mainloop()

def aggiorna_health():
    global health
    global god
    if god == 0:
        stringa_health = ' '.join('⬛' * health)
        health_lab.config(text=stringa_health)
def aggiorna_health2():
    global health2
    global god2
    if god2 == 0:
        stringa_health2 = ' '.join('⬛' * health2)
        health_lab2.config(text=stringa_health2)

def godmode(event):
    global god
    god = 1
def godmode2(event):
    global god2
    god2 = 1

def resize(dimensione):
    global giocatore, arma
    global gunpos
    x1, y1, x2, y2 = base_sf.coords(giocatore)
    base_sf.coords(giocatore, x1*dimensione, y1*dimensione, x2*dimensione, y2*dimensione)
    
    x1, y1, x2, y2 = base_sf.coords(arma)
    base_sf.coords(arma, x1*dimensione, y1*dimensione, x2*dimensione, y2*dimensione)
    x1, y1, x2, y2 = base_sf.coords(giocatore)
    base_sf.coords(arma, x2, y1 + 3, x2 + 5, y2 -3)
    gunpos = "e"

def resize2(dimensione):
    global giocatore2, arma2
    global gunpos2 
    x1, y1, x2, y2 = base_sf.coords(giocatore2)
    base_sf.coords(giocatore2, (1000-(1000-x1)*dimensione), 1000-(1000-y1)*dimensione, 1000-(1000-x2)*dimensione, 1000-(1000-y2)*dimensione)
    
    x1, y1, x2, y2 = base_sf.coords(arma2)
    base_sf.coords(arma2, x1*dimensione, y1*dimensione, x2*dimensione, y2*dimensione)
    x1, y1, x2, y2 = base_sf.coords(giocatore2)
    base_sf.coords(arma2, x2, y1 + 3, x2 + 5, y2 -3)
    gunpos2 = "e"

def collide(obj1, obj2):
    x1, y1, x2, y2 = base_sf.bbox(obj1)
    x3, y3, x4, y4 = base_sf.bbox(obj2)
    if (x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3):
        return True
    else:
        return False

def sposta():
    global gunpos
    global gunpos2
    x1, y1, x2, y2 = base_sf.coords(giocatore)
    x12, y12, x22, y22 = base_sf.coords(giocatore2)
    if "w" in pulsanti and y1 > 5:
        base_sf.move(giocatore, 0, -10)
        x1, y1, x2, y2 = base_sf.coords(giocatore)
        base_sf.coords(arma, x1 + 3, y1 - 4, x2 -3, y1)
        gunpos = "n"
    if "d" in pulsanti and x2 < 1000:
        base_sf.move(giocatore, 10, 0)
        x1, y1, x2, y2 = base_sf.coords(giocatore)
        base_sf.coords(arma, x2, y1 + 3, x2 + 4, y2 -3)
        gunpos = "e"
    if "s" in pulsanti and y2 < 1000:
        base_sf.move(giocatore, 0, 10)
        x1, y1, x2, y2 = base_sf.coords(giocatore)
        base_sf.coords(arma, x1 + 3, y2, x2 - 3, y2 + 4)
        gunpos = "s"
    if "a" in pulsanti and x1 > 5:
        base_sf.move(giocatore, -10, 0)
        x1, y1, x2, y2 = base_sf.coords(giocatore)
        base_sf.coords(arma, x1 - 4, y1 + 3, x1, y2 - 3)
        gunpos = "o"
    if "i" in pulsanti and y12 > 5:
        base_sf.move(giocatore2, 0, -10)
        x1, y1, x2, y2 = base_sf.coords(giocatore2)
        base_sf.coords(arma2, x1 + 3, y1 - 4, x2 -3, y1)
        gunpos2 = "n"
    if "l" in pulsanti and x22 < 1000:
        base_sf.move(giocatore2, 10, 0)
        x1, y1, x2, y2 = base_sf.coords(giocatore2)
        base_sf.coords(arma2, x2, y1 + 3, x2 + 4, y2 -3)
        gunpos2 = "e"
    if "k" in pulsanti and y22 < 1000:
        base_sf.move(giocatore2, 0, 10)
        x1, y1, x2, y2 = base_sf.coords(giocatore2)
        base_sf.coords(arma2, x1 + 3, y2, x2 - 3, y2 + 4)
        gunpos2 = "s"
    if "j" in pulsanti and x12 > 5:
        base_sf.move(giocatore2, -10, 0)
        x1, y1, x2, y2 = base_sf.coords(giocatore2)
        base_sf.coords(arma2, x1 - 4, y1 + 3, x1, y2 - 3)
        gunpos2 = "o"
    
    base.after(50, sposta)
def key_press(event):
    if event.keysym not in pulsanti:
        pulsanti.append(event.keysym)
def key_release(event):
    if event.keysym in pulsanti:
        pulsanti.remove(event.keysym)

def move_bullet_nord(bullet):
    global gunpos
    global health2
    x1b, y1b, x2b, y2b = base_sf.coords(bullet)
    if (y1a + 2)-(y1b + 1) < 500 and x1b < 1000 and x1b > 0 and y1b < 1000 and y1b > 0:
        base_sf.move(bullet, 0, -7)
        if collide(giocatore2,bullet):
            if 1 not in proiettili:
                proiettili.append(1)
            elif 2 not in proiettili:
                proiettili.append(2)
            elif 3 not in proiettili2:
                proiettili.append(3)
            base_sf.delete(bullet)
            aggiorna_conta_proiettili()
            health2 -=1
            aggiorna_health2()
            healthcheck()
        else:
            base_sf.after(10, move_bullet_nord, bullet)
    else:
        if 1 not in proiettili:
            proiettili.append(1)
        elif 2 not in proiettili:
            proiettili.append(2)
        elif 3 not in proiettili:
            proiettili.append(3)
        base_sf.delete(bullet)
        aggiorna_conta_proiettili()
def move_bullet_est(bullet):
    global gunpos
    global health2
    x1b, y1b, x2b, y2b = base_sf.coords(bullet)
    if (x1b + 1) - (x1a + 2) < 500 and x1b < 1000 and x1b > 0 and y1b < 1000 and x1b > 0:
        base_sf.move(bullet, 7, 0)
        if collide(giocatore2,bullet):
            if 1 not in proiettili:
                proiettili.append(1)
            elif 2 not in proiettili:
                proiettili.append(2)
            elif 3 not in proiettili2:
                proiettili.append(3)
            base_sf.delete(bullet)
            aggiorna_conta_proiettili()
            health2 -=1
            aggiorna_health2()
            healthcheck()
        else:
            base_sf.after(10, move_bullet_est, bullet)
    else:
        if 1 not in proiettili:
            proiettili.append(1)
        elif 2 not in proiettili:
            proiettili.append(2)
        elif 3 not in proiettili:
            proiettili.append(3)
        base_sf.delete(bullet)
        aggiorna_conta_proiettili()
def move_bullet_sud(bullet):
    global gunpos
    global health2
    x1b, y1b, x2b, y2b = base_sf.coords(bullet)
    if (y1b + 1)-(y1a + 2) < 500 and x1b < 1000 and x1b > 0 and y1b < 1000 and y1b > 0:
        base_sf.move(bullet, 0, 7)
        if collide(giocatore2,bullet):
            if 1 not in proiettili:
                proiettili.append(1)
            elif 2 not in proiettili:
                proiettili.append(2)
            elif 3 not in proiettili2:
                proiettili.append(3)
            base_sf.delete(bullet)
            aggiorna_conta_proiettili()
            health2 -=1
            aggiorna_health2()
            healthcheck()
        else:
            base_sf.after(10, move_bullet_sud, bullet)
    else:
        if 1 not in proiettili:
            proiettili.append(1)
        elif 2 not in proiettili:
            proiettili.append(2)
        elif 3 not in proiettili:
            proiettili.append(3)
        base_sf.delete(bullet)
        aggiorna_conta_proiettili()
def move_bullet_ovest(bullet):
    global gunpos
    global health2
    x1b, y1b, x2b, y2b = base_sf.coords(bullet)
    if (x1a + 2)-(x1b + 1) < 500 and x1b < 1000 and x1b > 0 and y1b < 1000 and x1b > 0:
        base_sf.move(bullet, -7, 0)
        if collide(giocatore2,bullet):
            if 1 not in proiettili:
                proiettili.append(1)
            elif 2 not in proiettili:
                proiettili.append(2)
            elif 3 not in proiettili2:
                proiettili.append(3)
            base_sf.delete(bullet)
            aggiorna_conta_proiettili()
            health2 -=1
            aggiorna_health2()
            healthcheck()
        else:
            base_sf.after(10, move_bullet_ovest, bullet)
    else:
        if 1 not in proiettili:
            proiettili.append(1)
        elif 2 not in proiettili:
            proiettili.append(2)
        elif 3 not in proiettili:
            proiettili.append(3)
        base_sf.delete(bullet)
        aggiorna_conta_proiettili()
def shoot(event):
    global x1a, y1a, x2a, y2a
    x1a, y1a, x2a, y2a = base_sf.coords(arma)

    if proiettili:
        if proiettili[0] == 1:
            proiettili.remove(1)
            aggiorna_conta_proiettili()
            if gunpos == "n":
                bullet1 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y2a + 10, fill="blue")
                move_bullet_nord(bullet1)
            elif gunpos == "e":
                bullet1 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y2a - 2, fill="blue")
                move_bullet_est(bullet1)
            elif gunpos == "s":
                bullet1 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y1a + 17, fill="blue")
                move_bullet_sud(bullet1)
            else:
                bullet1 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y1a + 13, fill="blue")
                move_bullet_ovest(bullet1)
        elif proiettili[0] == 2:
            proiettili.remove(2)
            aggiorna_conta_proiettili()
            if gunpos == "n":
                bullet2 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y2a + 10, fill="blue")
                move_bullet_nord(bullet2)
            elif gunpos == "e":
                bullet2 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y2a - 2, fill="blue")
                move_bullet_est(bullet2)
            elif gunpos == "s":
                bullet2 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y1a + 17, fill="blue")
                move_bullet_sud(bullet2)
            else:
                bullet2 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y1a + 13, fill="blue")
                move_bullet_ovest(bullet2)
        else:
            proiettili.remove(3)
            aggiorna_conta_proiettili()
            if gunpos == "n":
                bullet3 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y2a + 10, fill="blue")
                move_bullet_nord(bullet3)
            elif gunpos == "e":
                bullet3 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y2a - 2, fill="blue")
                move_bullet_est(bullet3)
            elif gunpos == "s":
                bullet3 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y1a + 17, fill="blue")
                move_bullet_sud(bullet3)
            else:
                bullet3 = base_sf.create_rectangle(x1a + 2, y1a + 2, x1a + 13, y1a + 13, fill="blue")
                move_bullet_ovest(bullet3)

def move_bullet_nord2(bullet2):
    global gunpos2
    global health
    x1b2, y1b2, x2b2, y2b2 = base_sf.coords(bullet2)
    if (y1a2 + 2) - (y1b2 + 1) < 500 and x1b2 < 1000 and x1b2 > 0 and y1b2 < 1000 and y1b2 > 0:
        base_sf.move(bullet2, 0, -7)
        if collide(giocatore,bullet2):
            if 1 not in proiettili2:
                proiettili2.append(1)
            elif 2 not in proiettili2:
                proiettili2.append(2)
            elif 3 not in proiettili2:
                proiettili2.append(3)
            base_sf.delete(bullet2)
            aggiorna_conta_proiettili2()
            health -=1
            aggiorna_health()
            healthcheck()
        else:
            base_sf.after(10, move_bullet_nord2, bullet2)
    else:
        if 1 not in proiettili2:
            proiettili2.append(1)
        elif 2 not in proiettili2:
            proiettili2.append(2)
        elif 3 not in proiettili2:
            proiettili2.append(3)
        base_sf.delete(bullet2)
        aggiorna_conta_proiettili2()

def move_bullet_est2(bullet2):
    global gunpos2
    global health
    x1b2, y1b2, x2b2, y2b2 = base_sf.coords(bullet2)
    if (x1b2 + 1) - (x1a2 + 2) < 500 and x1b2 < 1000 and x1b2 > 0 and y1b2 < 1000 and x1b2 > 0:
        base_sf.move(bullet2, 7, 0)
        if collide(giocatore,bullet2):
            if 1 not in proiettili2:
                proiettili2.append(1)
            elif 2 not in proiettili2:
                proiettili2.append(2)
            elif 3 not in proiettili2:
                proiettili2.append(3)
            base_sf.delete(bullet2)
            aggiorna_conta_proiettili2()
            health -=1
            aggiorna_health()
            healthcheck()
        else:
            base_sf.after(10, move_bullet_est2, bullet2)
    else:
        if 1 not in proiettili2:
            proiettili2.append(1)
        elif 2 not in proiettili2:
            proiettili2.append(2)
        elif 3 not in proiettili2:
            proiettili2.append(3)
        base_sf.delete(bullet2)
        aggiorna_conta_proiettili2()

def move_bullet_sud2(bullet2):
    global gunpos2
    global health
    x1b2, y1b2, x2b2, y2b2 = base_sf.coords(bullet2)
    if (y1b2 + 1) - (y1a2 + 2) < 500 and x1b2 < 1000 and x1b2 > 0 and y1b2 < 1000 and y1b2 > 0:
        base_sf.move(bullet2, 0, 7)
        if collide(giocatore,bullet2):
            if 1 not in proiettili2:
                proiettili2.append(1)
            elif 2 not in proiettili2:
                proiettili2.append(2)
            elif 3 not in proiettili2:
                proiettili2.append(3)
            base_sf.delete(bullet2)
            aggiorna_conta_proiettili2()
            health -=1
            aggiorna_health()
            healthcheck()
        else:
            base_sf.after(10, move_bullet_sud2, bullet2)
    else:
        if 1 not in proiettili2:
            proiettili2.append(1)
        elif 2 not in proiettili2:
            proiettili2.append(2)
        elif 3 not in proiettili2:
            proiettili2.append(3)
        base_sf.delete(bullet2)
        aggiorna_conta_proiettili2()

def move_bullet_ovest2(bullet2):
    global gunpos2
    global health
    x1b2, y1b2, x2b2, y2b2 = base_sf.coords(bullet2)
    if (x1a2 + 2) - (x1b2 + 1) < 500 and x1b2 < 1000 and x1b2 > 0 and y1b2 < 1000 and x1b2 > 0:
        base_sf.move(bullet2, -7, 0)
        if collide(giocatore,bullet2):
            if 1 not in proiettili2:
                proiettili2.append(1)
            elif 2 not in proiettili2:
                proiettili2.append(2)
            elif 3 not in proiettili2:
                proiettili2.append(3)
            base_sf.delete(bullet2)
            aggiorna_conta_proiettili2()
            health -=1
            aggiorna_health()
            healthcheck()
        else:
            base_sf.after(10, move_bullet_ovest2, bullet2)
    else:
        if 1 not in proiettili2:
            proiettili2.append(1)
        elif 2 not in proiettili2:
            proiettili2.append(2)
        elif 3 not in proiettili2:
            proiettili2.append(3)
        base_sf.delete(bullet2)
        aggiorna_conta_proiettili2()

def shoot2(event):
    global x1a2, y1a2, x2a2, y2a2
    x1a2, y1a2, x2a2, y2a2 = base_sf.coords(arma2)

    if proiettili2:
        if proiettili2[0] == 1:
            proiettili2.remove(1)
            aggiorna_conta_proiettili2()
            if gunpos2 == "n":
                bullet12 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y2a2 + 10, fill="red")
                move_bullet_nord2(bullet12)
            elif gunpos2 == "e":
                bullet12 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y2a2 - 2, fill="red")
                move_bullet_est2(bullet12)
            elif gunpos2 == "s":
                bullet12 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y1a2 + 17, fill="red")
                move_bullet_sud2(bullet12)
            else:
                bullet12 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y1a2 + 13, fill="red")
                move_bullet_ovest2(bullet12)
        elif proiettili2[0] == 2:
            proiettili2.remove(2)
            aggiorna_conta_proiettili2()
            if gunpos2 == "n":
                bullet22 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y2a2 + 10, fill="red")
                move_bullet_nord2(bullet22)
            elif gunpos2 == "e":
                bullet22 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y2a2 - 2, fill="red")
                move_bullet_est2(bullet22)
            elif gunpos2 == "s":
                bullet22 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y1a2 + 17, fill="red")
                move_bullet_sud2(bullet22)
            else:
                bullet22 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y1a2 + 13, fill="red")
                move_bullet_ovest2(bullet22)
        else:
            proiettili2.remove(3)
            aggiorna_conta_proiettili2()
            if gunpos2 == "n":
                bullet32 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y2a2 + 10, fill="red")
                move_bullet_nord2(bullet32)
            elif gunpos2 == "e":
                bullet32 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y2a2 - 2, fill="red")
                move_bullet_est2(bullet32)
            elif gunpos2 == "s":
                bullet32 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y1a2 + 17, fill="red")
                move_bullet_sud2(bullet32)
            else:
                bullet32 = base_sf.create_rectangle(x1a2 + 2, y1a2 + 2, x1a2 + 13, y1a2 + 13, fill="red")
                move_bullet_ovest2(bullet32)

def aggiorna_conta_proiettili():
    global proiettili
    stringa_proiettili = ' '.join('⬛' * len(proiettili))
    conta_proiettili_lab.config(text=stringa_proiettili)

def aggiorna_conta_proiettili2():
    global proiettili2
    stringa_proiettili2 = ' '.join('⬛' * len(proiettili2))
    conta_proiettili_lab2.config(text=stringa_proiettili2)


def esci(event):
    base.destroy()

base = tk.Tk()
base.geometry('1500x1000')
base.title("back to square one")

base_sf = tk.Canvas(base, width=1000, height=1000, bg="white")
base_sf.pack()
base_sf.focus_set()

giocatore = base_sf.create_rectangle(1, 1, 11, 11, fill="blue")
arma = base_sf.create_rectangle(11, 4, 14, 8, fill="blue")

giocatore2 = base_sf.create_rectangle(999,999,989,989, fill="red")
arma2 = base_sf.create_rectangle(989,996,986,992, fill="red")

proiettili = [1,2,3]
proiettili2 = [1,2,3]  

health = 3
health2 = 3

god = 0
god2 = 0

conta_proiettili_lab = tk.Label(base, text="", fg="blue")
conta_proiettili_lab.place(x=100,y=395)
aggiorna_conta_proiettili()

conta_proiettili_lab2 = tk.Label(base, text="", fg="red")
conta_proiettili_lab2.place(x=1375,y=395)
aggiorna_conta_proiettili2()

health_lab = tk.Label(base, text="", fg="green")
health_lab.place(x=100,y=595)
aggiorna_health()

health_lab2 = tk.Label(base, text="", fg="green")
health_lab2.place(x=1375,y=595)
aggiorna_health2()

resize_val = 2
resize(resize_val)
resize2(resize_val)

pulsanti = []
base.bind("<KeyPress>", key_press)
base.bind("<KeyRelease>", key_release)
base.bind("<space>", shoot)

base.bind("<Return>", shoot2)

base.bind("<Escape>", esci)

base.bind("wswsadadwasdwasd", godmode)
base.bind("ikikjljlijklijkl", godmode2)

base.bind("")
sposta()

base.mainloop()