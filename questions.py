import random
words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]

# AGREGADO: diccionario de categorías
categories = {
    "programación": [
        "python",
        "programa",
        "variable",
        "funcion",
        "bucle",
        "cadena",
        "entero",
        "lista",
    ],
    "animales": [
        "perro",
        "gato",
        "tortuga",
        "caballo",
    ],
    "frutas": [
        "manzana",
        "banana",
        "pera",
        "naranja",
    ]
}

# AGREGADO: mostrar categorías y elegir una
print("Categorías disponibles:")
for nombre in categories:
    print("-", nombre)
categoria_elegida = input("Elegí una categoría: ")

# AGREGADO: seleccionar la lista de palabras según la categoría elegida
if categoria_elegida in categories:
    words = categories[categoria_elegida]

word = random.choice(words)
guessed = []
attempts = 6
score = 0  # <-- AGREGADO

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        score += 6  # <-- AGREGADO
        print("¡Ganaste!")
        print(f"Puntaje final: {score}")  # <-- AGREGADO
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")

    # Validar entrada: exactamente un carácter y que sea letra
    if len(letter) != 1 or not letter.isalpha():
       print("Entrada no válida")
       print()
       continue
    
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        score -= 1  # <-- AGREGADO
        print("Esa letra no está en la palabra.")
    
    print()
else:
    score = 0  # <-- AGREGADO
    print(f"¡Perdiste! La palabra era: {word}")
    print(f"Puntaje final: {score}")  # <-- AGREGADO