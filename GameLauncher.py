import tkinter
import os
from PIL import Image, ImageTk

# Create root window
root = tkinter.Tk()
root.geometry("400x400")
root.title("Game Launcher by Alex")

canvas = tkinter.Canvas(root, width=400, height=400)
canvas.pack()

img = ImageTk.PhotoImage(Image.open('resources/retro-arcade.jpg').resize((400, 400), Image.ANTIALIAS))
canvas.background = img
bg = canvas.create_image(0, 0, anchor=tkinter.NW, image=img)

def runPong():
    os.system('python Pong/Pong.py')

def runSnake():
    os.system('python Snake/snake.py')

def runBubbleTouch():
    os.system('python BubbleTouch/BubbleTouch.py')

# Create GUI
pong = tkinter.Button(root, text = "Pong!", command=lambda: runPong())
pong.place(x=75, y=195)
snake = tkinter.Button(root, text = "Snake!", command=lambda: runSnake())
snake.place(x=177, y=187)
bubbletouch = tkinter.Button(root, text = "Bubble Touch!", command=lambda: runBubbleTouch())
bubbletouch.place(x=263, y=190)

root.mainloop()