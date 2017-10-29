# 6.00 Problem Set 8
#
# Name: SOLUTIONS
#
#

import numpy
import random
import pylab
from ps7b_sol import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numViruses, maxPop, maxBirthProb, clearProb,
                               resistances, mutProb, numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a list of drugs that each ResistantVirus is resistant to
                 (a list of strings, e.g., ['guttagonol'])
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    """

    finalResults = {}
    delays = [300, 150, 75, 0]
    
    for delay in delays:
        finalNumViruses = []
        for n in xrange(0, numTrials):
            total = runDrugSimulation(numViruses, maxPop, maxBirthProb,
                                      clearProb, resistances, mutProb, delay,
                                      delay + 150)
                                                 
            finalNumViruses.append(total[-1])

        finalResults[delay] = finalNumViruses

    plotNum = 1
    for n in delays:
        pylab.subplot(2, 2, plotNum)
        pylab.title("delay: " + str(n))
        pylab.xlabel("final virus counts")
        pylab.ylabel("# trials")
        pylab.hist(finalResults[n], bins=12, range=(0, 600)) # each bin of size 50
        plotNum += 1

    pylab.show()


def runDrugSimulation (numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numStepsBeforeDrugApplied, totalNumSteps):
    """ Helper function for doing one actual simulation run with drug applied """
    
    viruses = []

    for i in xrange(0, numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances,
                                      mutProb))

    patient = TreatedPatient(viruses, maxPop)

    numVirusesEachStep = []
    numResistantVirusesEachStep = []
    for i in xrange(0, totalNumSteps):
        if i == numStepsBeforeDrugApplied:
            patient.addPrescription("guttagonol")
        numVirusesEachStep.append(patient.update())

    return numVirusesEachStep
