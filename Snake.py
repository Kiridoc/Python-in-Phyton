import turtle
import time
import random



posponer = 0.1

#Marcador
score = 0
high_score = 0

#Configuración de la ventana
window = turtle.Screen()        #Crea la ventana
window.title("Snake Game")      #Pon el título
window.bgcolor("black")                 #Pon color al fondo
window.setup(width=600 , height=600)        #Pon las dimesiones de la ventana
window.tracer(0)                        #Esta linea hará que las animaciones sean visualmente más agradables

#Cabeza de la serpiente
cabeza = turtle.Turtle()    #Crear al cabeza
cabeza.speed(0)             #Velocidad de la serpiente
cabeza.shape("square")      #Forma de la cabeza
cabeza.penup()
cabeza.color("purple")
cabeza.goto(0,0)
cabeza.direccion = "stop"

#Comida
comida = turtle.Turtle()   
comida.speed(0)             
comida.shape("circle")      
comida.penup()
comida.color("red")
comida.goto(0,100)

#Segmentos / cuerpo de serpiente
segmentos = []

#Texto puntuación
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0       High Score: 0", align="center", font=("Courier",22,"normal"))

#Texto Game Over
game_over = turtle.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.goto(0, 0)  # Esto coloca el mensaje en el centro de la pantalla
game_over.color("red")

#FUNCIONES---------------------------------------------------------------------------
def perder():
    game_over.write("Game Over", align="center", font=("Arial", 20, "bold"))
    cabeza.direccion = "stop"
    window.ontimer(reiniciar,2000)

def reiniciar():
    cabeza.goto(0,0)
    for segmento in segmentos:
        segmento.forward(1000)
        segmento.hideturtle()
    segmentos.clear()
    game_over.clear()
    #Reiniciar marcador
    texto.clear()
    texto.write(f"Score: {score}       High Score: {high_score}", align="center", font=("Courier",22,"normal"))
#------------------------------------------------------------------------------------

#Funciones
def arriba():
    if cabeza.direccion != "down":
        cabeza.direccion = "up"
def abajo():
    if cabeza.direccion != "up":
        cabeza.direccion = "down"
def izquierda():
    if cabeza.direccion != "right":
        cabeza.direccion = "left"
def derecha():
    if cabeza.direccion != "left":
        cabeza.direccion = "right"


def movimiento():
    if cabeza.direccion == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direccion == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direccion == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    if cabeza.direccion == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

#Teclado
window.listen()
window.onkeypress(arriba, "Up")
window.onkeypress(abajo, "Down")
window.onkeypress(izquierda, "Left")
window.onkeypress(derecha, "Right")

while True:
    window.update()

    #Colisión con los bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        perder()
        posponer = 0.1
        score = 0

        

    #Colisión de la comida
    if cabeza.distance(comida) < 28:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()   
        nuevo_segmento.speed(0)             
        nuevo_segmento.shape("square")      
        nuevo_segmento.penup()
        nuevo_segmento.color("magenta")
        segmentos.append(nuevo_segmento)
        posponer -= 0.001

        #Aumentar marcadores
        score += 10
        if score > high_score:
            high_score = score
        texto.clear()
        texto.write(f"Score: {score}       High Score: {high_score}", align="center", font=("Courier",22,"normal"))

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    if (cabeza.direccion != "stop"):
        for index in range(totalSeg -1, 0, -1):
            x = segmentos[index - 1].xcor()
            y = segmentos[index - 1].ycor()
            segmentos[index].goto(x,y)
        
        if totalSeg > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            segmentos[0].goto(x,y)

    movimiento()

    #Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza)  < 20:
            perder()
            posponer = 0.1
            score = 0

    time.sleep(posponer)