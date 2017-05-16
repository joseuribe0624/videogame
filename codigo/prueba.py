from tkinter import *
from tkinter import font
from tkinter import *
from tkinter import ttk
def moveCarroPrincipal(tecla):
    if tecla.char == "a":
        print("izquierda\n")
        marco.move(jeep,-3,0)
        marco.after(1,marco.move(jeep,-3,0))
    elif tecla.char=="d":
        print("derecha\n")
        marco.move(jeep,3,0)
        marco.after(1,marco.move(jeep,3,0))

game=Tk()
game.geometry("820x580")
game.resizable(width=False,height=False)
marco=Canvas(game,width=820,height=580,bg="light blue")
marco.pack()
mapa=PhotoImage(file="mundo1.png")
marco.create_image(-2, -2, image = mapa, anchor = NW)
#se crea la imagen dentro del canvas como ya hay dos imagene lo que hace es sobre poner una encima de la otra
carroPrincipal=PhotoImage(file="yipeto(128).png")
#tenemos que darle una variable para los eventos de las teclas
jeep=marco.create_image(330, 480, image = carroPrincipal, anchor = NW)
#bind para asignar que move es con una tecla
marco.bind("<KeyPress>",moveCarroPrincipal)
marco.focus_set()
raiz.withdraw()
game.mainloop()
