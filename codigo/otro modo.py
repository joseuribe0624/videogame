#height altura
#widht=ancho
#menu
#se demora 8,06 segundos a la velocidad que esta en acabarse la pantalla
from tkinter import *
from tkinter import font
from tkinter import *
from tkinter import ttk
import random
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
menuImagen = PhotoImage(file="menu-3.png")
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
    #mapa2.place_forget()


# funcion para el boton devolver genera de nuevo la pantalla de inicio
def volver():
    raiz.geometry('720x480')
    raiz.resizable(width=False, height=False)
    tuto.place_forget()
    tutorial.place(x=320, y=400)
    menuJuego.place(x=-2, y=-2)
    volver.place(x=320, y=450)
    play.place(x=320, y=350)
    #mapa2.place_forget()

def moveCarroSegundoMap(key):
    global posicionMap
    global posCarro
  
    valor=204
    rightCar=3
    # si se preciona la tecla a
    if key.char == "a":
        # el jeep se mueve a la izquierda -3 pixeles en el eje x
        marco.move(jeep, -3, 0)
        # cada un milisegundo
        marco.after(1, marco.move(jeep, -3, 0))
    elif key.char == "d":
        # se mueve a la derecha si se presiona la tecla d
        marco.move(jeep, 3, 0)
        marco.after(1, marco.move(jeep, 3, 0))
    # condicional para que cuando se presiona la tecla b el carro arranque
    elif key.char=="b":
        # en un rango de 0 a 9000 serian noventa segundos es lo que dura la animacion del carro en movimiento
        #ya que esto es el tiempo limite que posee el carro para llegar a la meta
        valor=208
        valor2=614
        valor3=376
        valor4=444
        #for x in range(0, 9000):
        while True:
            #if marco.coords(mapaPrincipal)[1] < -26450:
             #   num1=random.randrange(210,438,20)
              #  petrol = marco.create_image(num1, 0, image=tinta, anchor=NW)
            # para mover la mancha de aceite con el mapa
            #marco.move(petrol,0,10)
            #mueve el mapa 10 pixeles esto dara la sensacion de moverce hacia atras
            marco.move(segundoMapa,0,10)
            #colisiones del mapa2
            #linea recta
            if marco.coords(segundoMapa)[1] < -26450:
                # colision derecha carro
                if marco.coords(jeep)[0] > 440:
                    #si se choca va a aparecer una imagen de una explosion
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    # si sucede el choque lo que sucede con el break es que el mapa se va a detener
                    marco.delete(jeep)
                    break
                #marco.delete(nombreitem)
                #colision eje izquiers
                elif marco.coords(jeep)[0] < 204.0:
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    marco.delete(jeep)
                    break
            # se va cargando el movimiento
            game.update()
            # cada cuantos segundos se va a mover la pantalla
            time.sleep(0.02)

            
marco = Canvas(game, width=820, height=29000, bg="light blue")
marco.pack_forget()

# funcion para los movimientos del carro del mapa 1
def moveCarroPrincipal(tecla):
    global posicionMap
    global posCarro
    #if marco.coords(mapaPrincipal)[1] < -26450:
     #   marco.move(petrol,num1,0)   
    #elif marco.coords(mapaPrincipal)[1] >= -26450 and marco.coords(mapaPrincipal)[1] < -25950:
    #    marco.move(petrol,num2,-3000)
    valor=204
    rightCar=3
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
        valor=208
        valor2=614
        valor3=376
        valor4=444
        #for x in range(0, 9000):
        global petrol    
        #marco.after(500,empezar)
        x=10
        dy=0
    # diferencia en los ejes
        dx=0
        while True:
            #mueve el mapa 10 pixeles esto dara la sensacion de moverce hacia atras
            marco.move(mapaPrincipal,0,10)
            #print(marco.bbox(jeep))
            #print(marco.bbox(petrol))
            #colisiones del mapa
            #linea recta
            #box = marco.bbox(petrol)
            #print(marco.find_overlapping(box))
            
                
            if marco.coords(mapaPrincipal)[1] == -28190 :
                print("hey")
                y=num1
                marco.move(petrol,num1,0)
                
            elif dy<=10 and dx<=10 :
                print("be careful")
                #marco.move(jeep,+3,0)
                marco.delete(jeep)
                

            elif marco.coords(mapaPrincipal)[1] == -26450:
                if marco.coords(mapaPrincipal)[0] > 500:
                    marco.move(petrol,-num2,x-1750)
                else:
                    marco.move(petrol,num2,x-1750)
                
    
            elif dy<=20 and dx<=20:
                print("be careful")
                marco.move(jeep,x+3,0)

            elif marco.coords(mapaPrincipal)[1] == -18000:
                if marco.coords(mapaPrincipal)[0] > 500:
                    marco.move(petrol,-num3,x-marco.coords(petrol)[1])
                else:
                    marco.move(petrol,num3,x-marco.coords(petrol)[1])

                
            #colision linea recta    
            elif marco.coords(mapaPrincipal)[1] < -26450:
                
                if marco.coords(jeep)[0] > 440:
                    #si se choca va a aparecer una imagen de una explosion
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    # si sucede el choque lo que sucede con el break es que el mapa se va a detener
                    marco.delete(jeep)
                    break
                
                elif marco.coords(jeep)[0] < 204.0:
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    marco.delete(jeep)
                    break
            # colision para la primer curva
            elif marco.coords(mapaPrincipal)[1] >= -26450 and marco.coords(mapaPrincipal)[1] < -25950 :
                if marco.coords(jeep)[0] < valor: 
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    marco.delete(jeep)
                    break
                elif marco.coords(jeep)[0]>valor4:
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    marco.delete(jeep)
                    break
                # como la curva no es una linea recta estuve pensando en un contador que me fuera
                #aumentando la curva para que cambiara el choque de la baranda
                else:
                    valor=valor+3
                    valor4=valor4+3
            # tercera colision linea recta
            elif marco.coords(mapaPrincipal)[1] >= -25950 and marco.coords(mapaPrincipal)[1] < -17840:
                #if marco.coords(mapaPrincipal)[1] == -19600:
                    #x=10
                    #marco.move(petrol,num3,x-6870)
                if marco.coords(jeep)[0] > 614: 
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    marco.delete(jeep)
                    break
                elif marco.coords(jeep)[0] < 376.0:
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    marco.delete(jeep)
                    break
                
            #colision  de segunda curva
            #si las coordenadas del mapa son mayores a ... y menores a ... de esta forma indica la pos para las colisiones
            elif marco.coords(mapaPrincipal)[1] >= -17840 and marco.coords(mapaPrincipal)[1] < -17255:
                if marco.coords(jeep)[0] > valor2: 
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    marco.delete(jeep)
                    break
                elif marco.coords(jeep)[0] < valor3:
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    marco.delete(jeep)
                    break
                else:
                    valor2=valor2-3
                    valor3=valor3-4
                #ultima seccion mapa
            elif marco.coords(mapaPrincipal)[1] >= -17255:
                # colision derecha carro
                if marco.coords(jeep)[0] > 440:
                    #si se choca va a aparecer una imagen de una explosion
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    # si sucede el choque lo que sucede con el break es que el mapa se va a detener
                    marco.delete(jeep)
                    break

                #colision eje izquiers
                elif marco.coords(jeep)[0] < 204.0:
                    ink=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=tinta, anchor=NW)
                    marco.delete(jeep)
                    break

                
            dy=marco.coords(petrol)[1]-marco.coords(jeep)[1]
            
            if marco.coords(petrol)[0] < marco.coords(jeep)[0]:
                dx= marco.coords(jeep)[0]-marco.coords(petrol)[0]
                
            elif marco.coords(petrol)[0] > marco.coords(jeep)[0]:
                dx= marco.coords(petrol)[0]-marco.coords(jeep)[0]

                
            marco.move(petrol,0,x)
            print(marco.coords(jeep)[0],marco.coords(mapaPrincipal)[1],marco.coords(petrol)[0],marco.coords(petrol),num2,num1)  
            
            # se va cargando el movimiento
            game.update()
            # cada cuantos segundos se va a mover la pantalla
            time.sleep(0.015)
       
           
# condicionales para mover el carro en sentido del eje y adelante atras


#imagen del mapa1 
mapa = PhotoImage(file="mapWorld.png")
#se crea la imagen dentro del canvas como ya hay dos imagene lo que hace es sobre poner una encima de la otra
carroPrincipal = PhotoImage(file="yipeto(128).png")
miniCarretera = PhotoImage(file="carreteraPequeña.png ")
carroMini = PhotoImage(file="yipeto(64).png ")
tinta = PhotoImage(file="Ink.png")
aceite=PhotoImage(file="aceite.png")
#mapa para el mundo 2 
mapaDesierto = PhotoImage(file="mapWorld2.png ")


#while True:
 #   marco.move(ink,ejex,ejey)
  #  pos=marco.coords(ink)
   # print(pos)
    #if pos[1]>700:
     #   nume=random.randrange(450,1000,10)
      #  ink = marco.create_image(0, 0, image=tinta, anchor=NW)
       # marco.move(ink,nume,0)
       # ejex=0
       # ejey=10

  
# funcion para iniciar el juego el mapa 1
def empezar():
    game.geometry("820x580")
    # de iconify para maximixar la ventana cuando ya presione el boton
    game.deiconify()
    marco.pack()
    raiz.withdraw()
    # nueva ventana
    game.resizable(width=False, height=False)

    global num1
    num1=random.randrange(220,410,3)
    # le doy un rango bajo ya que no quiero que se me aumente mas sino que me disminuya para que quede dentro de los limites
    global num2
    num2=random.randrange(50,100,3)
    global num3
    num3=random.randrange(50,100,3)          
    #global num4 puedo usarlo para los carros
    #num4=random.randrange(210,438,10)
    # canvas
    global mapaPrincipal 
    mapaPrincipal = marco.create_image(-2,-28200, image=mapa, anchor=NW)
    global petrol
    petrol = marco.create_image(0, 0, image=aceite, anchor=NW)   
    # tenemos que darle una variable para los eventos de las teclas
    global jeep
    jeep = marco.create_image(355, 480, image=carroPrincipal, anchor=NW)
    miniRoad = marco.create_image(0, 0, image=miniCarretera, anchor=NW)
    miniCuper = marco.create_image(0, 525, image=carroMini, anchor=NW) 
    #aceite = PhotoImage(file="aceite.png")
    #bind para asignar que move es con una tecla
    marco.bind("<KeyPress>", moveCarroPrincipal)
    marco.focus_set()
    game.mainloop()




def nivel2():
    game.geometry("820x580")
    # de iconify para maximixar la ventana cuando ya presione el boton
    game.deiconify()
    marco.pack()
    raiz.withdraw()
    # nueva ventana
    game.resizable(width=False, height=False)
    # canvas
    global segundoMapa
    segundoMapa = marco.create_image(-2,-28200, image=mapaDesierto, anchor=NW)
    # tenemos que darle una variable para los eventos de las teclas
    global jeep
    jeep = marco.create_image(355, 480, image=carroPrincipal, anchor=NW)
    miniRoad = marco.create_image(0, 0, image=miniCarretera, anchor=NW)
    miniCuper = marco.create_image(0, 525, image=carroMini, anchor=NW)
    #teclas y colisiones del segundo mapa 
    marco.bind("<KeyPress>", moveCarroSegundoMap)
    marco.focus_set()
    game.mainloop()



# BOTON PARA INICIAR LA PANTALLA DE JUEGO


player = StringVar()


# inicia el segundo menu para ya empezar el juego
def iniciar():
    global player
    textoJugador = ttk.Entry(raiz, textvariable=player, width=30)
    menu2.place(x=-2, y=-2)
    iniciarGame.place(x=320, y=250)
    #mapa3
    nivelNormal.place(x=320, y=350)
    #mapa4
    nivelExtrema.place(x=320, y=400)
    #mapa5
    mapa5.place(x=320,y=450)
    textoJugador.place(x=260, y=110)
    #mapa2
    mapa2.place(x=320,y=300)
    play.place_forget()
    volver.place_forget()

    # cierro la ventana pasada la del menu para abrir la nueva

#boton=photoImage(file="")
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
nivelNormal = ttk.Button(raiz, text="MAPA3")  # tener cuidado con estos botones y no olvidarlos son para los niveles
nivelExtrema = ttk.Button(raiz, text="MAPA4")

# boton para iniciar la pantalla de juego
iniciarGame = ttk.Button(raiz, text="MAPA1", command=empezar)

mapa2=ttk.Button(raiz, text="MAPA2",command=nivel2)
mapa5=ttk.Button(raiz,text="MAPA5")

mapa2.place_forget()
mapa5.place_forget()
iniciarGame.place_forget()
nivelNormal.place_forget()
nivelExtrema.place_forget()
# minimixa la ventana
game.iconify()
raiz.mainloop()
# salir del juego
# nueva partida
# tutorial
