from turtle import Turtle, Screen
import random

is_race_on = False
pantalla = Screen()
pantalla.setup(width=500, height=400)
apuesta_usuario = pantalla.textinput(title="Has tu apuesta.", prompt="¿Qué tortuga ganará la carrera? "
                                                                     "Ingresa un color: ")
colores = ["yellow", "blue", "red", "green", "orange", "purple"]
posiciones_y = [-75, -45, -15, 15, 45, 75]
tortugas = []

for turtle_index in range(0, 6):
    tortuga_nueva = Turtle(shape="turtle")
    tortuga_nueva.color(colores[turtle_index])
    tortuga_nueva.penup()
    tortuga_nueva.goto(x=-230, y=posiciones_y[turtle_index])
    tortugas.append(tortuga_nueva)

if apuesta_usuario:
    is_race_on = True

while is_race_on:

    for tortuga in tortugas:
        if tortuga.xcor() > 230:
            is_race_on = False
            color_ganador = tortuga.pencolor()
            if color_ganador == apuesta_usuario:
                print(f"Ganaste! La tortuga {color_ganador} es el ganador!")
            else:
                print(f"Perdiste! La tortuga {color_ganador} es el ganador!")

        distancia_aleatoria = random.randint(0, 10)
        tortuga.forward(distancia_aleatoria)

pantalla.exitonclick()
