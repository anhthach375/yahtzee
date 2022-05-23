from Dice import Dice

class Turn( object ):
    """ Represents a Turn of Yahtzee, where a player has 5 dice they can roll 
    up to 3 times. After each roll, they can choose to keep some/all of the dice. """

    def __init__( self ):
        """ Constructor creates a new Turn object that tracks dice and rolls remaining. """
        # instance property to track the 5 dice
        self.__dice:list = []
        
        # create the dice
        for i in range(5):
            # construct a new Dice object and append it to the list of dice
            self.__dice.append(Dice())
        # instance property to track the number of rolls left
        # initialize to 3
        self.__numRemainingRolls:int = 3

    
    def getDice( self ) -> list:
        """ Get a list of the dice. """

        # note: better practice would be to make a copy, so that the list and dice
        #       could not be unexpectedly modified; 
        #       for this course, it's okay just return the reference to the dice list
        return self.__dice
    
    def getDiceAt( self, index:int ) -> Dice:
        """ Get the (single) dice at the index. """

        # note: better practice would be to make a copy, so that the dice
        #       could not be unexpectedly modified; 
        #       for this course, it's okay just return the reference to the dice 
        return self.__dice[index]

    def getNumRemainingRolls( self ) -> int:
        """ Get the number of remaining rolls for this turn. """
        # STUB PLACEHOLDER
        return self.__numRemainingRolls

    def reset( self ) -> None:
        """ Reset the turn so there are 3 rolls remaining and all dice
        are released. """
        # STUB PLACEHOLDER
        self.__numRemainingRolls = 3
        for singleDice in self.__dice:
            singleDice.release()

    def keep( self, diceIndex: int ) -> None:
        """ Set the dice at the diceIndex to be a keeper. Assumes 
        we start counting at 0, so that we have diceIndex valued at 0,1,2,3,4. """
        # STUB PLACEHOLDER
        self.__dice[diceIndex].keep()

    def release( self, diceIndex: int ) -> None:
        """ Release the dice at the diceIndex so it can be rolled. Assumes 
        we start counting at 0, so that we have diceIndex valued at 0,1,2,3,4. """
        # STUB PLACEHOLDER
        self.__dice[diceIndex].release()

    def rollDice( self ) -> None:
        """ Roll the dice if there are rolls remaining; 
        if any are keepers, they will not change value.
        Updates the number of rolls remaining accordingly. """
        # STUB PLACEHOLDER
        # interate over the dice
        if self.__numRemainingRolls in range(1,4):
            for singleDice in self.__dice:
        # ask each dice to roll:
        # if any are keepers, they will not change value
                if singleDice.isKeeper() == True:
                    singleDice = singleDice
        # if not, roll
                singleDice.roll()
        # Updates the number of rolls remaining accordingly
            self.__numRemainingRolls -= 1


    def __str__( self ) -> str:
        """ Return a string representation of this turn. """

        # build up the description
        description:str = " "

        # for each index of the dice list
        for i in range(5):
            # format the dice with the label (one more than the index)
            description += f"{self.getDiceAt(i)} "

        return f"[{description}] with {self.getNumRemainingRolls()} rolls remaining."

