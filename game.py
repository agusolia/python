import random
words = ["python", "programacion","computadora","codigo","desarrollo","inteligencia"]
secret_word = random.choice(words)
max_fallos = 0
guessed_letters = []
print ("¡Bienvenido al juego de adivinanzas!")
print ("Estoy pensando en una palabra. ¿Puedes adivinar cual es?")
word_displayed = "_"* len(secret_word)
print (f"Palabra: {word_displayed}")
while max_fallos <=9 :
    letter = input ("Ingresa una letra: ").lower()
    if letter in guessed_letters:
        print ("Ya has intentado con esa letra. Intenta con otra.")
        max_fallos +=1
        continue
    if letter == (""):
        print ("Valor inválido. Ingrese otro. ")
        max_fallos += 1
        continue
    elif letter in secret_word:
        print ("¡Bien hecho! La letra esta en la palabra.")
    else:
        print ("Lo siento, la letra no esta en la palabra")
        max_fallos+= 1
    guessed_letters.append(letter)
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print (f"Palabra: {word_displayed}")
    if word_displayed == secret_word:
        print (f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print (f"¡Oh no! Has alcanzado los {max_fallos} fallos")
    print (f"La palabra secreta era: {secret_word}")