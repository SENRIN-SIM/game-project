from tkinter import *
import tkinter as tk
# from email.mime import image
import winsound
import random

JUMP_FORCE = 30
SPEED = 7
GRAVITY_FORCE = 9

TIMED_LOOP = 10
MOVE_INCREMENT = 10
COUNT_DRINK =1

keyPressed = []

window = Tk()
window.title("Sok")
app_width = window.winfo_screenwidth()
print(app_width)
app_height = window.winfo_screenheight()

window.geometry(f'{app_width}x{app_height}')

frame = Frame(window, width=app_width, height=app_height)
frame.pack()

canvas = Canvas(frame, width=app_width, height=app_height)
canvas.pack()
# ___________________Imagelevel1_________________________
interface_Image = PhotoImage(file="img/bg_Img1.png")
bg_Image =PhotoImage(file="img/interface.png")
hero_Image = PhotoImage(file="img/hero_right.png")
heroimg_left = PhotoImage(file="img/hero_left.png")

bonla = PhotoImage(file="img/bonla-removebg.png")
backclick = PhotoImage(file="img/singback_1-removebg-preview.png")
door = PhotoImage(file="img/doors 1.png")
wall = PhotoImage(file="img/wall.PNG")
iland = PhotoImage(file="img/iland.png")
land2 = PhotoImage(file="img/land2.png")
trees = PhotoImage(file="img/tree.png")
trees2 = PhotoImage(file="img/chers.png")
wall2 = PhotoImage(file="img/wall2.png")
helping = PhotoImage(file="img/tips.png")
komnop = PhotoImage(file="img/beer.png")
button = PhotoImage(file="img/button-removebg-preview.png")
leve_image = PhotoImage(file="img/next_level_img.png")

# __________________________Imagelevel2___________________________
bg_Image2 =PhotoImage(file="imgGame2/bgimage2.png")
dianond = PhotoImage(file="imgGame2/gold.png")
kos = PhotoImage(file="imgGame2/floatgold.png")
kos2 = PhotoImage(file="imgGame2/start.png")
daimon   = PhotoImage(file="imgGame2/gold.png")
trees02 = PhotoImage(file="imgGame2/floatgold.png")
iland_goal = PhotoImage(file="imgGame2/floatgold.png")
bom = PhotoImage(file="imgGame2/bom.png")
mott = PhotoImage(file="imgGame2/icethorn.png")
test = PhotoImage(file="imgGame2/test.png")

# ________________________interface_______________________

def interface():

    canvas.create_image(600,320,image=interface_Image)
    winsound.PlaySound("sound\\mixkit-game-level-completed-2059.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

    canvas.create_image(300,550,image=button, tags='start')
    canvas.create_text(300,550,text="GAME",font=('212BabyGirl', 50 ,'bold'),fill='white', tags='start')

    canvas.create_image(650,550,image=button, tags='start')
    canvas.create_text(650,550,text="HELP",font=('212BabyGirl', 50 ,'bold'),fill='white',tags='help')

    canvas.create_image(1000,550,image=button, tags='start')
    canvas.create_text(1000,550,text="EXIT",font=('212BabyGirl', 50 ,'bold'),fill='white',tags='exit')

   
interface()
# _____________________Show Level________________
def playGame(event):

    canvas.delete('all')
    startGame()
    click_sound()

canvas.tag_bind('start','<Button-1>',playGame)

# ________________________help_______________________
def need_help(event):

    canvas.delete('all')
    help()
    click_sound()
canvas.tag_bind('help','<Button-1>',need_help)
# ___________________________exit________________-_________
def exit(event):

    window.quit()
    click_sound()
canvas.tag_bind('exit','<Button-1>',exit)

# __________________help pacg_____________________________

def help():
    # canvas.create_image(600,320, image=bg_Image)
    canvas.create_image(700,320, image=helping, anchor=CENTER)
    winsound.PlaySound("sound\\help.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
# ____________________click_back_________________
    def back_btn():
        canvas.create_image(100,50,image=backclick, tags='bak')
        canvas.create_text(100,50,text="Back", font='212BabyGirl 15 bold', fill='white', tags='bak')
    back_btn()
    def bakClick(event):
        canvas.delete('all')
        interface()
    canvas.tag_bind('bak','<Button-1>',bakClick)

# __________________sound_______________________

def jumpsound():
     winsound.PlaySound("sound\\jump.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
def walksound():
     winsound.PlaySound("sound\\walk.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
def win_sond():
     winsound.PlaySound("sound\\mixkit-game-level-completed-2059.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
def lost_sond():
     winsound.PlaySound("sound\\help.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
def click_sound():
     winsound.PlaySound("sound\\walk.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    
# ________________start game__________________

def startGame():
    canvas.create_image(600,320, image=bg_Image)
    
    x = 170
    for i in range(2):
        canvas.create_image(x,590, image=wall2, tags="PLATFORM")
        x += wall.width()
    canvas.create_image(330,480, image=wall2, tags="PLATFORM")

    canvas.create_image(550, 350, image=iland, tags="PLATFORM" )
    canvas.create_image(900, 350, image=iland, tags="PLATFORM" )

    home = canvas.create_image(1320,100, image=door, tags="won" )
    x=1180
    for i in range(3):
        character1 = canvas.create_image(x,160, image=trees2, tags="PLATFORM")
        x += trees2.width()

    canvas.create_image(1250, 430, image=land2, tags="PLATFORM" )
    canvas.create_image(1270, 325, image=trees)
    beers = canvas.create_image(1290,360, image=komnop, tags="beer")

    # Create characters as rectangles on the canvas
    character1 = canvas.create_rectangle(850, 250, 910, 270, fill="orange", tags="PLATFORM", outline = "" )

    character2 = canvas.create_rectangle(500, 250, 560, 270, fill="orange", tags="PLATFORM", outline = "" )

    x = 410
    for i in range(25):
        denger = canvas.create_image(x, 640, image=bonla, tags="lost" )
        x += bonla.width()
    
# ===========/

    x=0
    for i in range(12):
        canvas.create_image(x, 680, image=wall2, tags="PLATFORM" )
        x += wall2.width()
    player = canvas.create_image(10,10, image=hero_Image, anchor=NW)

    def check_movement(direction_x=0, direction_y=0, checkGround=False):
        coord = canvas.coords(player)

        platforms = canvas.find_withtag("PLATFORM")
        if coord[0] + direction_x < 1 or coord[0] + direction_x > app_width:
            return False

        if checkGround:
            overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] +hero_Image.width(), coord[1]+hero_Image.height())
        else:
            overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+direction_x, coord[1]+direction_y)

        coord = canvas.coords(player)
        coord = canvas.coords(denger)
        coord = canvas.coords(beers)
        platforms = canvas.find_withtag("PLATFORM")
        wonner = canvas.find_withtag("won")
        loser = canvas.find_withtag("lost")
        drink = canvas.find_withtag("beer")
        # ===============1
        for plf in wonner:
            if plf in overlap:
                check_winner()
                win_sond()
                
        for plf in wonner:
            if plf in overlap:
                return False
        for platform in platforms:
            if platform in overlap:
                return False
        # ========================2
        for plf in loser:
            if plf in overlap:
                check_loster()
                lost_sond()

        for platform in platforms:
            if platform in overlap:
                return False
                
        # ========================3
        for plf in drink:
            if plf in overlap:
                drink_beer()    
        for platform in platforms:
            if platform in overlap:

                return False
        # =========================
        return True
    # _______________winner1______________
    def check_winner():
        
        canvas.create_image(0,0,image=leve_image,anchor=NW)
        # canvas.create_text(600, 500, text="YOU WON! BRO", font=("Ink free", 70),)
        canvas.create_text(220,300,text="YOU WON!",font=('212BabyGirl', 50 ,'bold'),fill='white')
        canvas.create_text(250, 450, text="NEXT-LEVEL", font=('212BabyGirl', 50 ,'bold'),fill='white', tags="level_2")
    # ________________go to next_level__________________
    def next_level(event):
        canvas.delete('all')
        startGame_2()
        click_sound()
    canvas.tag_bind('level_2','<Button-1>',next_level)
    # ___________________play again_________________
    def play_again(event):
        canvas.delete('all')
        startGame()
        click_sound()
    canvas.tag_bind('try','<Button-1>',play_again)
        
    # _________________lost_________________
    def check_loster():
        # canvas.create_text(600, 100, text="K.O!", font=("Ink free", 70))
        canvas.create_image(0,0,image=leve_image,anchor=NW)
        canvas.create_text(220,300,text="YOU LOST!",font=('212BabyGirl', 50 ,'bold'),fill='white')
        canvas.create_text(250, 450, text="TRY AGAIN?", font=('212BabyGirl', 50 ,'bold'),fill='white', tags="try")

    # _______________get beer3____________________
    def drink_beer():
        canvas.itemconfig(beers,image=bonla)
        
# _______________jump_______________________

    def jump(force):
        if force > 0:
            if check_movement(0, -force):
                canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force- 2.5)     

    def start_move(event):
        if event.keysym not in keyPressed:
            keyPressed.append(event.keysym)
            if len(keyPressed) == 1:
                move()

    def move():
        if not keyPressed == []:
            x = 0
            if "Left" in keyPressed:
                canvas.itemconfig(player, image=heroimg_left)
                x -= SPEED
            if "Right" in keyPressed:
                canvas.itemconfig(player, image=hero_Image)
                x += SPEED
            if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
                jump(JUMP_FORCE)
                jumpsound()
            if check_movement(x):
                canvas.move(player, x, 0)
                window.after(TIMED_LOOP, move)

    def gravity():
        if check_movement(0, GRAVITY_FORCE, True):
            canvas.move(player, 0 , GRAVITY_FORCE)
        window.after(TIMED_LOOP, gravity)
    def stop_move(event):
        global keyPressed
        if event.keysym in keyPressed:
            keyPressed.remove(event.keysym)

    # ========================================
    def move_characters():
        # Move the characters
        canvas.move(character1, MOVE_INCREMENT, 0)
        canvas.move(character2, -MOVE_INCREMENT, 0)

        # Get the current position of the characters
        char1_coords = canvas.coords(character1)
        char2_coords = canvas.coords(character2)

        # Check if characters have moved beyond the canvas boundaries
        if char1_coords[2] > app_width:
            canvas.move(character1, -app_width, 0)
        if char2_coords[0]< 0:
            canvas.move(character2, app_width, 0)

        # Scroll the canvas to keep characters in view
        canvas.xview_moveto((char1_coords[2] + char2_coords[0]) / (2 * app_width))

        # Schedule the next character movement
        canvas.after(100, move_characters)  # Adjust the delay as needed

# __________________click to back_______________________
    def back_btn():
        canvas.create_image(100,50,image=backclick, tags='bak')
        canvas.create_text(100,50,text="Back", font='212BabyGirl 15 bold', fill='white', tags='bak')
    back_btn()
    def bakClick(event):
        canvas.delete('all')
        interface()
        click_sound()
    canvas.tag_bind('bak','<Button-1>',bakClick)

    # Start moving the characters
    move_characters()

    # ========================================

    gravity()

    window.bind("<Key>", start_move)
    window.bind("<KeyRelease>", stop_move)

# __________________click to back_______________________

def startGame_2():
    canvas.create_image(600,320, image=bg_Image2)
    
    canvas.create_image(100,620, image=kos, tags="PLATFORM")

    canvas.create_image(340, 650, image=kos2, tags="PLATFORM" )
    canvas.create_image(530, 550, image=kos2, tags="PLATFORM" )
    canvas.create_image(730, 450, image=kos2, tags="PLATFORM" )
    beers = canvas.create_image(700, 400, image=test, tags="beer")
    # bomm = canvas.create_image(730, 350, image=bom)
    motts = canvas.create_image(800, 400, image=bom, tags="lost")
    canvas.create_image(930, 350, image=kos2, tags="PLATFORM" )

    home = canvas.create_image(1275,150, image=daimon, tags="won" )

    canvas.create_image(1200,260, image=iland_goal, tags="PLATFORM")

    x = 0
    for i in range(30):
        denger = canvas.create_image(x, 800, image=trees, tags="lost" )
        x += bonla.width()
    
# ===========/
    
    player = canvas.create_image(10,10, image=hero_Image, anchor=NW)

    def check_movement(direction_x=0, direction_y=0, checkGround=False):
        coord = canvas.coords(player)

        platforms = canvas.find_withtag("PLATFORM")
        if coord[0] + direction_x < 1 or coord[0] + direction_x > app_width:
            return False

        if checkGround:
            overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] +hero_Image.width(), coord[1]+hero_Image.height())
        else:
            overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+direction_x, coord[1]+direction_y)

        coord = canvas.coords(player)
        coord = canvas.coords(denger)
        coord = canvas.coords(beers)
        platforms = canvas.find_withtag("PLATFORM")
        wonner = canvas.find_withtag("won")
        loser = canvas.find_withtag("lost")
        drink = canvas.find_withtag("beer")
        # ===============1
        for plf in wonner:
            if plf in overlap:
                check_winner()
                win_sond()
        for plf in wonner:
            if plf in overlap:
                return False
        for platform in platforms:
            if platform in overlap:
                return False
        # ========================2
        for plf in loser:
            if plf in overlap:
                check_loster()
                lost_sond()

        for platform in platforms:
            if platform in overlap:
                return False
                
        # ========================3
        for plf in drink:
            if plf in overlap:
                drink_beer()    
        # for platform in platforms:
        #     if platform in overlap:

        #         return False
        # =========================
        return True
    # _______________winner1______________
    def check_winner():
        canvas.create_image(0,0,image=leve_image,anchor=NW)
        canvas.create_text(220,300,text="YOU WON!",font=('212BabyGirl', 50 ,'bold'),fill='white')
        canvas.create_text(250, 450, text="NEXT-LEVEL", font=('212BabyGirl', 50 ,'bold'),fill='white', tags="level_2")
    # ________________go to next_level__________________
    def next_level(event):
        canvas.delete('all')
        startGame()
        click_sound()
    canvas.tag_bind('level_2','<Button-1>',next_level)
    # ___________________play again_________________
    def play_again(event):
        canvas.delete('all')
        startGame_2()
        click_sound()
    canvas.tag_bind('try','<Button-1>',play_again)
        
    # _________________lost_________________
    def check_loster():
        canvas.create_image(0,0,image=leve_image,anchor=NW)
        canvas.create_text(220,300,text="YOU LOST!",font=('212BabyGirl', 50 ,'bold'),fill='white')
        canvas.create_text(250, 450, text="TRY AGAIN?", font=('212BabyGirl', 50 ,'bold'),fill='white', tags="try")

    # _______________get beer3____________________
    def drink_beer():
        canvas.itemconfig(motts,image=mott)

# _______________jump_______________________

    def jump(force):
        if force > 0:
            if check_movement(0, -force):
                canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force- 2.5)
            
    def start_move(event):
        if event.keysym not in keyPressed:
            keyPressed.append(event.keysym)
            if len(keyPressed) == 1:
                move()

    def move():
        if not keyPressed == []:
            x = 0
            if "Left" in keyPressed:
                canvas.itemconfig(player, image=heroimg_left)
                x -= SPEED
            if "Right" in keyPressed:
                canvas.itemconfig(player, image=hero_Image)
                x += SPEED
            if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
                jump(JUMP_FORCE)
                jumpsound()
            if check_movement(x):
                canvas.move(player, x, 0)
                window.after(TIMED_LOOP, move)

    def gravity():
        if check_movement(0, GRAVITY_FORCE, True):
            canvas.move(player, 0 , GRAVITY_FORCE)
        window.after(TIMED_LOOP, gravity)
    def stop_move(event):
        global keyPressed
        if event.keysym in keyPressed:
            keyPressed.remove(event.keysym)

# __________________click to back_______________________
    def back_btn():
        canvas.create_image(100,50,image=backclick, tags='bak')
        canvas.create_text(100,50,text="Back", font='212BabyGirl 15 bold', fill='white', tags='bak')
    back_btn()
    def bakClick(event):
        canvas.delete('all')
        interface()
        click_sound()
    canvas.tag_bind('bak','<Button-1>',bakClick)

    # ========================================

    gravity()

    window.bind("<Key>", start_move)
    window.bind("<KeyRelease>", stop_move)

window.mainloop()