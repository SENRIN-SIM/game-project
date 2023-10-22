from tkinter import *
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
app_height = window.winfo_screenheight()

window.geometry(f'{app_width}x{app_height}')

frame = Frame(window, width=app_width, height=app_height)
frame.pack()

canvas = Canvas(frame, width=app_width, height=app_height)
canvas.pack()
# ___________________Image_________________________
interface_Image = PhotoImage(file="img/interface.png")
bg_Image =PhotoImage(file="img/bg_img.png")
hero_Image = PhotoImage(file="img/hero player .png")
bonla = PhotoImage(file="img/bonla.png")
backclick = PhotoImage(file="img/singback_1-removebg-preview.png")

# ________________________interface_______________________

def interface():

    canvas.create_image(600,320,image=interface_Image)
    winsound.PlaySound("sound\\mixkit-game-level-completed-2059.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

    canvas.create_text(650,250,text="GAME",font=('212BabyGirl', 60 ,'bold'),fill='black',tags='start')

    # canvas.create_text(650,350,text="HELP",font=('212BabyGirl', 60 ,'bold'),fill='black',tags='help')

    # canvas.create_text(650,450,text="EXIT",font=('212BabyGirl', 60 ,'bold'),fill='black',tags='exit')

interface()
# _____________________Show Level________________
def playGame(event):

    canvas.delete('all')
    startGame()

canvas.tag_bind('start','<Button-1>',playGame)

# ________________start game__________________


def startGame():
    canvas.create_image(600,320, image=bg_Image)
    


    canvas.create_rectangle(0, 800, app_width, app_height, fill="black", tags="PLATFORM")
    canvas.create_rectangle(0, 700, app_width, 850, fill="blue", tags="PLATFORM")
    
    canvas.create_rectangle(160, 600, 240, 700, fill="coral", tags="PLATFORM")
    canvas.create_rectangle(240, 510, 360, 530, fill="green", tags="PLATFORM")
    canvas.create_rectangle(240, 530, 360, 650, fill="coral", tags="PLATFORM")


    # ========

    canvas.create_rectangle(500, 350, 600, 400, fill="coral", tags="PLATFORM")
    canvas.create_rectangle(500, 330, 600, 350, fill="green", tags="PLATFORM", outline = "green" )

    canvas.create_rectangle(890, 350, 1000, 400, fill="coral", tags="PLATFORM")
    canvas.create_rectangle(890, 330, 1000, 350, fill="green", tags="PLATFORM", outline = "green" )
    # =========
    canvas.create_rectangle(160, 580, 270, 600, fill="green", tags="PLATFORM")

    canvas.create_rectangle(1150,400, 1400, 750, fill="coral", tags="PLATFORM", outline = "green" )
    canvas.create_rectangle(360, 620, 1150, 650, fill="green", tags="PLATFORM", outline = "green" )
    # canvas.create_image(420, 610, image=bonla, tags="PLATFORM" )

    # canvas.create_rectangle(0, 0, 40, 700, fill="coral", tags="PLATFORM", outline = "orange" )
    canvas.create_rectangle(0, 650, 1150, 700, fill="brown", tags="PLATFORM", outline = "brown" )
    canvas.create_rectangle(0, 630, 300, 650, fill="green", tags="PLATFORM", outline = "green" )
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

    def jump(force):
        if force > 0:
            if check_movement(0, -force):
                canvas.move(player, 0, -force)
                window.after(TIMED_LOOP, jump, force- 3)


    def start_move(event):
        if event.keysym not in keyPressed:
            keyPressed.append(event.keysym)
            if len(keyPressed) == 1:
                move()

    def move():
        if not keyPressed == []:
            x = 0
            if "Left" in keyPressed:
                x -= SPEED
            if "Right" in keyPressed:
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
    character1 = canvas.create_rectangle(850, 300, 910, 320, fill="blue", tags="PLATFORM", outline = "white" )

    character2 = canvas.create_rectangle(500, 300, 560, 320, fill="orange", tags="PLATFORM", outline = "white" )

    # ________________Win___________________


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