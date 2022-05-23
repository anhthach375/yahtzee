class ScoreCard( object ):
    """ Represents a score card for yahtzee that can compute values for each
    (unscored) combination and can track which combinations are scored. """

    # a dictionary hard-codng a map from letters (for user selection) to combo names
    # to access just the combo names, use combos.values()
    # which will be keys for the dictionaries
    # we will hard-code the lower half combo names, then use a loop for the upper
    combos:dict = { "A":"Ones", "B":"Twos", "C":"Threes", 
                    "D":"Fours", "E":"Fives", "F":"Sixes",
                    "G":"Three of a kind", "H":"Four of a kind", 
                    "I":"Full house", "J":"Small straight", "K":"Large straight",
                    "L":"Yahtzee", "M":"Chance"} 
                    # "G":"Three of a kind", "H":"Four of a kind", "I":"Full house", 
                    # "J":"Small straight", "K":"Large straight", 
                    # "L":"Yahtzee", "M":"Chance"}

    def __init__( self ):
        # keep a dictionary to track which scores are checked off
        # for example, "1s" -> False means the combo has not been used
        #              "3s" -> True means the combo has been used
        self.__checked = {}

        # keep a dictionary to track the combinations' scores
        self.__comboScores:dict = {}

        # now create the initial entries for the dictionaries
        #    False entries in the checked dictionary
        #    -1 entries in the comboScores
        for comboName in ScoreCard.combos.values():
            # create an entry that maps to False for the checked
            self.__checked[comboName] = False
            # create an entry that maps to -1 for the comboScores
            self.__comboScores[comboName] = -1
    
    def checkedOff( self, comboName:str ) -> bool:
        """ Return true if the combo name (e.g., "1s", "Full house") has
        been scored/checked off. """
        # STUB PLACEHOLDER
        if self.__checked[comboName] == True:
            return True
        return False
    
    def checkOff( self, comboName:str ) -> None:
        """ Check off this combo name (e.g., "1s", "Full house") with its current score. """
        # STUB PLACEHOLDER
        self.__checked[comboName] = True

    def numRemainingCombos( self ) -> int:
        """ Return the number of combos not yet checked off."""    

        # variable to accumulate the count into
        numRemaining:int = 0

        # iterate over the combo names
        for comboName in ScoreCard.combos.values():
            # if a combo is not checked off
            if not self.checkedOff(comboName):
                # update the total remaining
                numRemaining += 1
        # return the count
        return numRemaining

    def setScore( self, comboName:str, score:int ) -> None:
        """ If the combo has not yet been checked off,
        stores the score as the value for the combo. """
        # STUB PLACEHOLDER
        # if self.checkedOff(comboName) == False:
        if self.__checked[comboName] == False:
            self.__comboScores[comboName] = score
    
    def getScore( self, comboName:str ) -> int:
        """ Returns the combo's score (does not matter if the combo is checked off or not). 
        If the comboName is not in the dictionary, returns -1 as a flag. """
        # STUB PLACEHOLDER
        # if comboName not in self.__comboScores:
        if comboName not in self.__comboScores:
        # if self.checkedOff(comboName) == True:
            return -1
        else:
            return self.__comboScores[comboName]

    def totalScore( self ) -> int:
        """ Compute the total score (the total of all checked off combos). """
        # STUB PLACEHOLDER
        totalScore:int = 0
        for comboName in ScoreCard.combos.values():
            totalScore += self.__comboScores[comboName]
        return totalScore
        
    def scoreDice( self, dice:list ) -> None:
        """ Given the dice list, score the upper and lower halves. """
        self.scoreUpperHalf(dice)
        self.scoreLowerHalf(dice)

    def diceToInList(self, dice:list) -> list:
        # create an empty list
        intList:list = []
        # get the int value of each singleDice in the dice list
        for singleDice in dice:
        # append singleDice to the empty list 
            intList.append(singleDice.getValue())
        return intList

    def scoreUpperHalf( self, dice:list ) -> None:
        """ Given the dice list, score the upper half of the scorecard
        and enter scores for "1s", "2s", ..."6s" unless it's already checked off. """
        # STUB PLACEHOLDER
        # invoke diceToInList to convert all element in the dice list to int value
        UpperHalf:list = self.diceToInList(dice)
        # create a list that takes 6 string elements
        comboist:list = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
        for i in range(len(comboist)):
            count:int = UpperHalf.count(i+1) * (i+1)
            self.setScore(comboist[i], count)
        
    def scoreLowerHalf( self, dice:list ) -> None:
        """ Given the dice list score the lower half of the scorecard
        and enter scores for combos like "Full house" or "Small straight" 
        unless it's already checked off. """       
        self.scoreThreeOfAKind(dice)     
        self.scoreFourOfAKind(dice)
        self.scoreFullHouse(dice)
        self.scoreSmallStraight(dice)
        self.scoreLargeStraight(dice)
        self.scoreYahtzee(dice)
        self.scoreChance(dice)
        self.scoreThreeOfAKind(dice)

    def scoreThreeOfAKind( self, dice:list ) -> None:
        """ Given the dice list, score three of a kind. """
        # STUB PLACEHOLDER
        # invoke diceToInList to convert all element in the dice list to int value
        newThreeKind:list = self.diceToInList(dice)
        # check if "Three of a kind" has been checked off or not
        if not self.__checked["Three of a kind"]:
            self.setScore("Three of a kind", 0)
            for value in range(1,7):
        # create a variable named 'occur' which is count the number of times that number from 1-6 appear in the list 
                occur:int = newThreeKind.count(value)
        # if the occur is greater than 3, then update the score
                if occur >= 3:
                    self.setScore("Three of a kind", sum(newThreeKind))
               
                
    def scoreFourOfAKind( self, dice:list ) -> None:
        """ Given the dice list, score four of a kind. """
        # STUB PLACEHOLDER

        newFourKind:list = self.diceToInList(dice)
        if not self.__checked["Four of a kind"]:
            self.setScore("Four of a kind", 0)
            for value in range(1,7):
                occur:int = newFourKind.count(value)
                if occur >= 4:
                    self.setScore("Four of a kind", sum(newFourKind))
        

    def scoreFullHouse( self, dice:list ) -> None:
        """ Given the dice list, score full house (2 of a kind + 3 of a kind). """
        # STUB PLACEHOLDER
        newFullHouse:list = self.diceToInList(dice)
        # sort the order of the list (from smallest to biggest)
        newFullHouse.sort()
        # check if "Full house" has been checked off or not
        if not self.__checked["Full house"]:
            self.setScore("Full house", 0)
        # exactly 2 of one value, exactly 3 of another value
            if (newFullHouse.count(newFullHouse[0]) == 2 and newFullHouse.count(newFullHouse[4]) == 3) or (newFullHouse.count(newFullHouse[0]) == 3 and newFullHouse.count(newFullHouse[4]) == 2):
                self.setScore("Full house", 25)
    
    def containsAll(self, values:list, searchElts:list ) -> bool:
    # if every element of the searchElts list appears in the values list.
    # set the inital to be 0
        total:int = 0
        for value in searchElts:
            if value in values:
                total += 1
    # if the total equals to the len of searchElts, it means all values of searchElts are in values
        if total == len(searchElts):
            return True
        return False
            
    def scoreSmallStraight( self, dice:list ) -> None:
        """ Given the dice list, score small straight (4 in order). """
        # STUB PLACEHOLDER
        newSmall:list = self.diceToInList(dice)
        # check if "Small straight" has been checked off or not
        if not self.__checked["Small straight"]:
            self.setScore("Small straight", 0)
        # there are only three cases for the small straight
            if self.containsAll(newSmall, [1,2,3,4]) == True or self.containsAll(newSmall, [2,3,4,5]) == True or self.containsAll(newSmall, [3,4,5,6]):
                self.setScore("Small straight", 30)
    

    def scoreLargeStraight( self, dice:list ) -> None:
        """ Given the dice list, score large straight (5 in order). """
        # STUB PLACEHOLDER
        newLarge:list = self.diceToInList(dice)
        if not self.__checked["Large straight"]:
            self.setScore("Large straight", 0)
        # there are only two cases for the small straight
            if self.containsAll(newLarge, [1,2,3,4,5]) == True or self.containsAll(newLarge, [2,3,4,5,6]) == True:
                self.setScore("Large straight", 40)

    def scoreYahtzee( self, dice:list ) -> None:
        """ Given the dice list, score Yahtzee (all 5 the same). """
        # STUB PLACEHOLDER
        newYahtzee:list = self.diceToInList(dice)
        # check if "Yahtzee" has been checked off or not
        if not self.__checked["Yahtzee"]:
            self.setScore("Yahtzee", 0)
            for value in newYahtzee:
                occur:int = newYahtzee.count(value)
        # if the occur is 5, then update the score
                if occur == 5:
                    self.setScore("Yahtzee", 50)

    def scoreChance( self, dice:list ) -> None:
        """ Given the dice list, score chance (sum of values). """
        # STUB PLACEHOLDER
        newChance:list = self.diceToInList(dice)
        self.setScore("Chance", sum(newChance))
    
    def toString( self, onlyChecked:bool ) -> str:
        """ Return a string representation of the score card. Each combo will
        be on its own line with the selector item in front. Scores that are
        checked off will be surrounded by asterisks, as in
        (A) Ones: *3*
        (B) Twos: 4
        (C) Threes: 0
        ...
        If onlyChecked is True, non checked off values will be blank; 
        otherwise, they will show current value (probably from most recent
        dice rolls).
        """
        # a string to build up the description
        description:str = "Score Card\n------------\n"

        # iterate over the combo items ("A", "B", ...)
        for item in ScoreCard.combos:
            # the combo name is in the dictionary ("Ones", "Twos", ...)
            comboName:str = ScoreCard.combos[item]

            # add the combo info, as in "(A) Ones: "
            description += f"({item}) {comboName}: "

            # find the current score
            comboScore:int = self.getScore( comboName )

            # if it is a checked off score, surround it with asterisks
            if self.checkedOff( comboName ):
                description += f"*{comboScore}*\n"
            elif not onlyChecked:
                description += f"{comboScore}\n"
            else:
                description += "\n"
        
        # once we've made it through all the combos, return the description
        return description

    def __str__( self ) -> str:
        """ Return a string representation of the score card. Each combo will
        be on its own line with the selector item in front. Scores that are
        checked off will be surrounded by asterisks, and all others will be blank,
        as in
        (A) Ones: *3*
        (B) Twos: 
        (C) Threes: *0*
        ...
        """
        return self.toString( True )

