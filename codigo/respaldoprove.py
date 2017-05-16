#height altura
#widht=ancho
#menu
from tkinter import *
from tkinter import font
from tkinter import *
from tkinter import ttk
import time
game = Tk()
raiz = Toplevel(game)
# ventana hija para el segundo menu

# define el tamaño de la pantalla
raiz.geometry("720x480")
# se hace esto para que la pantalla no sea reducida o aumentada y asi no dañar el tamaño de la imagen
raiz.resizable(width=False, height=False)
# pantallas


# titulo
# IMAGENES
raiz.title("MOUNTAIN FIGHTERS THE GAME")
menuImagen = PhotoImage(file="menuGame.png")
menuJuego = ttk.Label(raiz, image=menuImagen)

tutoImagen = PhotoImage(file="howTo.png")
tuto = ttk.Label(raiz, image=tutoImagen)

menu_segundo = PhotoImage(file="segundoMenu.png")
menu2 = ttk.Label(raiz, image=menu_segundo)
menu2.place_forget()


# boton que despliega tutorial na nueva pantalla
def abrirTutorial():
    # se le da las dimensiones
    raiz.geometry('720x480')
    raiz.resizable(width=False, height=False)
    # place forget es para olvidar los botenes labels etc que tenia antes para que no aparezcan
    menuJuego.place_forget()
    tuto.place(x=-2, y=-2)
    tutorial.place_forget()
    volver.place(x=10, y=450)
    play.place_forget()


# funcion para el boton devolver genera de nuevo la pantalla de inicio
def volver():
    raiz.geometry('720x480')
    raiz.resizable(width=False, height=False)
    tuto.place_forget()
    tutorial.place(x=320, y=400)
    menuJuego.place(x=-2, y=-2)
    volver.place(x=320, y=450)
    play.place(x=320, y=350)


# funcion para mover la pantalla de juego

     
    
# funcion para los movimientos del carro
def moveCarroPrincipal(tecla):
    # si se preciona la tecla a
    if tecla.char == "a":
        # el jeep se mueve a la izquierda -3 pixeles en el eje x
        marco.move(jeep, -3, 0)
        # cada un milisegundo
        marco.after(1, marco.move(jeep, -3, 0))
    elif tecla.char == "d":
        # se mueve a la derecha si se presiona la tecla d
        marco.move(jeep, 3, 0)
        marco.after(1, marco.move(jeep, 3, 0))
    # condicional para que cuando se presiona la tecla b el carro arranque
    elif tecla.char=="b":
        # en un rango de 0 a 9000 serian noventa segundos es lo que dura la animacion del carro en movimiento
        #ya que esto es el tiempo limite que posee el carro para llegar a la meta
        for x in range(0, 9000):
            # esto dice hacia donde se mueve la imagen en este caso se va yendo hacia atras
            marco.move(mapaPrincipal,0,5)
            # se va cargando el movimiento
            game.update()
            # cada cuantos segundos se va a mover la pantalla
            time.sleep(0.02)
            carreterita.move(miniCuper,0,-1)
            game.update()
            time.sleep(0.10)
  
            
  
       

# condicionales para mover el carro en sentido del eje y adelante atras

# nueva ventana

game.resizable(width=False, height=False)
# canvas
marco = Canvas(game, width=820, height=580, bg="light blue",highlightthickness=0)
marco.place_forget()
#canvas para el minicuper pequeño y para el minimapa

mapa = PhotoImage(file="mundo2.png")
mapaPrincipal = marco.create_image(20, 0, image=mapa, anchor=NW)
# se crea la imagen dentro del canvas como ya hay dos imagene lo que hace es sobre poner una encima de la otra
carroPrincipal = PhotoImage(file="yipeto(128).png")
# tenemos que darle una variable para los eventos de las teclas
jeep = marco.create_image(330, 480, image=carroPrincipal, anchor=NW)

carreterita = Canvas(game, width=67, height=580, bg="dark blue",highlightthickness=0)
carreterita.place_forget()
#esto tiene que ir en el otro canvas para que no haya conflicto en el time.sleep
miniCarretera = PhotoImage(file="carreteraPequeña.png ")
miniRoad = carreterita.create_image(0, 0, image=miniCarretera, anchor=NW)
carroMini = PhotoImage(file="yipeto(64).png ")
miniCuper = carreterita.create_image(0, 525, image=carroMini, anchor=NW)

# bind para asignar que move es con una tecla

marco.bind("<KeyPress>", moveCarroPrincipal)
marco.focus_set()
carreterita.bind("<KeyPress>", moveCarroPrincipal)
carreterita.focus_set()




# funcion para iniciar el juego
def empezar():
    game.geometry("820x580")
    # de iconify para maximixar la ventana cuando ya presione el boton
    game.deiconify()
    marco.place(x=48,y=0)
    carreterita.place(x=-2,y=-2)
    raiz.withdraw()
    game.mainloop()


# BOTON PARA INICIAR LA PANTALLA DE JUEGO
player = StringVar()
# inicia el segundo menu para ya empezar el juego
def iniciar():
    global player
    textoJugador = ttk.Entry(raiz, textvariable=player, width=30)
    menu2.place(x=-2, y=-2)
    iniciarGame.place(x=320, y=400)
    nivelNormal.place(x=320, y=250)
    nivelExtrema.place(x=320, y=300)
    textoJugador.place(x=260, y=110)
    play.place_forget()
    volver.place_forget()

    # cierro la ventana pasada la del menu para abrir la nueva


play = ttk.Button(raiz, text="JUGAR", command=iniciar)
# boton para abrir el tutorial
tutorial = ttk.Button(raiz, text="TUTORIAL", command=abrirTutorial)
volver = ttk.Button(raiz, text="REGRESAR", command=volver)

# widgets
menuJuego.place(x=-2, y=-2)
tuto.place_forget()
volver.place(x=320, y=450)
tutorial.place(x=320, y=400)
play.place(x=320, y=350)

# BOTONES PARA LA FUNCION INICIAR

# estos botones los tengo que definir luego
nivelNormal = ttk.Button(raiz, text="NORMAL")  # tener cuidado con estos botones y no olvidarlos son para los niveles
nivelExtrema = ttk.Button(raiz, text="EXTREMA")
# boton para iniciar la pantalla de juego
iniciarGame = ttk.Button(raiz, text="INICIAR", command=empezar)

iniciarGame.place_forget()
nivelNormal.place_forget()
nivelExtrema.place_forget()
# minimixa la ventana
game.iconify()
raiz.mainloop()
# salir del juego
# nueva partida
# tutorial
