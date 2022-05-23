from ScoreCard import ScoreCard
from Turn import Turn

class YahtzeeGame( object ):
    """ Plays a single-player versio of Yahtzee, 
    a game wiith 5 dice and different combinations to score. """

    def __init__( self ):
        """ Creates a new Yahtzee game that will track scores and 
        allow the user to play a turn until all combos have been checked off. """

        # initialize the scorer, main state for the game
        self.__scoreCard = ScoreCard()

        # initialize the turn, which we will manage the logic for a turn
        self.__turn = Turn()

    def playGame( self ) -> int:

       """ Play Yahtzee! This will prompt the player to play one turn

       as long as there are combos left. When the game ends, returns

       the final score. """

       print( "Welcome to Yahtzee!" )

       # while there are combos not yet checked off

       while self.__scoreCard.numRemainingCombos() > 0:

           # play a turn

           self.playTurn()
       # final score

       finalScore:int = self.__scoreCard.totalScore()

       print( f"Final score: {finalScore}")

       # return the final score

       return finalScore

    
    def playTurn( self ) -> None:
        """ Play a turn of Yahtzee. """

        print( f"Start the turn!")

        # reset the turn (in case this isn't the first)
        self.__turn.reset()

        # roll the dice to start
        self.__turn.rollDice()

        # the user might decide to stop rolling early, so we will
        # use this boolean to track that
        # userWantsToRoll:bool = True

        # while there are rolls remaining and the user wants to roll
        while self.__turn.getNumRemainingRolls() > 0 and self.promptDiceSelection():
            # now roll the dice
            self.__turn.rollDice()
        
        print( f"Ready to score: {self.__turn}" )

        # score the turn
        self.scoreTurn()

        # print the score cord
        print( self.__scoreCard )
    
    def scoreTurn( self ) -> None:
        """ Prompt the user to choose which combo to check off. """

        # ask the score card to compute possible scores for the dice
        self.__scoreCard.scoreDice( self.__turn.getDice() )

        # print the score card with all possible values
        print( self.__scoreCard.toString( False ) )

        # and ask the user to select which combo to use
        userSelection = input( "Which will you check off? [A/B/C/...] ")
        
        # if they want to quit
        if userSelection.lower() == "q":
            exit()
            
        # get the combo name associated to the selection by looking it up in the "class" dictionary
        comboName:str = ScoreCard.combos[userSelection.upper()]

        # if the combo is already checked off
        if self.__scoreCard.checkedOff( comboName ):
            # prompt them again
            self.scoreTurn()
        else:
            # ask the score card to check off that combo
            self.__scoreCard.checkOff( comboName )

    def promptDiceSelection( self ) -> bool:
        """ Prompt the user to choose which dice to keep or
        decide if they want to stop rolling. Returns False if
        and only if the user decides to stop rolling. """

        # and print out the current dice
        # the Turn object will print [ x x x x x x ]
        print( self.__turn )
        labels:list = ["a","b","c","d","e"]
        # to label the dice, print a line that has the labels
        print(f"  {'   '.join(labels)}")
        userSelection:str = input( "Which dice to keep? [(N)one/(S)top/a,c,d,...] " )
        
        # if they want to quit
        if userSelection.lower() == "q":
            exit()
        # if they want to stop rolling
        elif userSelection.lower() == "s":
            return False
        # or they want to keep no additional dice
        elif userSelection.lower() == "n" or userSelection == "":
            return True
        # otherwise, unpack their selection
        else:
            # split their response apart by commas
            splitSelection:list = userSelection.split( "," )

            # for each selected dice value
            for selection in splitSelection:
                # find the index of that label, which corresponds to the dice index,
                # by using the list method index
                diceIndex:int = labels.index( selection.strip() )

                # tell the turn to keep that dice
                self.__turn.keep( diceIndex )

            return True

if __name__ == "__main__":
    # create a new Yahtzee game
    game:YahtzeeGame = YahtzeeGame()

    # play the game
    game.playGame()