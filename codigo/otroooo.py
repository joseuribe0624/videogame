#height altura
#widht=ancho
#menu
#se demora 8,06 segundos a la velocidad que esta en acabarse la pantalla
from tkinter import *
import tkinter
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
marco = Canvas(game, width=820, height=29000, bg="light blue")
marco.pack_forget()
def moveCarroTercerMap(key):
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
            # en un rango de 0 a 9000 serian noventa segundos es lo que dura la animacion del carro en movimiento
        #ya que esto es el tiempo limite que posee el carro para llegar a la meta
        valor=249
        valor2=628
        valor3=421
        valor4=459
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
        #print(marco.find_all())
        
        #print(box)
        while True:
            box2 = marco.bbox(petrol)
            box =marco.bbox(jeep)
            box4 = marco.bbox(enemyState)

            box5 = marco.bbox(enemyState2)

            box6 = marco.bbox(enemyFoll)

            box7 = marco.bbox(enemyFoll2)

            box8 = marco.bbox(enemyMov)
            
            box9 = marco.bbox(enemyMov2)

          
            #MANCHA ACEITE
            if 2 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                # para saber que animacion debe realizar si la de desviarse a la izquierda o derecha
                if marco.coords(jeep)> marco.coords(petrol):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()

            #ENEMIGO STATE
            elif 4 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyState):
                    marco.delete(box2)
                    animacionRight()
                else:
                  
                    marco.delete(box2)
                    animacionLeft()

                    
            #ENEMGIGO STATE2
            elif 5 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyState2):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()

            #ENEMIGO FOLL
            elif 6 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyFoll):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()


            #ENEMIGO FOLL2
            elif 7 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyFoll2):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()


            #ENIMGO MOV
            elif 8 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyMov):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()
                    
            #ENEMIGO MOV2
            elif 9 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyMov2):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()
    
            marco.after(15,marco.move(mapaPrincipal,0,10))

            #print(marco.find_closest(marco.coords(petrol)[0],marco.coords(petrol)[1]))
          
            manchasAceites2()

            enemigosApariciones2()

            enemigosSiguen2()

            enemigoMueve2()
            
#COLISONES MAPA
            #primera colision
            if marco.coords(mapaPrincipal)[1] < 1000 :
                
                if marco.coords(jeep)[0] > 509:
                    
                    animacionMapaRight()
            
                elif marco.coords(jeep)[0] < 275.0:
                    animacionMapaLeft()
                 
                
#FIN COLISIONES
            #print(marco.coords(mapaPrincipal)[1],marco.coords(jeep)[0])
            
                        
            marco.move(petrol,0,x)
            marco.move(enemyState,0,y)
            marco.move(enemyState2,0,z)
            marco.move(enemyFoll,0,folly)
            marco.move(enemyMov,0,moveY)
            print(marco.coords(mapaPrincipal)[1], marco.coords(petrol)[0],marco.coords(petrol)[1], marco.coords(enemyFoll)[0])  
            game.update()
def moveCarroSegundoMap(keys):
    global posicionMap
    global posCarro
    valor=204
    rightCar=3
    # si se preciona la tecla a
    if keys.char == "a":
        # el jeep se mueve a la izquierda -3 pixeles en el eje x
        marco.move(jeep, -3, 0)
        # cada un milisegundo
        marco.after(1, marco.move(jeep, -3, 0))
    elif keys.char == "d":
        # se mueve a la derecha si se presiona la tecla d
        marco.move(jeep, 3, 0)
        marco.after(1, marco.move(jeep, 3, 0))
    # condicional para que cuando se presiona la tecla b el carro arranque
    elif keys.char=="b":
        # en un rango de 0 a 9000 serian noventa segundos es lo que dura la animacion del carro en movimiento
            # en un rango de 0 a 9000 serian noventa segundos es lo que dura la animacion del carro en movimiento
        #ya que esto es el tiempo limite que posee el carro para llegar a la meta
        valor=249
        valor2=628
        valor3=421
        valor4=459
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
        #print(marco.find_all())
        
        #print(box)
        while True:
            box2 = marco.bbox(petrol)
            box =marco.bbox(jeep)
            box4 = marco.bbox(enemyState)

            box5 = marco.bbox(enemyState2)

            box6 = marco.bbox(enemyFoll)

            box7 = marco.bbox(enemyFoll2)

            box8 = marco.bbox(enemyMov)
            
            box9 = marco.bbox(enemyMov2)

          
            #MANCHA ACEITE
            if 2 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                # para saber que animacion debe realizar si la de desviarse a la izquierda o derecha
                if marco.coords(jeep)> marco.coords(petrol):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()

            #ENEMIGO STATE
            elif 4 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyState):
                    marco.delete(box2)
                    animacionRight()
                else:
                  
                    marco.delete(box2)
                    animacionLeft()

                    
            #ENEMGIGO STATE2
            elif 5 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyState2):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()

            #ENEMIGO FOLL
            elif 6 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyFoll):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()


            #ENEMIGO FOLL2
            elif 7 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyFoll2):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()


            #ENIMGO MOV
            elif 8 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyMov):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()
                    
            #ENEMIGO MOV2
            elif 9 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
                if marco.coords(jeep)> marco.coords(enemyMov2):
                    marco.delete(box2)
                    animacionRight()
                else:
                    #marco.after(15,marco.move(jeep,50,0))
                    marco.delete(box2)
                    animacionLeft()
    
            marco.after(15,marco.move(mapaPrincipal,0,10))

            #print(marco.find_closest(marco.coords(petrol)[0],marco.coords(petrol)[1]))
          
            manchasAceites2()

            enemigosApariciones2()

            enemigosSiguen2()

            enemigoMueve2()
            
#COLISONES MAPA
            #primera colision
            if marco.coords(mapaPrincipal)[1] < 1000 :
                
                if marco.coords(jeep)[0] > 509:
                    
                    animacionMapaRight()
            
                elif marco.coords(jeep)[0] < 275.0:
                    animacionMapaLeft()
                 
                
#FIN COLISIONES
            #print(marco.coords(mapaPrincipal)[1],marco.coords(jeep)[0])
            
                        
            marco.move(petrol,0,x)
            marco.move(enemyState,0,y)
            marco.move(enemyState2,0,z)
            marco.move(enemyFoll,0,folly)
            marco.move(enemyMov,0,moveY)
           #print(marco.coords(mapaPrincipal)[1], marco.coords(petrol)[0],marco.coords(petrol)[1], marco.coords(enemyFoll)[0])  
            game.update()
         

            


# funcion para los movimientos del carro del mapa 1
def moveMapaP(nudes):
    valor=249
    valor2=628
    valor3=421
    valor4=459
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
    #print(marco.find_all())
    
    #print(box)

        
    llamadas()
  
    #MANCHA ACEITE
    

    marco.after(20,marco.move(mapaPrincipal,0,10))
        
    marco.after(20,marco.move(petrol,0,10))
    marco.after(20,marco.move(enemyState,0,10))
    marco.after(20,marco.move(enemyState2,0,10))
    marco.after(20,marco.move(enemyFoll,0,10))
    marco.after(20,marco.move(enemyMov,0,10))

    marco.after(20, lambda: moveMapaP("hola"))
   #print(marco.coords(mapaPrincipal)[1], marco.coords(petrol)[0],marco.coords(petrol)[1], marco.coords(enemyFoll)[0])  

        
        
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
        marco.after(1, lambda: marco.move(jeep, -3, 0))
        #time.sleep(0.1)
    elif tecla.char == "d":
        # se mueve a la derecha si se presiona la tecla d
        marco.move(jeep, 3, 0)
        marco.after(1, marco.move(jeep, 3, 0))
        #time.sleep(0.1)
    # condicional para que cuando se presiona la tecla b el carro arranque

def llamadas():
    global box2,box,box4,box5,box6,box7,box8,box9
    box2 = marco.bbox(petrol)
    box =marco.bbox(jeep)
    box4 = marco.bbox(enemyState)

    box5 = marco.bbox(enemyState2)

    box6 = marco.bbox(enemyFoll)

    box7 = marco.bbox(enemyFoll2)

    box8 = marco.bbox(enemyMov)
    
    box9 = marco.bbox(enemyMov2)
    manchasAceites()

    enemigosApariciones()

    enemigosSiguen()

    enemigoMueve()
    colisiones()
    choquesMap()

    marco.after(10,llamadas)
    
def choquesMap():
    if marco.coords(mapaPrincipal)[1] < -26450:
        
        if marco.coords(jeep)[0] > 455:
            
            animacionMapaRight()
    
        
        elif marco.coords(jeep)[0] < 245.0:
            animacionMapaLeft()
         
        
    # colision para la primer curva
    elif marco.coords(mapaPrincipal)[1] >= -26450 and marco.coords(mapaPrincipal)[1] < -25950 :
        
        if marco.coords(jeep)[0] < valor: 
            
            animacionMapaLeft()  
        elif marco.coords(jeep)[0] > valor4:
            animacionMapaRight()
            
                
        # como la curva no es una linea recta estuve pensando en un contador que me fuera
        #aumentando la curva para que cambiara el choque de la baranda
        else:
            valor=valor+3
            valor4=valor4+3
    # tercera colision linea recta
    elif marco.coords(mapaPrincipal)[1] >= -25950 and marco.coords(mapaPrincipal)[1] < -17840:
        if marco.coords(jeep)[0] > 624: 
            animacionMapaRight()
            
        elif marco.coords(jeep)[0] < 415.0:
            
            animacionMapaLeft()
                
    #colision  de segunda curva
                
    #si las coordenadas del mapa son mayores a ... y menores a ... de esta forma indica la pos para las colisiones
    elif marco.coords(mapaPrincipal)[1] >= -17840 and marco.coords(mapaPrincipal)[1] < -17255:
        if marco.coords(jeep)[0] > valor2: 
            animacionMapaRight()
                
        elif marco.coords(jeep)[0] < valor3:
            animacionMapaLeft()
                
        else:
            valor2=valor2-3
            valor3=valor3-4
            
        #ultima seccion mapa
    elif marco.coords(mapaPrincipal)[1] >= -17255:
        # colision derecha carro
        
        if marco.coords(jeep)[0] > 440:
            animacionMapaRight()
                

        elif marco.coords(jeep)[0] < 204.0:
            animacionMapaLeft()
def colisiones():
    if 2 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
        # para saber que animacion debe realizar si la de desviarse a la izquierda o derecha
        if marco.coords(jeep)> marco.coords(petrol):
            marco.delete(box2)
            animacionRight()
        else:
            #marco.after(15,marco.move(jeep,50,0))
            marco.delete(box2)
            animacionLeft()

    #ENEMIGO STATE
    elif 4 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
        if marco.coords(jeep)> marco.coords(enemyState):
            marco.delete(box2)
            animacionRight()
        else:
          
            marco.delete(box2)
            animacionLeft()

            
    #ENEMGIGO STATE2
    elif 5 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
        if marco.coords(jeep)> marco.coords(enemyState2):
            marco.delete(box2)
            animacionRight()
        else:
            #marco.after(15,marco.move(jeep,50,0))
            marco.delete(box2)
            animacionLeft()

    #ENEMIGO FOLL
    elif 6 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
        if marco.coords(jeep)> marco.coords(enemyFoll):
            marco.delete(box2)
            animacionRight()
        else:
            #marco.after(15,marco.move(jeep,50,0))
            marco.delete(box2)
            animacionLeft()


    #ENEMIGO FOLL2
    elif 7 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
        if marco.coords(jeep)> marco.coords(enemyFoll2):
            marco.delete(box2)
            animacionRight()
        else:
            #marco.after(15,marco.move(jeep,50,0))
            marco.delete(box2)
            animacionLeft()


    #ENIMGO MOV
    elif 8 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
        if marco.coords(jeep)> marco.coords(enemyMov):
            marco.delete(box2)
            animacionRight()
        else:
            #marco.after(15,marco.move(jeep,50,0))
            marco.delete(box2)
            animacionLeft()
            
    #ENEMIGO MOV2
    elif 9 in marco.find_overlapping(box[0],box[1],box[2],box[3]):
        if marco.coords(jeep)> marco.coords(enemyMov2):
            marco.delete(box2)
            animacionRight()
        else:
            #marco.after(15,marco.move(jeep,50,0))
            marco.delete(box2)
            animacionLeft()
            
def animacionLeft():
    marco.itemconfigure(jeep, state='hidden')
    for a in range (len(choqueLeft)):
        display1=marco.create_image(marco.coords(jeep)[0]-13,marco.coords(jeep)[1],image=choqueLeft[a], anchor=NW)
        marco.after(50,marco.move(display1,-20,-10))
        marco.move(display1,-20,-10)
        marco.after(15,marco.move(jeep,-20,-10))
        #marco.move(display1,-50,0)
        if a==4:
            #marco.after(15,marco.move(display1,50,0))
            marco.delete(display1)
            marco.move(jeep,-20,-10)
        game.update()
        marco.delete(display1)
    marco.itemconfigure(jeep, state='normal')
    
def animacionRight():
    marco.itemconfigure(jeep, state='hidden')
    for a in range (len(choqueRight)):    
        display1=marco.create_image(marco.coords(jeep)[0]-13,marco.coords(jeep)[1],image=choqueRight[a], anchor=NW)
        marco.after(50,marco.move(display1,20,-10))
        marco.move(display1,20,-10)
        marco.after(15,marco.move(jeep,20,-10))
        #marco.move(display1,+50,0)
        if a==4:
            #marco.after(15,marco.move(display1,20,0))
            marco.delete(display1)
            marco.move(jeep,20,-10)
        game.update()
        #time.sleep(1.0)
        
        marco.delete(display1)
    marco.itemconfigure(jeep, state='normal')

def animacionMapaLeft():
    marco.itemconfigure(jeep, state='hidden')
    for a in range (len(explosiones)):
         
        display=marco.create_image(marco.coords(jeep)[0]-13,marco.coords(jeep)[1],image=explosiones[a], anchor=NW)
        if a==6:
            marco.delete(display)
            marco.move(jeep,+50,0)

        game.update()
        time.sleep(0.2)
        marco.delete(display)
    marco.itemconfigure(jeep, state='normal')

def animacionMapaRight():
    marco.itemconfigure(jeep, state='hidden')
    for a in range (len(explosiones)):
        #explosiones
        display=marco.create_image(marco.coords(jeep)[0]-13,marco.coords(jeep)[1],image=explosiones[a], anchor=NW)
        if a==6:
            marco.delete(display)
            marco.move(jeep,-50,0)
                #marco.move(mapaPrincipal,0,0)
        game.update()
        time.sleep(0.2)
        marco.delete(display)
    marco.itemconfigure(jeep, state='normal')

def enemigoMueve():
    numerosAleatorios()
    if marco.coords(mapaPrincipal)[1] == -19700:
        marco.coords(enemyMov,num2,0)
        
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

    elif marco.coords(mapaPrincipal)[1] == -2800:  
         marco.coords(enemyMov,num1,0)

    elif marco.coords(mapaPrincipal)[1]>-13800 and marco.coords(mapaPrincipal)[1] < -13700:
        
        while marco.coords(mapaPrincipal)[1]< -13700:
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
            
    elif marco.coords(mapaPrincipal)[1] == -14900:  
         marco.coords(enemyMov,num1,0)

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
    numerosAleatorios()
             #enemigo que me sigue            
    if marco.coords(mapaPrincipal)[1] == -25200:

        marco.coords(enemyFoll,num2,0)
        
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
            
    elif marco.coords(mapaPrincipal)[1] == -8500:
        marco.coords(enemyFoll, num1,0)
        
    elif marco.coords(mapaPrincipal)[1]>-8500 and marco.coords(mapaPrincipal)[1]<-8400:
        valorCoord=0
        while marco.coords(jeep)[0]!= marco.coords(enemyFoll)[0]:
 
            marco.after(15,marco.move(mapaPrincipal,0,10))
           
            if marco.coords(jeep)[0]>marco.coords(enemyFoll)[0]:
              
                valorCoord= marco.coords(jeep)[0]-marco.coords(enemyFoll)[0]
                marco.after(15,marco.move(enemyFoll,valorCoord,0))
                
            else:
                valorCoords= marco.coords(enemyFoll)[0]-marco.coords(jeep)[0]
                marco.after(15,marco.move(enemyFoll,-valorCoord,0))
        
            game.update()


    elif marco.coords(mapaPrincipal)[1] == -10200:
        marco.coords(enemyFoll, num1,0)
        
    elif marco.coords(mapaPrincipal)[1]>-10200 and marco.coords(mapaPrincipal)[1]<-10100:
        valorCoord=0
        while marco.coords(jeep)[0]!= marco.coords(enemyFoll)[0]:
 
            marco.after(15,marco.move(mapaPrincipal,0,10))
           
            if marco.coords(jeep)[0]>marco.coords(enemyFoll)[0]:
              
                valorCoord= marco.coords(jeep)[0]-marco.coords(enemyFoll)[0]
                marco.after(15,marco.move(enemyFoll,valorCoord,0))
                
            else:
                valorCoords= marco.coords(enemyFoll)[0]-marco.coords(jeep)[0]
                marco.after(15,marco.move(enemyFoll,-valorCoord,0))
        
            game.update()

    elif marco.coords(mapaPrincipal)[1] == -4500:
        marco.coords(enemyFoll, num1,0)
    
    elif marco.coords(mapaPrincipal)[1]>-4500 and marco.coords(mapaPrincipal)[1]<-4400:
        valorCoord=0
        while marco.coords(jeep)[0]!= marco.coords(enemyFoll)[0]:
 
            marco.after(15,marco.move(mapaPrincipal,0,10))
           
            if marco.coords(jeep)[0]>marco.coords(enemyFoll)[0]:
              
                valorCoord= marco.coords(jeep)[0]-marco.coords(enemyFoll)[0]
                marco.after(15,marco.move(enemyFoll,valorCoord,0))
                
            else:
                valorCoords= marco.coords(enemyFoll)[0]-marco.coords(jeep)[0]
                marco.after(15,marco.move(enemyFoll,-valorCoord,0))
        
            game.update()


    

def enemigosApariciones():
#CARRO APARICION enemigo 1
    numerosAleatorios()
    
    if marco.coords(mapaPrincipal)[1] == -27190:
        marco.coords(enemyState,num1,0)
    #aparicion enemigo 2
                
    elif marco.coords(mapaPrincipal)[1] == -27490:
        marco.coords(enemyState2,num1,0)

    #segunda aparicion enemigo1
    elif marco.coords(mapaPrincipal)[1] == -24000:
        marco.coords(enemyState,num2,0)

    #segunda aparicion enemigo 2

    elif marco.coords(mapaPrincipal)[1] == -24440:
        marco.coords(enemyState2,num2,0)

    #tercera aparicion enemigo 1
    elif marco.coords(mapaPrincipal)[1] == -20340:
        marco.coords(enemyState,num2,0)

    elif marco.coords(mapaPrincipal)[1] == -16900:
        marco.coords(enemyState,num1,0)

    elif marco.coords(mapaPrincipal)[1] == -12170:
        marco.coords(enemyState,num1,0)

    elif marco.coords(mapaPrincipal)[1] == -14500:
        marco.coords(enemyState2,num1,0)

    elif marco.coords(mapaPrincipal)[1] == -22350:
        marco.coords(enemyState2,num2,0)

    elif marco.coords(mapaPrincipal)[1] == -20790:
        marco.coords(enemyState2,num2,0)

    elif marco.coords(mapaPrincipal)[1] == -13840:
        marco.coords(enemyState,num1,0)

    elif marco.coords(mapaPrincipal)[1] == -11000:
        marco.coords(enemyState2,num1,0)

    elif marco.coords(mapaPrincipal)[1] == -9500:
        marco.coords(enemyState,num1,0)

    elif marco.coords(mapaPrincipal)[1] == -8500:
        marco.coords(enemyState2,num1,0)

    elif marco.coords(mapaPrincipal)[1] == -7700:
        marco.coords(enemyState,num1,0)

    elif marco.coords(mapaPrincipal)[1] == -5500:
        marco.coords(enemyState2,num1,0)

    elif marco.coords(mapaPrincipal)[1] == -3500:
        marco.coords(enemyState,num1,0)
 
       
def manchasAceites():
    numerosAleatorios()
    
    if marco.coords(mapaPrincipal)[1] == -28190:
        marco.coords(petrol,num1,0)

              #segunda aparicion mancha
    elif marco.coords(mapaPrincipal)[1] == -23500:
        marco.coords(petrol,num2,0)
                
        #tercera aparicion mancha
    elif marco.coords(mapaPrincipal)[1] == -20000:
        marco.coords(petrol,num2,0)

        #cuarta aparicicon mancha de aceite
    elif marco.coords(mapaPrincipal)[1] == -15000:
        marco.coords(petrol,num1,0)

    elif marco.coords(mapaPrincipal)[1] == -22000:
        marco.coords(petrol,num2,0)

    elif marco.coords(mapaPrincipal)[1] == -3000:
        marco.coords(petrol,num1,0)


        

#MAPAS DE LINEA RECTA
def enemigoMueve2():
    numerosAleatoriosRecta()
    if marco.coords(mapaPrincipal)[1] == -19700:
        marco.coords(enemyMov,num3,0)
        
    elif marco.coords(mapaPrincipal)[1]>-19700 and marco.coords(mapaPrincipal)[1] < -19600:
        
        while marco.coords(mapaPrincipal)[1]< -19600:
            #llamo el after para el mapa ya que con esto evito el lag al hacer las siguientes acciones
            marco.after(15,marco.move(mapaPrincipal,0,10))

            #AQUI LE DIGO QUE SI ES MAYOR A 330 UE ES LA MITAD DE LA CARRETERA SE CORRA
            if marco.coords(enemyMov)[0]>300:
                marco.after(15,marco.move(enemyMov,-10,0))
                
                #game.update()
                #aqui como no se va a cumplir el if de arriba se sobre entiende que nuestro carro esta en una posicion menor al enemigo
                #por eso en este caso la direccion en el eje x se debe de restar
            else:
                marco.after(15,marco.move(enemyMov,10,0))
            game.update()


    elif marco.coords(mapaPrincipal)[1] == -2800:  
         marco.coords(enemyMov,num3,0)

    elif marco.coords(mapaPrincipal)[1]>-13800 and marco.coords(mapaPrincipal)[1] < -13700:
        
        while marco.coords(mapaPrincipal)[1]< -13700:
            #llamo el after para el mapa ya que con esto evito el lag al hacer las siguientes acciones
            marco.after(15,marco.move(mapaPrincipal,0,10))
            if marco.coords(enemyMov)[0]>300:
                marco.after(15,marco.move(enemyMov,-10,0))
 
            else:
                marco.after(15,marco.move(enemyMov,10,0))
            game.update()
            
    elif marco.coords(mapaPrincipal)[1] == -14900:  
         marco.coords(enemyMov,num3,0)

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
    
 
def enemigosSiguen2():
    numerosAleatoriosRecta()
    numerosAleatorios()
             #enemigo que me sigue            
    if marco.coords(mapaPrincipal)[1] == -25200:

        marco.coords(enemyFoll,num3,0)
        
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
            
    elif marco.coords(mapaPrincipal)[1] == -8500:
        marco.coords(enemyFoll, num1,0)
        
    elif marco.coords(mapaPrincipal)[1]>-8500 and marco.coords(mapaPrincipal)[1]<-8400:
        valorCoord=0
        while marco.coords(jeep)[0]!= marco.coords(enemyFoll)[0]:
 
            marco.after(15,marco.move(mapaPrincipal,0,10))
           
            if marco.coords(jeep)[0]>marco.coords(enemyFoll)[0]:
              
                valorCoord= marco.coords(jeep)[0]-marco.coords(enemyFoll)[0]
                marco.after(15,marco.move(enemyFoll,valorCoord,0))
                
            else:
                valorCoords= marco.coords(enemyFoll)[0]-marco.coords(jeep)[0]
                marco.after(15,marco.move(enemyFoll,-valorCoord,0))
        
            game.update()


    elif marco.coords(mapaPrincipal)[1] == -10200:
        marco.coords(enemyFoll, num1,0)
        
    elif marco.coords(mapaPrincipal)[1]>-10200 and marco.coords(mapaPrincipal)[1]<-10100:
        valorCoord=0
        while marco.coords(jeep)[0]!= marco.coords(enemyFoll)[0]:
 
            marco.after(15,marco.move(mapaPrincipal,0,10))
           
            if marco.coords(jeep)[0]>marco.coords(enemyFoll)[0]:
              
                valorCoord= marco.coords(jeep)[0]-marco.coords(enemyFoll)[0]
                marco.after(15,marco.move(enemyFoll,valorCoord,0))
                
            else:
                valorCoords= marco.coords(enemyFoll)[0]-marco.coords(jeep)[0]
                marco.after(15,marco.move(enemyFoll,-valorCoord,0))
        
            game.update()

    elif marco.coords(mapaPrincipal)[1] == -4500:
        marco.coords(enemyFoll, num3,0)
    
    elif marco.coords(mapaPrincipal)[1]>-4500 and marco.coords(mapaPrincipal)[1]<-4400:
        valorCoord=0
        while marco.coords(jeep)[0]!= marco.coords(enemyFoll)[0]:
 
            marco.after(15,marco.move(mapaPrincipal,0,10))
           
            if marco.coords(jeep)[0]>marco.coords(enemyFoll)[0]:
              
                valorCoord= marco.coords(jeep)[0]-marco.coords(enemyFoll)[0]
                marco.after(15,marco.move(enemyFoll,valorCoord,0))
                
            else:
                valorCoords= marco.coords(enemyFoll)[0]-marco.coords(jeep)[0]
                marco.after(15,marco.move(enemyFoll,-valorCoord,0))
        
            game.update()


#####################################################    

def enemigosApariciones2():
#CARRO APARICION enemigo 1
    numerosAleatoriosRecta()
    
    if marco.coords(mapaPrincipal)[1] == -27190:
        marco.coords(enemyState,num3,0)
    #aparicion enemigo 2
                
    elif marco.coords(mapaPrincipal)[1] == -27490:
        marco.coords(enemyState2,num3,0)

    #segunda aparicion enemigo1
    elif marco.coords(mapaPrincipal)[1] == -24000:
        marco.coords(enemyState,num3,0)

    #segunda aparicion enemigo 2

    elif marco.coords(mapaPrincipal)[1] == -24440:
        marco.coords(enemyState2,num3,0)

    #tercera aparicion enemigo 1
    elif marco.coords(mapaPrincipal)[1] == -20340:
        marco.coords(enemyState,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -16900:
        marco.coords(enemyState,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -12170:
        marco.coords(enemyState,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -14500:
        marco.coords(enemyState2,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -22350:
        marco.coords(enemyState2,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -20790:
        marco.coords(enemyState2,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -13840:
        marco.coords(enemyState,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -11000:
        marco.coords(enemyState2,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -9500:
        marco.coords(enemyState,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -8500:
        marco.coords(enemyState2,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -7700:
        marco.coords(enemyState,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -5500:
        marco.coords(enemyState2,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -3500:
        marco.coords(enemyState,num3,0)
 
       
def manchasAceites2():
    numerosAleatoriosRecta()
    
    if marco.coords(mapaPrincipal)[1] == -28190:
        marco.coords(petrol,num3,0)

              #segunda aparicion mancha
    elif marco.coords(mapaPrincipal)[1] == -23500:
        marco.coords(petrol,num3,0)
                
        #tercera aparicion mancha
    elif marco.coords(mapaPrincipal)[1] == -20000:
        marco.coords(petrol,num3,0)

        #cuarta aparicicon mancha de aceite
    elif marco.coords(mapaPrincipal)[1] == -15000:
        marco.coords(petrol,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -22000:
        marco.coords(petrol,num3,0)

    elif marco.coords(mapaPrincipal)[1] == -3000:
        marco.coords(petrol,num3,0)

#FIN MAPAS LINEA RECTA


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
mapaPelea=PhotoImage(file="mapWorld3.png")

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

#choques Left
choque1= PhotoImage(file="crash1.png")
choque2= PhotoImage(file="crash2.png")
choque2_1= PhotoImage(file="crash2_1.png")
choque2_2= PhotoImage(file="crash2_2.png")
choqueLeft=[choque1,choque2, choque2_1,choque2_2]

#choques right
choque3=PhotoImage(file="crash3.png")
choque4= PhotoImage(file="crash4.png")
choque4_1= PhotoImage(file="crash4_1.png")
choque4_2= PhotoImage(file="crash4_2.png")
choqueRight=[choque3,choque4,choque4_1,choque4_2]

def numerosAleatoriosRecta():
    for a in range(1):
        global num3
        num3=random.randrange(260,509,30)   
        

def numerosAleatorios():
    for a in range(1):
        global num1
        num1=random.randrange(280,410,20)   
        global num2
        num2=random.randrange(420,608,20)
 

  
# funcion para iniciar el juego el mapa 1
def empezar():
    game.geometry("820x580")
    # de iconify para maximixar la ventana cuando ya presione el boton
    game.deiconify()
    marco.pack()
    raiz.withdraw()
    # nueva ventana
    game.resizable(width=False, height=False)

   
    global mapaPrincipal 
    mapaPrincipal = marco.create_image(-2,-28200, image=mapa, anchor=NW)
    global petrol
    petrol = marco.create_image(-35, 0, image=aceite, anchor=NW)   
    # tenemos que darle una variable para los eventos de las teclas
    
    miniRoad = marco.create_image(0, 0, image=miniCarretera, anchor=NW)

    #IMAGENES PARA LOS ENEMIGOS 
    global enemyState
    enemyState= marco.create_image(-35, 0, image=enemigoState, anchor=NW)
    #NUMEROS RANDOMS PARA LOS ENEMIGOS
    #aparicion1
    global numEnemy1
    numEnemy1=random.randrange(360,480,10)
   
    global enemyState2
    enemyState2 = marco.create_image(-35, 0, image=enemigoState2, anchor=NW)
    #NUMEROS RANDOMS PARA LOS ENEMIGOS
    #aparicion1
   
    #ENMIGOS QUE ME SIGUEN
    global enemyFoll
    enemyFoll= marco.create_image(-35, 0, image=enemigoFollow, anchor=NW)
    #aparicion1
    
    
    global enemyFoll2
    enemyFoll2= marco.create_image(-35, 0, image=enemigoFollow2, anchor=NW)
    #aparicion1
   

    #ENEMIGOS QUE SE MUEVEN
    global enemyMov
    enemyMov= marco.create_image(-35, 0, image=enemigoMove, anchor=NW)
    #aparicion 1
   
    
    global enemyMov2
    enemyMov2= marco.create_image(-35, 0, image=enemigoMove2, anchor=NW)
    #aparicion1

    global jeep
    jeep = marco.create_image(365, 480, image=carroPrincipal, anchor=NW)

    
    nombre=Label(marco, textvariable=player)
    nombre.place(x=100,y=0)
    


    

    
    #miniCuper = marco.create_image(0, 525, image=carroMini, anchor=NW) 
    #aceite = PhotoImage(file="aceite.png")
    #bind para asignar que move es con una tecla
    marco.bind("<KeyPress>", moveCarroPrincipal)
    marco.bind("<w>", moveMapaP)
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

   
    global mapaPrincipal 
    mapaPrincipal = marco.create_image(-2,-28200, image=mapaDesierto, anchor=NW)
    global petrol
    petrol = marco.create_image(-35, 0, image=aceite, anchor=NW)   
    # tenemos que darle una variable para los eventos de las teclas
    
    miniRoad = marco.create_image(0, 0, image=miniCarretera, anchor=NW)

    #IMAGENES PARA LOS ENEMIGOS 
    global enemyState
    enemyState= marco.create_image(-35, 0, image=enemigoState, anchor=NW)
    #NUMEROS RANDOMS PARA LOS ENEMIGOS
    #aparicion1
    global numEnemy1
    numEnemy1=random.randrange(360,480,10)
   
    global enemyState2
    enemyState2 = marco.create_image(-35, 0, image=enemigoState2, anchor=NW)
    #NUMEROS RANDOMS PARA LOS ENEMIGOS
    #aparicion1
   
    #ENMIGOS QUE ME SIGUEN
    global enemyFoll
    enemyFoll= marco.create_image(-35, 0, image=enemigoFollow, anchor=NW)
    #aparicion1
    
    
    global enemyFoll2
    enemyFoll2= marco.create_image(-35, 0, image=enemigoFollow2, anchor=NW)
    #aparicion1
   

    #ENEMIGOS QUE SE MUEVEN
    global enemyMov
    enemyMov= marco.create_image(-35, 0, image=enemigoMove, anchor=NW)
    #aparicion 1
   
    
    global enemyMov2
    enemyMov2= marco.create_image(-35, 0, image=enemigoMove2, anchor=NW)
    #aparicion1

    global jeep
    jeep = marco.create_image(365, 480, image=carroPrincipal, anchor=NW)

    marco.bind("<KeyPress>", moveCarroSegundoMap)
    marco.focus_set()
    game.mainloop()

def nivel3():
    game.geometry("820x580")
    # de iconify para maximixar la ventana cuando ya presione el boton
    game.deiconify()
    marco.pack()
    raiz.withdraw()
    # nueva ventana
    game.resizable(width=False, height=False)

   
    global mapaPrincipal 
    mapaPrincipal = marco.create_image(-2,-28200, image=mapaPelea, anchor=NW)
    global petrol
    petrol = marco.create_image(-35, 0, image=aceite, anchor=NW)   
    # tenemos que darle una variable para los eventos de las teclas
    
    miniRoad = marco.create_image(0, 0, image=miniCarretera, anchor=NW)

    #IMAGENES PARA LOS ENEMIGOS 
    global enemyState
    enemyState= marco.create_image(-35, 0, image=enemigoState, anchor=NW)
    #NUMEROS RANDOMS PARA LOS ENEMIGOS
    #aparicion1
    global numEnemy1
    numEnemy1=random.randrange(360,480,10)
   
    global enemyState2
    enemyState2 = marco.create_image(-35, 0, image=enemigoState2, anchor=NW)
    #NUMEROS RANDOMS PARA LOS ENEMIGOS
    #aparicion1
   
    #ENMIGOS QUE ME SIGUEN
    global enemyFoll
    enemyFoll= marco.create_image(-35, 0, image=enemigoFollow, anchor=NW)
    #aparicion1
    
    
    global enemyFoll2
    enemyFoll2= marco.create_image(-35, 0, image=enemigoFollow2, anchor=NW)
    #aparicion1
   

    #ENEMIGOS QUE SE MUEVEN
    global enemyMov
    enemyMov= marco.create_image(-35, 0, image=enemigoMove, anchor=NW)
    #aparicion 1
   
    
    global enemyMov2
    enemyMov2= marco.create_image(-35, 0, image=enemigoMove2, anchor=NW)
    #aparicion1

    global jeep
    jeep = marco.create_image(365, 480, image=carroPrincipal, anchor=NW)

    marco.bind("<KeyPress>", moveCarroTercerMap)
    marco.focus_set()
    game.mainloop()



# BOTON PARA INICIAR LA PANTALLA DE JUEGO


player = tkinter.StringVar()
player.set("")


# inicia el segundo menu para ya empezar el juego
def iniciar():
    #global player
    
    textoJugador = ttk.Entry(raiz, textvariable=player, width=30)
    #global player
    #player=textoJugador.get()
    #nombre = Label(marco, text=player)

    #nombre.place(x=100,y=10)
    
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
nivelNormal = ttk.Button(raiz, text="MAPA3",command=nivel3)  # tener cuidado con estos botones y no olvidarlos son para los niveles
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