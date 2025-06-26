##
# @file        DTM-Sim.py
# @author      Linda Nguyen
# @brief       Simulation of a deterministic turing machine
# @details     This script generates a set of 2D points, calculates Manhattan distances,
#              and identifies the m closest point-pairs using a distance-based sorting algorithm.
# @date        2025-06-25


#6-tuple that defines the DTM
mInputSymbols = {} #sigma
mAllSymbols = {} #gamma
mStates = {}
mDirection = { -1, 1 } #left = -1, right = +1: this is contained within the transition table
mBlankSymbol = 'b'

#Transition table
mTransitions = {}

#starting state
mStartState = 'q0'
mHaltStates = {}
mTape = ['b'] * 20 #inital tape containing 100 blank symbols
mTapeHistory = []

##--------------------------------------------------------------------------------------------

##
# @brief Initialize global variables 
#
# Set the global variables containing the 6-tuple for the DTM. 
# THIS DTM IS FOR PART A
#
# @param input - N/A
# @return N/A
def initializeDTMForPartA():

    #get access to the global variables
    global mInputSymbols
    global mAllSymbols
    global mStates
    global mTransitions
    global mHaltStates

    #6-tuple that defines the DTM
    mInputSymbols = { 0, 1 } #sigma
    mAllSymbols = { '0', '1', 'b' } #gamma
    mStates = { "q0", "q1", "q2", "q3", "qY", "qN" }

    #Transition table
    mTransitions = {
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

    mHaltStates = { "qY", "qN" }


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
        mTape[initialIndex] =  char
        initialIndex += 1


##
# @brief Performs the transitions on the tape
#
# Uses the transition table to modify the tape and transition through states until it
# reaches a halt state
#
# @param input - N/A
# @return N/A
def doTransitions():

    numTransitions = 0
    currentState = mStartState
    headIndex = 10 #start at the initial index we set in the createTape function

    while currentState not in mHaltStates:
        symbol = mTape[headIndex]

        #get the next state, symbol to write to tape, and where to move tape head
        transitionResult = mTransitions[currentState][symbol]

        #put the transition results into individual variables for readability
        nextState = transitionResult[0]
        writeSymbol = transitionResult[1]
        moveHead = transitionResult[2]

        #update the state, head index, and write symbol to tape
        currentState = nextState
        mTape[headIndex] = writeSymbol
        headIndex += moveHead

        #print the state of the tape and increment numTransitions
        print(numTransitions, ". ", mTape, sep='')
        numTransitions += 1
        mTapeHistory.append(mTape)

    #if number of transitions is greater than 30, write the transitions to a file
    if numTransitions > 29:
        with open("dtm_output.txt", "w") as f:
            for trans in mTapeHistory:
                f.write(''.join(trans))


# Defining main function
def main():
    initializeDTMForPartA()
    createTape("10100")
    doTransitions()
    

# Using the special variable 
# __name__
if __name__=="__main__":
    main()