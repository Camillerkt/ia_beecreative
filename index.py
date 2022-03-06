from IA import *

import numpy as np
import matplotlib.pyplot as plt

def createRandomWeights():
    ia = Ia('files/un.txt', 0.01, 0.5)
    ia.createEntryVector()
    ia.createWeightVector()

    return ia.weightVector

#On génère un vecteur de poids aléatoire
weights = createRandomWeights()

def getErrorValue(fileName, learningRate, theta):
    global weights

    #Les étapes pour modifier le vecteurs de poids et retourner la valeur de l'erreur
    ia = Ia(fileName, learningRate, theta)
    ia.createEntryVector()
    ia.weightVector = weights
    ia.doSomeCalcs()
    ia.spreadError()
    weights = ia.weightVector

    return ia.errorValue

totalError = 0.1
listOfTotalError = []

while totalError > 0:
    if random.random() == 0 :
        error0 = getErrorValue('files/un.txt', 0.01, 0.5)
        error1 = getErrorValue('files/zero.txt', 0.01, 0.5)
    else :
        error1 = getErrorValue('files/zero.txt', 0.01, 0.5)
        error0 = getErrorValue('files/un.txt', 0.01, 0.5)
    
    totalError = abs(error0) + abs(error1)

    listOfTotalError.append(totalError)


#Courbe

x = np.array(range(len(listOfTotalError)))
y = np.array(listOfTotalError)
plt.plot(x, y)

plt.show()