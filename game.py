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
# ___________________Image_________________________
interface_Image = PhotoImage(file="img/bg_img.png")
bg_Image =PhotoImage(file="img/interface.png")
hero_Image = PhotoImage(file="img/Hero Player .png")
heroimg_left = PhotoImage(file="img/Hero_Player_left-removebg-preview.png")
bonla = PhotoImage(file="img/bonla.png")
backclick = PhotoImage(file="img/singback_1-removebg-preview.png")
door = PhotoImage(file="img/doors 1.png")
wall = PhotoImage(file="img/wall.PNG")
iland = PhotoImage(file="img/iland.png")
land2 = PhotoImage(file="img/land2.png")
trees = PhotoImage(file="img/tree.png")
wall2 = PhotoImage(file="img/wall2.png")


# ________________________interface_______________________

def interface():

    canvas.create_image(600,320,image=interface_Image)
    winsound.PlaySound("sound\\mixkit-game-level-completed-2059.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

    canvas.create_text(650,250,text="GAME",font=('212BabyGirl', 60 ,'bold'),fill='white', tags='start')

    canvas.create_text(650,350,text="HELP",font=('212BabyGirl', 60 ,'bold'),fill='white',tags='help')

    canvas.create_text(650,450,text="EXIT",font=('212BabyGirl', 60 ,'bold'),fill='white',tags='exit')

interface()
# _____________________Show Level________________
def playGame(event):

    canvas.delete('all')
    startGame()

canvas.tag_bind('start','<Button-1>',playGame)

# ________________start game__________________


def startGame():
    canvas.create_image(600,320, image=bg_Image)
    
    x = 170
    for i in range(2):
        canvas.create_image(x,580, image=wall2, tags="PLATFORM")
        x += wall.width()
    canvas.create_image(330,480, image=wall2, tags="PLATFORM")

    canvas.create_image(550, 350, image=iland, tags="PLATFORM" )
    canvas.create_image(900, 350, image=iland, tags="PLATFORM" )

    home = canvas.create_image(1280,100, image=door )


    canvas.create_image(1250, 430, image=land2, tags="PLATFORM" )
    canvas.create_image(1270, 325, image=trees)


    x = 410
    for i in range(10):
        denger = canvas.create_image(x, 640, image=bonla, tags="PLATFORM" )
        x += bonla.width()
    

# ===========/

    x=0
    for i in range(12):
        canvas.create_image(x, 680, image=wall, tags="PLATFORM" )
        x += wall.width()
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
        for platform in platforms:
            if platform in overlap:
                return False
        return True
# _______________jump_______________________

    def jump(force):
        if force > 0:
            if check_movement(0, -force):
                canvas.move(player, 0, -force)
                window.after(TIMED_LOOP, jump, force- 3)
                # winsound.PlaySound("sound\\jump.wav", winsound.SND_ASYNC | winsound.SND_ASYNC, tag="sound")
            


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
        if char2_coords[0] < 0:
            canvas.move(character2, app_width, 0)

        # Scroll the canvas to keep characters in view
        canvas.xview_moveto((char1_coords[2] + char2_coords[0]) / (2 * app_width))

        # Schedule the next character movement
        canvas.after(100, move_characters)  # Adjust the delay as needed


    # Create characters as rectangles on the canvas
    character1 = canvas.create_rectangle(850, 250, 910, 270, fill="orange", tags="PLATFORM", outline = "" )

    character2 = canvas.create_rectangle(500, 250, 560, 270, fill="orange", tags="PLATFORM", outline = "" )

    # ________________lost condition___________________

    def Lost():

        canvas.create_rectangle(220,200,1000,500,fill='white')

        canvas.create_text(600,250,text="You Lost!",font="212BabyGirl 60 bold", fill="black")

        # canvas.create_image(300,350,image=fruits)
        canvas.create_text(400,350,text='score X ', font='212BabyGirl 25 bold',fill='black')
        # canvas.create_text(480,350,text=score,font='212BabyGirl 30 bold',fill='red')

        # canvas.create_image(700,350,image=heart)
        canvas.create_text(790,350,text='Heart X ', font='212BabyGirl 25 bold',fill='black')
        canvas.create_text(860,350,text='0',font='212BabyGirl 30 bold',fill='red')

        canvas.create_text(900,450,text='Menu',font='212BabyGirl 30',fill='black',tags='ne')
    
        if player[3] <= denger[1]:
            Lost()

# __________________click to back_______________________
    def back_btn():
        canvas.create_image(100,50,image=backclick, tags='bak')
        canvas.create_text(100,50,text="Back", font='212BabyGirl 15 bold', fill='white', tags='bak')
    back_btn()
    def bakClick(event):
        canvas.delete('all')
        interface()
    canvas.tag_bind('bak','<Button-1>',bakClick)



    # Start moving the characters
    move_characters()


    # ========================================


    gravity()

    window.bind("<Key>", start_move)
    window.bind("<KeyRelease>", stop_move)





window.mainloop()