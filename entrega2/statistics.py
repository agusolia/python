def constructor(names, goals, goals_avoided, assists): 

    #funcion que crea y retorna un diccionario de tuplas, donde la clave es el nombre del jugador

    names = names.replace(",", "")
    names = names.split()
    players = {}
    for name, go, ga, a in zip(names, goals, goals_avoided, assists): 
        players[name.upper()] = (go, ga, a) 
    return players

def scorer (players): 

    # funcion que devuelve el nombre y la cantidad de goles que hizo el maximo goleador
    # max va a recorrer el iterable players, usando la funcion lambda

    scorerName, scorerGoals = max(players.items(), key= lambda x: x[1][0])
    return scorerName, scorerGoals[0]    #retorna el nombre y los goles realizados

def calculateValue (player): #funcion que calcula el puntaje
    stats = player[1]
    score = stats[0]*1.5 + stats[1]*1.25 + stats[2]
    return (player[0], score)

def calculateList (players): #funcion que crea la lista de puntajes
    list_scores = list(map(calculateValue, players.items()))
    return list_scores

def mIP (players): #funcion que devuelve el nombre del jugador mas influyente
    scores_list = calculateList (players) 
    mip = max (scores_list , key = lambda x: x[1]) #devuelve una tupla
    return mip [0]


def average (goals): 
    total = sum (goals) #suma todos los goles realizados usando la funcion sum() 
    return total/25

def scorerAverage (players):

    #llama a la función scorer, la cual calcula el maximo goleador

    scorer_player = scorer (players) #recibe una tupla con el nombre y la cantidad de goles del maximo goleador
    return scorer_player[1]/25 #retorna el promedio por partido