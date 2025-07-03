import time
import random

preguntas = {
    1: [
        {'pregunta': '¿Cuál es el color del cielo en un día despejado?', 'opciones': ['a) Verde', 'b) Azul', 'c) Rojo ', 'd) Amarillo'], 'respuesta': 'b'},
        {'pregunta': '¿Cuántos días tiene una semana?', 'opciones': ['a) 5', 'b) 6', 'c) 7', 'd) 8'], 'respuesta': 'c'},
    ],
    2: [
        {'pregunta': '¿Cuál es el planeta más cercano al sol?', 'opciones': ['a) Venus', 'b) Marte', 'c) Mercurio', 'd) Tierra'], 'respuesta': 'c'},
        {'pregunta': '¿En qué continente se encuentra Brasil?', 'opciones': ['a) Europa', 'b) Asia', 'c) América', 'd) África'], 'respuesta': 'c'}
    ],
    3: [
        {'pregunta': '¿Qué animal es conocido como el “rey de la selva”?', 'opciones': ['a) León', 'b) Elefante', 'c) Tigre', 'd) Jirafa'], 'respuesta': 'a'},
        {'pregunta': '¿Cuántos lados tiene un triángulo?', 'opciones': ['a) 3', 'b) 4', 'c) 5', 'd) 6'], 'respuesta': 'a'}
    ],
    4: [
        {'pregunta': '¿Qué gas respiramos que es esencial para vivir?', 'opciones': ['a) Dióxido de carbono', 'b) Oxígeno', 'c) Helio', 'd) Nitrógeno'], 'respuesta': 'b'},
        {'pregunta': '¿Cuál es la capital de México?', 'opciones': ['a) Monterrey', 'b) Guadalajara', 'c) Ciudad de México', 'd) Cancún'], 'respuesta': 'c'}
    ],
    5: [
        {'pregunta': '¿Quién escribió "Cien años de soledad"?', 'opciones': ['a) Pablo Neruda', 'b) Gabriel García Márquez', 'c) Isabel Allende', 'd) Mario Vargas Llosa'], 'respuesta': 'b'},
        {'pregunta': '¿Qué órgano del cuerpo humano bombea la sangre?', 'opciones': ['a) Hígado', 'b) Pulmones', 'c) Corazón', 'd) Estómago'], 'respuesta': 'c'}
    ],
    6: [
        {'pregunta': '¿Qué elemento químico tiene el símbolo "O"?', 'opciones': ['a)  Oro', 'b)  Oxígeno', 'c) Osmio', 'd) Ozono'], 'respuesta': 'b'},
        {'pregunta': '¿En qué año llegó el hombre a la Luna?', 'opciones': ['a) 1959', 'b) 1969', 'c) 1979', 'd) 1989'], 'respuesta': 'b'}
    ],
    7: [
        {'pregunta': '¿Cuál es el río más largo del mundo?', 'opciones': ['a)  Amazonas', 'b)  Nilo', 'c) Yangtsé', 'd) Misisipi'], 'respuesta': 'a'},
        {'pregunta': '¿Qué país tiene más habitantes en el mundo?', 'opciones': ['a) India', 'b) China', 'c) Estados Unidos', 'd) Indonesia'], 'respuesta': 'a'}
    ],
    8: [
        {'pregunta': '¿Qué autor escribió "La divina comedia"?', 'opciones': ['a) William Shakespeare', 'b) Dante Alighieri', 'c) Virgilio ', 'd) Cervantes'], 'respuesta': 'b'},
        {'pregunta': '¿Qué partícula subatómica tiene carga negativa?', 'opciones': ['a) Protón', 'b) Neutrón', 'c) Electrón', 'd) Quark'], 'respuesta': 'c'}
    ],
    9: [
        {'pregunta': '¿Qué científico propuso la teoría de la relatividad?', 'opciones': ['a) Isaac Newton', 'b) Albert Einstein', 'c) Galileo Galilei', 'd) Stephen Hawking'], 'respuesta': 'b'},
        {'pregunta': '¿Cuál es el país más pequeño del mundo?', 'opciones': ['a) Mónaco', 'b) San Marino', 'c) Ciudad del Vaticano', 'd) Liechtenstein'], 'respuesta': 'c'}
    ],
    10: [
        {'pregunta': '¿Qué estructura matemática es utilizada para describir las simetrías fundamentales en la física de partículas?', 'opciones': ['a) Álgebra lineal', 'b) Teoría de números', 'c) Grupos de Lie', 'd)  Cálculo diferencial'], 'respuesta': 'c'},
        {'pregunta': '¿Quién compuso la ópera “El anillo del nibelungo”?', 'opciones': ['a) Mozart', 'b) Beethoven', 'c) Verdi', 'd) Richard Wagner'], 'respuesta': 'd'}
    ]
}

dinero = 0
utilizadoLlamada = False
utilizado5050 = False
utilizadoCambio = False
comodines = {
    "1": {"nombre": "50/50", "usado": False},
    "2": {"nombre": "Llamada a un amigo", "usado": False},
    "3": {"nombre": "Cambio de pregunta", "usado": False}
}

print("BIENVENIDO A QUIEN QUIERE SER MILLONARIO")
print("ENTRAS POBRE Y SALES MILLONARIOOOOO")
print("Comenzamos el juego")
print("*" * 200)

#Rango de niveles 

for nivel in range(1, 11):
    preguntas_nivel = preguntas[nivel]
    pregunta_actual = preguntas_nivel[0]
    otra_pregunta = preguntas_nivel[1]

    cambio_activado = False  

    comodines_usados_en_esta_pregunta = []
    #Inicia el juego
    while True:
        print(f"\nLa pregunta es: {pregunta_actual['pregunta']}")
        for opcion in pregunta_actual['opciones']:
            print(opcion)
            time.sleep(1)
        #cuantos comodines disponibles tiene 
        while True:
            comodines_disponibles = [clave for clave, info in comodines.items() if not info["usado"]]
            if comodines_disponibles:
                print("\nComodines disponibles:")
                for clave in comodines_disponibles:
                    print(f"{clave}) {comodines[clave]['nombre']}")
                eleccion = input("¿Quieres usar un comodín? (Escribe número o (no) ): ").lower()
                #se mira si el jugador quiere usar un comodin
                if eleccion in comodines_disponibles or eleccion == "no":
                    if eleccion in comodines_disponibles:
                        comodines[eleccion]["usado"] = True
                        comodines_usados_en_esta_pregunta.append(eleccion)
                        print(f"\nHas utilizado el comodín: {comodines[eleccion]['nombre']}")
                    #comodin del 50/50  
                    if eleccion == "1":
                        opciones = pregunta_actual['opciones']
                        respuesta_correcta = pregunta_actual['respuesta']
                        opcion_correcta = [op for op in opciones if op.lower().startswith(respuesta_correcta)]
                        opciones_incorrectas = [op for op in opciones if not op.lower().startswith(respuesta_correcta)]
                        opcion_incorrecta = random.choice(opciones_incorrectas)
                        opciones_mostradas = [opcion_correcta[0], opcion_incorrecta]
                        random.shuffle(opciones_mostradas) # sirve para mezclar aleatoriamente el orden de los elementos de una lista
                        print(f"\nOpciones después de aplicar 50/50:")
                        for opcion in opciones_mostradas:
                            print(opcion)
                    #comodin llamada el amigo es mmuy muy inteligente
                    elif eleccion == "2":
                        print("Has elegido llamar a un amigo. Tu amigo te dice que la respuesta es:", pregunta_actual['respuesta'])
                    #cambio de pregunta 
                    elif eleccion == "3":
                        cambio_activado = True
                        pregunta_actual = otra_pregunta
                        print("Has cambiado la pregunta. La nueva pregunta es:")
                        print(pregunta_actual['pregunta'])
                        for opcion in pregunta_actual['opciones']:
                            print(opcion)
                            time.sleep(1)
                elif eleccion == "no":
                    break
                #Se comprueba si el comodin se utilizo 
                else:
                    print("Comodín no válido o ya usado.")
            else:
                print("\nYa no tienes más comodines disponibles.")
                break

            #se mira las respuestas del jugador si sale o responde bien
            respuesta = input(f"\n🤔Ingresa la letra de tu 'respuesta' (Escribe 'comodin' para utilizar otro comodín o escribe 'salir'): ").lower()
            if respuesta == "salir":
                print(f"\nTU DINERO GANADO FUE ${dinero}, GRACIAS POR JUGAR.")
                exit()
            if respuesta == pregunta_actual['respuesta']:
                print(f"\n✅ RESPUESTA CORRECTA")
                dinero += 10000
                dinero *= 2
                print(f"💰 Dinero ganado: ${dinero}")
                break  
            #El jugador pierde cada vez que responde mal 
            else:
                print("❌ RESPUESTA INCORRECTA")
                print("Has perdido el juego.")
                print(f"💸 Te llevas: ${dinero}")
                exit()

          #se mira si el jugador se quiere retirar y no perder su plataaaaaaa

            retirar = input(f"\n¿Deseas retirarte del juego? (si/no): ").lower()
            if retirar == "si":
                    print(f"\nTU DINERO GANADO FUE ${dinero}, GRACIAS POR JUGAR.")
                    exit()
        # Si se respondió bien, salimos del while True para pasar a la siguiente pregunta
        if respuesta == pregunta_actual['respuesta']:
            break
