import pdb
import logging
import numpy as np


class DNA(object):
    genes = '' 

    def __init__(self, geneData):

        # Two options here.  If an int was passed, this is the DNA length, so 
        # create the DNA with this number of genes. Do this by creating a string 
        # of random letters.  If a string was passed, copy it straight into 
        # the data structure.

        if isinstance(geneData, int):
            # Create a single DNA element by building it from random characters
            for i in range(0, geneData):
                self.genes += unichr(np.random.randint(32,128))
        else:
            self.genes = geneData

        self.fitnessScore = 0        # The fitness of the DNA
        self.length = len(self.genes)

#   Description: Calculate the fitness score by comparing each character in the DNA
#                and each character in the target phrase.  Each time a character
#                matches, add one to the score.  Divide the score by the length of
#                the phrase to get a final score.

    def fitness(self, targetPhrase):
        try:
            # Check that the phrase and the gene are the same size
            if not len(targetPhrase)==self.length: raise AssertionError
            
            score = 0
            for i in range(0, self.length-1):
                if(self.genes[i]==targetPhrase[i]):
                    score += 1
            
            self.fitnessScore = (float)(score)/(float)(len(targetPhrase)-1)
        
        except AssertionError:
            print "Gene is different size than passed target phrase in DNA fitness method."

        return self.fitnessScore


    # Returns the number of characters in the gene
    def getLength(self):
        return self.length

    # Debug method to set the DNA to prespecified value
    def setDNAValue(self, geneValues):
        self.genes = geneValues
        print 'Genes set to %s' % geneValues

    def outputGene (self):
        print(self.genes)

