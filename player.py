class Player:
    """
    Player class.
    
    Player has a name and a scoreboard.

    Player also check if all combinations are true. If yes, end game.

    Player also prints the scoreboard.
    """
    def __init__(self, name:str):
        self.name = name

        self._scoreboard = {}

        self._ones = False
        self._twos = False
        self._threes = False
        self._fours = False
        self._fives = False
        self._sixes = False
        self._house = False
        self._yatzy = False

    def score(self, combination_type, score):
        """
        Function counts the score and set combination to true if it is not zero.
        """
        #Set combination as a key and score as a value in scoreboard directory.
        self._scoreboard[combination_type] = score

        #Set combination type as true if score is not zero.
        if combination_type == "Ones":
            if score != 0:
                self._ones = True
        elif combination_type == "Twos":
            if score != 0:
                self._twos = True
        elif combination_type == "Threes":
            if score != 0:
                self._threes = True
        elif combination_type == "Fours":
            if score != 0:
                self._fours = True
        elif combination_type == "Fives":
            if score != 0:
                self._fives = True
        elif combination_type == "Sixes":
            if score != 0:
                self._sixes = True
        elif combination_type == "House":
            if score != 0:
                self._house = True
        elif combination_type == "Yatzy":
            if score == True:
                self._yatzy = True

    def check_scoreboard(self, player):
        """
        Function checks if scoreboard is complete.
        """
        #If player has gotten every combination, end the game.
        if (self._ones and self._twos and self._threes and self._fours and self._fives and self._sixes and 
            self._house and self._yatzy) == True:
            print(f"{player.name} has scored all combinations!")
            return True
    

    def print_current_scoreboard(self, player):
        """
        Function print out scoreboard of player.
        """
        #The player score is written out with both key and value of scoreboard directory.
        print(f"{player.name}'s score is: ")
        total_score = 0
        for key, value in self._scoreboard.items():
            print(f'{key} : {value}')
            total_score += value
        print(f"Total score is: {total_score}")

    
