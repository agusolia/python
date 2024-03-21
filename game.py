import random
words = ["python", "programacion","computadora","codigo","desarrollo","inteligencia"]
secret_word = random.choice(words)
total_car= len(secret_word)
max_fallos = 0
guessed_letters = []
print ("¡Bienvenido al juego de adivinanzas!")
print ("")
print ("Dificultades:")
print ("* Presiona F para Facil")
print ("* Presiona  M para Media")
print ("*Presiona D para Dificil")
dificultad = input(":").lower()
letters=[]
print ("Estoy pensando en una palabra. ¿Puedes adivinar cual es?")
if dificultad == "f":
    guessed_letters= ["a","e","i","o","u"]
    inicio=0
    fin=total_car
elif dificultad == "m":
    inicio=1
    fin= total_car-1 
    pri_car= secret_word [0:1]
    ult_car= secret_word [total_car-1:total_car]
    letters.append(pri_car)
else:
    inicio=0
    fin= total_car
for letter in secret_word [inicio : fin]:
    if letter in guessed_letters:
        letters.append(letter)      
    else:
        letters.append("_")
if  dificultad == "m":
    letters.append(ult_car)
word_displayed = "".join(letters)
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
    if dificultad=="m":
        letters.append(pri_car)
    for letter in secret_word [inicio : fin]:
        if letter in guessed_letters:
         letters.append(letter)      
        else:
            letters.append("_")
    if dificultad == "m":
        letters.append(ult_car)
    word_displayed = "".join(letters)
    print (f"Palabra: {word_displayed}")
    if word_displayed == secret_word:
        print (f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print (f"¡Oh no! Has alcanzado los {max_fallos} fallos")
    print (f"La palabra secreta era: {secret_word}")