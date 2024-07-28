import turtle
import time
import random
import threading

#Serpiente---------------------------------------------------------
class Serpiente:
    def __init__(self,color,x,y,coordPunt):
        #Cabeza
        self.cabeza = turtle.Turtle()
        self.cabeza.speed(0)
        self.cabeza.shape("square")
        self.cabeza.penup()
        self.cabeza.color(color)
        self.cabeza.goto(x,y)
        self.cabeza.direccion = "stop"

        #Segmentos
        self.segmentos = []

        #Marcador
        self.score = 0

        #Texto puntuación
        self.texto = turtle.Turtle()
        self.texto.speed(0)
        self.texto.color("white")
        self.texto.penup()
        self.texto.hideturtle()
        self.texto.goto(coordPunt,260)
        self.texto.write("Score: 0", align="center", font=("Courier",22,"normal"))

        #Texto Game Over
        self.game_over = turtle.Turtle()
        self.game_over.hideturtle()
        self.game_over.penup()
        self.game_over.goto(0, 0)
        self.game_over.color(color)

#------------------------------------------------------------------

#Comida------------------------------
class Comida:
    def __init__(self):
       self.comida = turtle.Turtle()   
       self.comida.speed(0)             
       self.comida.shape("circle")      
       self.comida.penup()
       self.comida.color("red")
       self.comida.goto(0,100)
#------------------------------------




#--------------------------------------------------JUEGO-----------------------------------------------------------
posponer = 0.08
cronometro = 120

#Cronómetro
contador = turtle.Turtle()
contador.speed(0)
contador.color("white")
contador.penup()
contador.hideturtle()
contador.goto(0,260)
contador.write(f"Tiempo: {cronometro}", align="center", font=("Courier",22,"normal"))




#Configuración de la ventana----------------
window = turtle.Screen()       
window.title("Snake Game")      
window.bgcolor("black")               
window.setup(width=1280 , height=600)        
window.tracer(0)   

root = window.getcanvas().winfo_toplevel()
root.resizable(False, False)
#-------------------------------------------          
#        

#Serpientes y manzana----------------------
serpiente1 = Serpiente("green",-200,0,-550)
serpiente2 = Serpiente("purple",200,0,545)
manzana = Comida()
#-------------------------------------------


#Reiniciar_Serpiente---------------------------------------------------------------------------------------------
def reiniciarSerpiente(serp,x):
    
    serp.cabeza.goto(x,0)

    for segmento in serp.segmentos:
        segmento.forward(1000)
        segmento.hideturtle()
    serp.segmentos.clear()
    serp.game_over.clear()
    #Reiniciar marcador
    serp.texto.clear()
    serp.texto.write("Score: 0", align="center", font=("Courier",22,"normal"))
    serp.score = 0
#--------------------------------------------------------------------------------------------------------------

#Reiniciar-------------------------------
def reiniciar():
    reiniciarSerpiente(serpiente1,-200)
    reiniciarSerpiente(serpiente2,200)
#----------------------------------------

    

#Game_Over---------------------------------------------------------------------------
def ganar(serp,jugador):
    serpiente1.cabeza.direccion = "stop"
    serpiente2.cabeza.direccion = "stop"
    if jugador == '-':
        serp.game_over.color("gray")
    serp.game_over.write(f"¡Ganador {jugador}!", align="center", font=("Arial", 20, "bold"))
    if jugador == '-':
        serp.game_over.color("green")
    window.ontimer(reiniciar,2000)
#------------------------------------------------------------------------------------




#Funciones para dirección--------------
def arriba(serp):
    if serp.cabeza.direccion != "down":
        serp.cabeza.direccion = "up"
def abajo(serp):
    if serp.cabeza.direccion != "up":
        serp.cabeza.direccion = "down"
def izquierda(serp):
    if serp.cabeza.direccion != "right":
        serp.cabeza.direccion = "left"
def derecha(serp):
    if serp.cabeza.direccion != "left":
        serp.cabeza.direccion = "right"
#--------------------------------------

#Movimiento de las serpientes----------------
def movimiento(serp):
    if serp.cabeza.direccion == "up":
        y = serp.cabeza.ycor()
        serp.cabeza.sety(y + 20)

    if serp.cabeza.direccion == "down":
        y = serp.cabeza.ycor()
        serp.cabeza.sety(y - 20)

    if serp.cabeza.direccion == "right":
        x = serp.cabeza.xcor()
        serp.cabeza.setx(x + 20)

    if serp.cabeza.direccion == "left":
        x = serp.cabeza.xcor()
        serp.cabeza.setx(x - 20)
#--------------------------------------------

#Teclado--------------------------------------------
window.listen()

window.onkeypress(lambda: arriba(serpiente1), "Up")
window.onkeypress(lambda: abajo(serpiente1), "Down")
window.onkeypress(lambda: izquierda(serpiente1), "Left")
window.onkeypress(lambda: derecha(serpiente1), "Right")

window.onkeypress(lambda: arriba(serpiente2), "w")
window.onkeypress(lambda: abajo(serpiente2), "s")
window.onkeypress(lambda: izquierda(serpiente2), "a")
window.onkeypress(lambda: derecha(serpiente2), "d")
#----------------------------------------------------

#Aumentar marcadores--------------------------------------------------------------------------------
def aumentarMarcador(serp):
        serp.score += 10
        serp.texto.clear()
        serp.texto.write(f"Score: {serp.score}", align="center", font=("Courier",22,"normal"))
#---------------------------------------------------------------------------------------------------

#Colisión de la comida----------------------------------
def colisionComida(serp,color):
    if serp.cabeza.distance(manzana.comida) < 28:
        x = random.randint(-550,550)
        y = random.randint(-260,260)
        manzana.comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()   
        nuevo_segmento.speed(0)             
        nuevo_segmento.shape("square")      
        nuevo_segmento.penup()
        nuevo_segmento.color(color)
        serp.segmentos.append(nuevo_segmento)
        #posponer -= 0.001

        aumentarMarcador(serp)
#-------------------------------------------------------

#Mover el cuerpo de las serpientes-------------
def moverCuerpo(serp):
    totalSeg = len(serp.segmentos)
    if (serp.cabeza.direccion != "stop"):
        for index in range(totalSeg -1, 0, -1):
            x = serp.segmentos[index - 1].xcor()
            y = serp.segmentos[index - 1].ycor()
            serp.segmentos[index].goto(x,y)
        
        if totalSeg > 0:
            x = serp.cabeza.xcor()
            y = serp.cabeza.ycor()
            serp.segmentos[0].goto(x,y)
#----------------------------------------------

#Colision con borde---------------------------------------------------------------------------------------------------------
def colision_borde(serp,serp2,jugador):
    if serp.cabeza.xcor() > 620 or serp.cabeza.xcor() < -620 or serp.cabeza.ycor() > 290 or serp.cabeza.ycor() < -290:
        ganar(serp2,jugador)
#---------------------------------------------------------------------------------------------------------------------------

#Colision con cuerpo----------
def colision_cuerpo(serp1,serp2,jugador):
    first = True
    for segmento in serp2.segmentos:
        if segmento.distance(serp1.cabeza)  < 20:
            ganar(serp2,jugador)
    for segmento in serp1.segmentos:
        if segmento.distance(serp1.cabeza)  < 20 and not first:
            ganar(serp2,jugador)
        first = False

tiempo_anterior = time.time()

while True:

    #Tiempo--------------------------
    tiempo_actual = time.time()
    if tiempo_actual - tiempo_anterior >= 1:
        contador.clear()
        contador.write(f"Tiempo: {cronometro}", align="center", font=("Courier",22,"normal"))
        cronometro -= 1
        tiempo_anterior = tiempo_actual

    if cronometro == -1:
        if serpiente1.score > serpiente2.score:
            ganar(serpiente1,"J1")
        elif serpiente2.score > serpiente1.score:
            ganar(serpiente2,"J2")
        else:
            ganar(serpiente1,"-")
    
    if cronometro == -2 or (serpiente1.cabeza.direccion == "stop" and serpiente2.cabeza.direccion == "stop"):
        cronometro = 120
    #--------------------------------

    window.update()

    movimiento(serpiente1)
    movimiento(serpiente2)

    colisionComida(serpiente1,"lightgreen")
    colisionComida(serpiente2,"magenta")

    moverCuerpo(serpiente1)
    moverCuerpo(serpiente2)

    colision_borde(serpiente1,serpiente2,"J2")
    colision_borde(serpiente2,serpiente1,"J1")

    colision_cuerpo(serpiente1,serpiente2,"J2")
    colision_cuerpo(serpiente2,serpiente1,"J1")

    time.sleep(posponer)