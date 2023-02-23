import sys
import tkinter as tk
import tkinter.font as tkFont
import time
import cv2
import numpy as np
import keyboard

w, h = 360, 240
fbRange = [6200, 6800]
pid = [0.4, 0.4, 0] # proporcion, integral, derivada
pError = 0

class App:
    def __init__(self, root):
        #setting title
        root.title("Dagger Demo Mision ")
        #setting window size
        width=558
        height=319
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_471=tk.Label(root)
        GLabel_471["bg"] = "#5db6fb"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_471["font"] = ft
        GLabel_471["fg"] = "#333333"
        GLabel_471["justify"] = "center"
        GLabel_471["text"] = "Dagger 1"
        GLabel_471["relief"] = "flat"
        GLabel_471.place(x=0,y=0,width=557,height=92)

        GButton_787=tk.Button(root)
        GButton_787["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_787["font"] = ft
        GButton_787["fg"] = "#000000"
        GButton_787["justify"] = "center"
        GButton_787["text"] = "Ruta Programada"
        GButton_787["relief"] = "raised"
        GButton_787.place(x=210,y=170,width=129,height=43)
        GButton_787["command"] = self.GButton_787_command

        # GButton_417=tk.Button(root)
        # GButton_417["bg"] = "#f0f0f0"
        # ft = tkFont.Font(family='Times',size=10)
        # GButton_417["font"] = ft
        # GButton_417["fg"] = "#000000"
        # GButton_417["justify"] = "center"
        # GButton_417["text"] = "Seguidor de Rostros"
        # GButton_417["relief"] = "raised"
        # GButton_417.place(x=330,y=170,width=129,height=45)
        # GButton_417["command"] = self.GButton_417_command

        GButton_251 = tk.Button(root)
        GButton_251["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_251["font"] = ft
        GButton_251["fg"] = "#000000"
        GButton_251["justify"] = "center"
        GButton_251["text"] = "Salir"
        GButton_251.place(x=240, y=260, width=70, height=25)
        GButton_251["command"] = self.GButton_251_command

    def GButton_787_command(self): #Ruta
        print("Ruta")
        exec(open("mission.py").read())

    # def GButton_417_command(self):# Seguidor de rostros
    #     print("Seguidor")
    #     exec(open("FaceTracking.py").read())

    def GButton_251_command(self):
        print("Salir")

        sys.exit()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()