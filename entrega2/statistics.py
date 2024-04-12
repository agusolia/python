def constructor(names, goals, goals_avoided, assists):
    names = names.replace(",", "")
    names = names.split()
    players = {}
    for name, go, ga, a in zip(names, goals, goals_avoided, assists):
        players[name.upper()] = (go, ga, a) 
    return players

def scorer (players):
    scorerName, scorerGoals = max(players.items(), key= lambda x: x[1][0])
    return scorerName, scorerGoals[0]

def calculateValue (player):
    stats = player[1]
    score = stats[0]*1.5 + stats[1]*1.25 + stats[2]
    return (player[0], score)

def calculateList (players):
    list_scores = list(map(calculateValue, players.items()))
    return list_scores

def mIP (players):
    scores_list = calculateList (players)
    mip = max (scores_list , key = lambda x: x[1])
    return mip [0]

def average (goals):
    total = sum (goals)
    return total/25

def scorerAverage (players):
    scorer_player = scorer (players) #recibe una tupla con el nombre y la cantidad de goles del maximo goleador
    return scorer_player[1]/25 #retorna el promedio por partido