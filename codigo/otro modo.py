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
        x=10
        y=10
        z=10
        print(marco.find_all())
        #for x in range(0, 9000):
        while True:
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
        global x
        x=10
        global y
        y=10
        global z
        z=10
        global folly
        folly=10
        global moveY
        moveY=10
        print(marco.find_all())
        
        #print(box)
        while True:
            box2 = marco.bbox(petrol)
            box =marco.bbox(jeep)
         #   print(marco.coords(petrol)[0])
            #mueve el mapa 10 pixeles esto dara la sensacion de moverce hacia atras
            #marco.move(mapaPrincipal,0,10)
            if 2 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                print("watch out")
                marco.delete(jeep)
    
            marco.after(30,marco.move(mapaPrincipal,0,10))

            #print(marco.find_closest(marco.coords(petrol)[0],marco.coords(petrol)[1]))
          

            manchasAceites()

            enemigosApariciones()

            enemigosSiguen()

            enemigoMueve()
            
#COLISONES MAPA
            #primera colision
            if marco.coords(mapaPrincipal)[1] < -26450:
                
                if marco.coords(jeep)[0] > 440:
                    #si se choca va a aparecer una imagen de una explosion
                    for a in range (len(explosiones)):
                        #explosiones
                        display=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=explosiones[a], anchor=NW)
                        if a==6:
                            marco.delete(display)
                            marco.move(jeep,-50,0)
                            #marco.move(mapaPrincipal,0,0)
                        game.update()
                        time.sleep(0.2)
                        marco.delete(display)
                    # si sucede el choque lo que sucede con el break es que el mapa se va a detener
                
                elif marco.coords(jeep)[0] < 204.0:
                    for a in range (len(explosiones)):
                        #explosiones
                        display=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=explosiones[a], anchor=NW)
                        if a==6:
                            marco.delete(display)
                            marco.move(jeep,+50,0)
                            #marco.move(mapaPrincipal,0,0)
                        game.update()
                        time.sleep(0.2)
                        marco.delete(display)
                        
            # colision para la primer curva
            elif marco.coords(mapaPrincipal)[1] >= -26450 and marco.coords(mapaPrincipal)[1] < -25950 :
                if marco.coords(jeep)[0] < valor: 
                    for a in range (len(explosiones)):
                        #explosiones
                        display=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=explosiones[a], anchor=NW)
                        if a==6:
                            marco.delete(display)
                            marco.move(jeep,+50,0)
                            #marco.move(mapaPrincipal,0,0)
                        game.update()
                        time.sleep(0.2)
                        marco.delete(display)
                elif marco.coords(jeep)[0] > valor4:
                    for a in range (len(explosiones)):
                        #explosiones
                        display=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=explosiones[a], anchor=NW)
                        if a==6:
                            marco.delete(display)
                            marco.move(jeep,-50,0)
                            #marco.move(mapaPrincipal,0,0)
                        game.update()
                        time.sleep(0.2)
                        marco.delete(display)
                # como la curva no es una linea recta estuve pensando en un contador que me fuera
                #aumentando la curva para que cambiara el choque de la baranda
                else:
                    valor=valor+3
                    valor4=valor4+3
            # tercera colision linea recta
            elif marco.coords(mapaPrincipal)[1] >= -25950 and marco.coords(mapaPrincipal)[1] < -17840:
                if marco.coords(jeep)[0] > 614: 
                    for a in range (len(explosiones)):
                        #explosiones
                        display=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=explosiones[a], anchor=NW)
                        if a==6:
                            marco.delete(display)
                            marco.move(jeep,-50,0)
                            #marco.move(mapaPrincipal,0,0)
                        game.update()
                        time.sleep(0.2)
                        marco.delete(display)
                elif marco.coords(jeep)[0] < 376.0:
                    for a in range (len(explosiones)):
                        #explosiones
                        display=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=explosiones[a], anchor=NW)
                        if a==6:
                            marco.delete(display)
                            marco.move(jeep,+50,0)
                            #marco.move(mapaPrincipal,0,0)
                        game.update()
                        time.sleep(0.2)
                        marco.delete(display)
            #colision  de segunda curva
                        
            #si las coordenadas del mapa son mayores a ... y menores a ... de esta forma indica la pos para las colisiones
            elif marco.coords(mapaPrincipal)[1] >= -17840 and marco.coords(mapaPrincipal)[1] < -17255:
                if marco.coords(jeep)[0] > valor2: 
                    for a in range (len(explosiones)):
                        #explosiones
                        display=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=explosiones[a], anchor=NW)
                        if a==6:
                            marco.delete(display)
                            marco.move(jeep,-50,0)
                            #marco.move(mapaPrincipal,0,0)
                        game.update()
                        time.sleep(0.2)
                        marco.delete(display)
                elif marco.coords(jeep)[0] < valor3:
                    for a in range (len(explosiones)):
                        #explosiones
                        display=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=explosiones[a], anchor=NW)
                        if a==6:
                            marco.delete(display)
                            marco.move(jeep,+50,0)
                            #marco.move(mapaPrincipal,0,0)
                        game.update()
                        time.sleep(0.2)
                        marco.delete(display)
                else:
                    valor2=valor2-3
                    valor3=valor3-4
                    
                #ultima seccion mapa
            elif marco.coords(mapaPrincipal)[1] >= -17255:
                # colision derecha carro
                if marco.coords(jeep)[0] > 440:
                    for a in range (len(explosiones)):
                        #explosiones
                        display=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=explosiones[a], anchor=NW)
                        if a==6:
                            marco.delete(display)
                            marco.move(jeep,-50,0)
                            #marco.move(mapaPrincipal,0,0)
                        game.update()
                        time.sleep(0.2)
                        marco.delete(display)
                #marco.delete(nombreitem)
                #colision eje izquiers
                elif marco.coords(jeep)[0] < 204.0:
                    for a in range (len(explosiones)):
                        #explosiones
                        display=marco.create_image(marco.coords(jeep)[0]+20,marco.coords(jeep)[1]+30,image=explosiones[a], anchor=NW)
                        if a==6:
                            marco.delete(display)
                            marco.move(jeep,+50,0)
                            #marco.move(mapaPrincipal,0,0)


                        game.update()
                        time.sleep(0.2)
                        marco.delete(display)
#FIN COLISIONES
            print(marco.coords(mapaPrincipal)[1])
            
                        
            marco.move(petrol,0,x)
            marco.move(enemyState,0,y)
            marco.move(enemyState2,0,z)
            marco.move(enemyFoll,0,folly)
            marco.move(enemyMov,0,moveY)
           #print(marco.coords(mapaPrincipal)[1], marco.coords(petrol)[0],marco.coords(petrol)[1], marco.coords(enemyFoll)[0])  
            #time.sleep(0.015)
            # se va cargando el movimiento
            game.update()
            # cada cuantos segundos se va a mover la pantalla
            #time.sleep(0.02)

def enemigoMueve():
     if marco.coords(mapaPrincipal)[1] == -19700:

        marco.move(enemyMov,numMove,moveY-marco.coords(enemyMov)[1])
        
     elif marco.coords(mapaPrincipal)[1]>-19700 and marco.coords(mapaPrincipal)[1] < -19600:
        
        while marco.coords(mapaPrincipal)[1]< -19600:
            #llamo el after para el mapa ya que con esto evito el lag al hacer las siguientes acciones
            marco.after(15,marco.move(mapaPrincipal,0,10))
            
            if marco.coords(enemyMov)[0]>540:
                marco.after(15,marco.move(enemyMov,-10,0))
                
                #game.update()
                #aqui como no se va a cumplir el if de arriba se sobre entiende que nuestro carro esta en una posicion menor al enemigo
                #por eso en este caso la direccion en el eje x se debe de restar
            else:
                marco.after(15,marco.move(enemyMov,10,0))
            game.update()
            
     elif marco.coords(mapaPrincipal)[1] == -14900:
       
        #marco.move(enemyMov,-numMove1,moveY-marco.coords(enemyMov)[1])
         
         marco.coords(enemyMov,numMove1,0)

        
     elif marco.coords(mapaPrincipal)[1]>-19700 and marco.coords(mapaPrincipal)[1] < -19600:
        
        while marco.coords(mapaPrincipal)[1]< -19600:
            #llamo el after para el mapa ya que con esto evito el lag al hacer las siguientes acciones
            marco.after(15,marco.move(mapaPrincipal,0,10))
            
            if marco.coords(enemyMov)[0]>300:
                marco.after(15,marco.move(enemyMov,-10,0))
                
                #game.update()
                #aqui como no se va a cumplir el if de arriba se sobre entiende que nuestro carro esta en una posicion menor al enemigo
                #por eso en este caso la direccion en el eje x se debe de restar
            else:
                marco.after(15,marco.move(enemyMov,10,0))
            game.update()
    
#FUNCIONES PARA LOS MAPAS CON CURVAS 
def enemigosSiguen():
             #enemigo que me sigue            
    if marco.coords(mapaPrincipal)[1] == -25200:

        marco.move(enemyFoll,numFoll,folly-marco.coords(enemyFoll)[1])
        
    elif marco.coords(mapaPrincipal)[1]>-25200 and marco.coords(mapaPrincipal)[1]<-25100:
        valorCoord=0
        while marco.coords(jeep)[0]!= marco.coords(enemyFoll)[0]:
        #llamo el after para el mapa ya que con esto evito el lag al hacer las siguientes acciones
            marco.after(15,marco.move(mapaPrincipal,0,10))
                # para que si el personaje esta en una posicion superior hacia la derecha, este sume 
            if marco.coords(jeep)[0]>marco.coords(enemyFoll)[0]:
                
                valorCoord= marco.coords(jeep)[0]-marco.coords(enemyFoll)[0]
                marco.after(15,marco.move(enemyFoll,valorCoord,0))
                    
                #aqui como no se va a cumplir el if de arriba se sobre entiende que nuestro carro esta en una posicion menor al enemigo
                #por eso en este caso la direccion en el eje x se debe de restar
            else:
                valorCoords= marco.coords(enemyFoll)[0]-marco.coords(jeep)[0]
                marco.after(15,marco.move(enemyFoll,-valorCoord,0))
        
            game.update()
            
    elif marco.coords(mapaPrincipal)[1] == -22000:
        if marco.coords(enemyFoll)[0] > 320:
            marco.move(enemyFoll,-numFoll2,folly-marco.coords(enemyFoll)[1])
        else:
            marco.move(enemyFoll,-numFoll2,folly-marco.coords(enemyFoll)[1])
        
    elif marco.coords(mapaPrincipal)[1]>-22000 and marco.coords(mapaPrincipal)[1]<-21900:
        valorCoord=0
        while marco.coords(jeep)[0]!= marco.coords(enemyFoll)[0]:
        #llamo el after para el mapa ya que con esto evito el lag al hacer las siguientes acciones
            marco.after(15,marco.move(mapaPrincipal,0,10))
            # para que si el personaje esta en una posicion superior hacia la derecha, este sume 
            if marco.coords(jeep)[0]>marco.coords(enemyFoll)[0]:
              
                valorCoord= marco.coords(jeep)[0]-marco.coords(enemyFoll)[0]
                marco.after(15,marco.move(enemyFoll,valorCoord,0))
                
            else:
                valorCoords= marco.coords(enemyFoll)[0]-marco.coords(jeep)[0]
                marco.after(15,marco.move(enemyFoll,-valorCoord,0))
        
            game.update()
    


           
            

def enemigosApariciones():
#CARRO APARICION enemigo 1 
    if marco.coords(mapaPrincipal)[1] == -27190:
        marco.move(enemyState,numEnemy1,y-marco.coords(enemyState)[1])
    #aparicion enemigo 2
                
    elif marco.coords(mapaPrincipal)[1] == -27490:
        marco.move(enemyState2,numEnemy2,z-marco.coords(enemyState)[1])

    #segunda aparicion enemigo1
    elif marco.coords(mapaPrincipal)[1] == -24000:
        if marco.coords(enemyState)[0] > 500:
            marco.move(enemyState,-numEnemy1_2,y-marco.coords(enemyState)[1])
        else:
            marco.move(enemyState,numEnemy1_2,y-marco.coords(enemyState)[1])

    #segunda aparicion enemigo 2

    elif marco.coords(mapaPrincipal)[1] == -24440:
        if marco.coords(enemyState2)[0] > 500:
            marco.move(enemyState2,-numEnemy2_2,z-marco.coords(enemyState)[1])
        else:
            marco.move(enemyState2,numEnemy2_2,z-marco.coords(enemyState)[1])

    #tercera aparicion enemigo 1
    elif marco.coords(mapaPrincipal)[1] == -20340:
        if marco.coords(enemyState)[0] > 500:
            marco.move(enemyState,-numEnemy1_3,y-marco.coords(enemyState)[1])
        else:
            marco.move(enemyState,numEnemy1_3,y-marco.coords(enemyState)[1])

    elif marco.coords(mapaPrincipal)[1] == -16900:
        if marco.coords(enemyState)[0] > 350:
            marco.move(enemyState2,-numEnemy2_2,z-marco.coords(enemyState2)[1])
        else:
            marco.move(enemyState2,numEnemy2_2,z-marco.coords(enemyState2)[1])
       
def manchasAceites():
    if marco.coords(mapaPrincipal)[1] == -28190:
        marco.move(petrol,num1,0)

              #segunda aparicion mancha
    elif marco.coords(mapaPrincipal)[1] == -23500:
        if marco.coords(petrol)[0] > 500:
            marco.move(petrol,-num2,x-marco.coords(petrol)[1])
        else:
            marco.move(petrol,num2,x-marco.coords(petrol)[1])
                
        #tercera aparicion mancha
    elif marco.coords(mapaPrincipal)[1] == -20000:
        if marco.coords(petrol)[0] > 500:
            marco.move(petrol,-num3,x-marco.coords(petrol)[1])
        else:
            marco.move(petrol,num3,x-marco.coords(petrol)[1])

        #cuarta aparicicon mancha de aceite
    elif marco.coords(mapaPrincipal)[1] == -15000:
        if marco.coords(petrol)[0] > 500:
            marco.move(petrol,-num4,x-marco.coords(petrol)[1])
            
        elif marco.coords(petrol)[0]<200:
            marco.move(petrol,num4,x-marco.coords(petrol)[1])


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

#ENEMIGOS
enemigoState= PhotoImage(file="enemy1.png")
enemigoState2= PhotoImage(file="enemy1_2.png")

#ENEMIGOS  QUE SIGUEN
enemigoFollow= PhotoImage(file="enemyFollow.png")
enemigoFollow2= PhotoImage(file="enemyFollow_2.png")

#ENMIGOS QUE SE MUEVEN
enemigoMove= PhotoImage(file="enemyMove.png")
enemigoMove2= PhotoImage(file="enemyMove_2.png")

#explosiones animacion
exp1 = PhotoImage(file="explosion1.png")
exp2 = PhotoImage(file="explosion2.png")
exp3 = PhotoImage(file="explosion3.png")
exp4 = PhotoImage(file="explosion4.png")
exp5 = PhotoImage(file="explosion5.png")
exp6 = PhotoImage(file="explosion6.png")
exp7 = PhotoImage(file="explosion7.png")

explosiones=[exp1,exp2,exp3,exp4,exp5,exp6,exp7]


    
  
# funcion para iniciar el juego el mapa 1
def empezar():
    game.geometry("820x580")
    # de iconify para maximixar la ventana cuando ya presione el boton
    game.deiconify()
    marco.pack()
    raiz.withdraw()
    # nueva ventana
    game.resizable(width=False, height=False)

    #RANDOM PARA EL ACEITE
    global num1
    num1=random.randrange(230,410,3)
    # le doy un rango bajo ya que no quiero que se me aumente mas sino que me disminuya para que quede dentro de los limites
    global num2
    num2=random.randrange(150,230,3)
    global num3
    num3=random.randrange(10,50,3)
    global num4
    num4=random.randrange(100,300,3)
    global num5
    num5=random.randrange(50,150,10)

    global mapaPrincipal 
    mapaPrincipal = marco.create_image(-2,-28200, image=mapa, anchor=NW)
    global petrol
    petrol = marco.create_image(0, 0, image=aceite, anchor=NW)   
    # tenemos que darle una variable para los eventos de las teclas
    global jeep
    jeep = marco.create_image(365, 480, image=carroPrincipal, anchor=NW)
    miniRoad = marco.create_image(0, 0, image=miniCarretera, anchor=NW)

    #IMAGENES PARA LOS ENEMIGOS 
    global enemyState
    enemyState= marco.create_image(-35, 0, image=enemigoState, anchor=NW)
    #NUMEROS RANDOMS PARA LOS ENEMIGOS
    #aparicion1
    global numEnemy1
    numEnemy1=random.randrange(360,480,10)
    global numEnemy1_2
    numEnemy1_2=random.randrange(100,200,10)
    global numEnemy1_3
    numEnemy1_3=random.randrange(100,180,10)
    
    global enemyState2
    enemyState2 = marco.create_image(-35, 0, image=enemigoState2, anchor=NW)
    #NUMEROS RANDOMS PARA LOS ENEMIGOS
    #aparicion1
    global numEnemy2
    numEnemy2=random.randrange(360,440,10)
    global numEnemy2_2
    numEnemy2_2=random.randrange(100,300,10)

    #ENMIGOS QUE ME SIGUEN
    global enemyFoll
    enemyFoll= marco.create_image(-35, 0, image=enemigoFollow, anchor=NW)
    #aparicion1
    global numFoll
    numFoll=random.randrange(480,580,10)
    
    global enemyFoll2
    enemyFoll2= marco.create_image(-35, 0, image=enemigoFollow2, anchor=NW)
    #aparicion1
    global numFoll2
    numFoll2=random.randrange(50,150,10)

    #ENEMIGOS QUE SE MUEVEN
    global enemyMov
    enemyMov= marco.create_image(-35, 0, image=enemigoMove, anchor=NW)
    #aparicion 1
    global numMove
    numMove=random.randrange(540,680,10)
    global numMove1
    numMove1=random.randrange(360,480,10)
    
    global enemyMov2
    enemyMov2= marco.create_image(-35, 0, image=enemigoMove2, anchor=NW)
    #aparicion1
    global numMove2
    numMove2=random.randrange(220,410,11)


    

    
    #miniCuper = marco.create_image(0, 525, image=carroMini, anchor=NW) 
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
    jeep = marco.create_image(330, 480, image=carroPrincipal, anchor=NW)
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

