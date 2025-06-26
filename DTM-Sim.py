##
# @file        DTM-Sim.py
# @author      Linda Nguyen
# @brief       Simulation of a deterministic turing machine
# @details     This script generates a set of 2D points, calculates Manhattan distances,
#              and identifies the m closest point-pairs using a distance-based sorting algorithm.
# @date        2025-06-25


#6-tuple that defines the DTM
inputSymbols = { 0, 1 } #sigma
allSymbols = { '0', '1', 'b' } #gamma
states = { "q0", "q1", "q2", "q3", "qY", "qN" }
direction = { -1, 1 } #left = -1, right = +1: this is contained within the transition table
blankSymbol = 'b'

#Transition table
transitions = {
    'q0': {
        '0': ('q0', '0', +1),
        '1': ('q0', '1', +1),
        'b': ('q1', 'b', -1)
    },
    'q1': {
        '0': ('q2', 'b', -1),
        '1': ('q3', 'b', -1),
        'b': ('qN', 'b', -1)
    },
    'q2': {
        '0': ('qY', 'b', -1),
        '1': ('qN', 'b', -1),
        'b': ('qN', 'b', -1)
    },
    'q3': {
        '0': ('qN', 'b', -1),
        '1': ('qN', 'b', -1),
        'b': ('qN', 'b', -1)
    }
}

#starting state
startState = 'q0'
haltStates = { "qY", "qN" }
tape = ['b'] * 20 #inital tape containing 100 blank symbols
tapeHistory = []

##--------------------------------------------------------------------------------------------

##
# @brief Initialize the tape
#
# Initializes the tape by placing the input string somewhere in the middle of 
# the tape 
#
# @param input - a string that will get put through the turing machine
# @return N/A
def createTape( input ):

    #set the initial index to 50 so we place the input somewhere in the middle of the tape
    initialIndex = 10

    #put the input in the tape starting in the middle
    for char in input:
        tape[initialIndex] =  char
        initialIndex += 1



def doTransitions():

    numTransitions = 0
    currentState = startState
    headIndex = 10 #start at the initial index we set in the createTape function

    while currentState not in haltStates:
        symbol = tape[headIndex]

        #get the next state, symbol to write to tape, and where to move tape head
        transitionResult = transitions[currentState][symbol]

        #put the transition results into individual variables for readability
        nextState = transitionResult[0]
        writeSymbol = transitionResult[1]
        moveHead = transitionResult[2]

        #update the state, head index, and write symbol to tape
        currentState = nextState
        tape[headIndex] = writeSymbol
        headIndex += moveHead

        #print the state of the tape and increment numTransitions
        print(numTransitions, ". ", tape, sep='')
        numTransitions += 1
        tapeHistory.append(tape)

    #if number of transitions is greater than 30, write the transitions to a file
    if numTransitions > 29:
        with open("dtm_output.txt", "w") as f:
            for trans in tapeHistory:
                f.write(''.join(trans))







# Defining main function
def main():
    createTape("10100")
    doTransitions()
    


# Using the special variable 
# __name__
if __name__=="__main__":
    main()