import pdb
import logging

from Population import Population as Pop
from DNA import DNA as DNA

target = 0
popmax = 200
mutationRate = 0.01
bestPhrase = 'To be or not to be.'
population = Pop(bestPhrase, 0.1, 10)

allPhrases = ''
stats = 0

def setup():
    logging.getLogger('').handlers = []
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("setup done")

def mainLoop():
    # Calculate the fitness
    while population.calcFitness() == 0.0:
        pass
    
    # Generate mating pool
    population.naturalSelection()

    #Create next generation
    population.generate()

    population.evaluate()

    if population.isFinished():
        logging.debug("Finished")

    logging.debug("All done")

setup()
mainLoop()

