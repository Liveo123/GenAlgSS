import pdb
import logging

import numpy as np
import pandas as pd
from DNA import DNA as DNA

class Population(object):

    def __init__(self, targetPhrase, mutationRate, num):
        
        self.finished = False
        self.mutationRate = mutationRate
        self.targetPhrase = targetPhrase

        # Create blank population
        self.population = pd.Series('' for _ in range(num))      #np.array([])
       
        # Loop through creating num phrases from random letters 
        # the same size as the targetPhrase
        
        for i in range (0, num):
            # Add test gene value
            #if i == num - 1:
            #   self.population[i] = DNA('To be or not to be.')  
            #   #np.append(self.population, DNA('To be or not to be.'))
            #lse:
            self.population[i] = DNA(len(targetPhrase))
                #self.population = np.append(self.population, DNA(len(targetPhrase)))
            self.population[i].outputGene()
        
        logging.debug("Population Constructor finished")
    
#   Description: Goes through all of the DNA in the population and
#                runs a method to calculate the fitness.  It adds all
#                of these together for a total population fitness.
    
    def calcFitness(self):
        totalFitness = 0.0
        for gn in self.population:
            totalFitness += gn.fitness(self.targetPhrase) 

        logging.debug("Total fitness = %f" % totalFitness)
        return totalFitness

    def naturalSelection(self):
       logging.debug("Natural Selection finished")

    def generate(self):
       logging.debug ("Generate finished")

    def evaluate(self):
        logging.debug("evaluate finished")

    def isFinished(self):
        return self.finished

#   Description: Converts a number from it's range yStart to yFin
#                to a different range, xStart to xFin.
#                e.g. 0 to 1 Converted to 0 to 100

    def mappy(self, theBugger, xStart, xFin, yStart, yFin):
        xDiff = xFin - xStart
        yDiff = yFin - yStart
        return ((xDiff/yDiff)*theBugger)+xStart
