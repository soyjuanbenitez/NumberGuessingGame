import random


def main():
    numero_aleatorio = random.randint(1, 100)
    saludo = print(""" 
    ¡¡Hola, Bienvenido al juego de adivinar el número!! 🎮
    Voy a pensar en un número del 1 al 100 y si lo adivinas ganas. 
    """)
    numero_usuario = int(input("Ahora escribe un número, recuerda 🤯 que sea entre el 1 y el 100: "))
    
    # Mientras el número ingresado por teclado 
    # es diferente al número aleatorio entramos al bucle
    while numero_usuario != numero_aleatorio:
        # Si el número del usuario es menor al número aleatorio se deberá introducir 
        # un número más alto, en caso contrario deberá introducir un número más bajo.
        if numero_usuario < numero_aleatorio:
            print("El número que has elegido es menor al que yo tengo en mente 🤖, busca uno más grande 📈")
        else:
            print("El número que has elegido es mayor al que yo tengo en mente 🤖, busca uno más pequeño 📉")
        numero_usuario = int(input("Escribe otro número: "))
    print("🎉🎉 ¡¡¡Felicitaciones, Ganaste el juego!!! 🎉🎉")


if __name__ == '__main__':
    main()