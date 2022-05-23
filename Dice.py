import random

class Dice(object):
    """ Represents a single 6-sided dice that can be rolled 
    to a value 1,2,...,6. Can be a "keeper" where the value
    does not change if a roll is attempted. """

    def __init__(self):
        """ Constructor creates a new dice that has
        not been rolled and is not a keeper. """
        # STUB PLACEHOLDER
        self.__value:int = -1
        self.__keeper:bool = False
    
    def getValue( self ) -> int:
        """ Get the value of this dice (e.g., what number is showing). 
        -1 means the dice has not yet been rolled. """
        # STUB PLACEHOLDER
        return self.__value 

    def isKeeper( self ) -> bool:
        """ Returns True if the dice is a keeper (cannot be rolled). """
        # STUB PLACEHOLDER
        # if self.__keeper == True:
        return self.__keeper

    def keep( self ) -> None:
        """ Keep this dice so its value cannot change. """
        # STUB PLACEHOLDER
        self.__keeper = True

    def release( self ) -> None:
        """ Release this dice so it can be rolled. """
        # STUB PLACEHOLDER
        self.__keeper = False
        
    def roll( self ) -> None:
        """ Try to roll the dice; if it's not a keeper, roll and update the value. """
        # STUB PLACEHOLDER
        if not self.__keeper:
        # if not self.isKeeper():
            self.__value = random.randint(1,6)


    def __str__( self ) -> str:
        """ Returns a string representation of this dice with the value; 
        if it is a keeper, enclose it in asterisks. """
        if self.isKeeper():
            return f" *{self.getValue()}* "
        else:
            return f" {self.getValue()} "
