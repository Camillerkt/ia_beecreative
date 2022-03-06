import random

from numpy import number

class Ia:
    def __init__(self, fileName, learningRate, theta):
        self.fileName = fileName
        self.learningRate = learningRate
        self.theta = theta

        self.imageMark = None
        self.neuronOutput = None
        self.errorValue = None
        self.entryVector = []
        self.weightVector = []

    def createEntryVector(self):
        with open(self.fileName) as file:
            file = file.read()
            for char in file:
                if char != '\n': #On retire tous les sauts de lignes
                    self.entryVector.append(char.replace('_', '0').replace('X', '1').replace('x', '1'))
            
            #On supprime le dernier élément du vecteur, qui correspond au marquage de l'image puis on convertit la liste en une matrice d'entiers
            self.imageMark = int(self.entryVector.pop())
            self.entryVector = [int(pixel) for pixel in self.entryVector]

    def createWeightVector(self):
        for pixel in self.entryVector:
            self.weightVector.append(random.uniform(0, 1/len(self.entryVector)))

    def calculatePotential(self):
        #Note : La fonction zip() combine le contenu de deux itérables ou plus
        return sum([x * w for (x, w) in zip(self.entryVector, self.weightVector)])
    
    def doSomeCalcs(self):
        #Calculer le potentiel du neurone de sortie
        self.neuronOutput = self.calculatePotential() - self.theta
        #Déduire la sortie du neurone 
        self.errorValue = self.imageMark - self.neuronOutput
    
    def spreadError(self):
        for weight_index in range(len(self.weightVector)):
            self.weightVector[weight_index] = self.weightVector[weight_index] + self.entryVector[weight_index] * self.errorValue * self.learningRate
    
    def generateNoise(self, seuil):
        alreadyUsedIndex = []
        numberOfPixelsTaken = seuil / len(self.entryVector) * 100
        for i in range(int(numberOfPixelsTaken)):
            random_index = random.randint(0,len(self.entryVector)-1)
            if random_index not in alreadyUsedIndex:
                if self.entryVector[random_index] == 1:
                    self.entryVector[random_index] = 0
                else:
                    self.entryVector[random_index] = 1
                alreadyUsedIndex.append(random_index)
            else:
                random_index = random.randint(0,len(self.entryVector)-1)
                
        return self.entryVector