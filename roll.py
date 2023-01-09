import random

class Roll:
    def __init__(self):
        """
        Create two lists. One for dice to roll and one for dice to hold.
        """
        self._dice_list = []
        self._held_dice = []

    def roll_dice(self):
        """
        Function roll all five dice.
        """
        #Clear held dice list.
        self._held_dice.clear()

        #Randomize numbers between 1 to 6 five times.
        self._dice_list = [random.randint(1,6) for dice in range (0,5)]

        #Print result. Return dice list.
        print(f'You rolled {self._dice_list}')
        return self._dice_list

    def hold_dice(self):
        """
        Function hold dice that player don't want to reroll.
        """
        #Player input which dice they want to hold.
        held = input('Which die/dice do you want to hold (comma seperated)? ')

        split = held.split(',')
    
        #If no dice is selected then return the full list
        if held == '':
            return self._dice_list

        #Convert from string to integer
        split_int = [int(item) for item in split]

        #Add the dice to a seperate list.
        for die in split_int:
            self._held_dice.append(die)

        #Remove the kept dice from the roll list.
        for value in split_int:
            if value in self._dice_list:
                self._dice_list.remove(value)

        #Return the dice list
        return self._dice_list

    def reroll_dice(self, dice_list):
        """
        Rolls the remaining dice that are not kept
        """
        #Randomize number between 1 to 6 the amount of time as the length of the dice list
        if len(dice_list) == 0:
            return
        else:
            self._dice_list = [random.randint(1,6) for die in range (0,(len(self._dice_list)))]

            #Return dice list
            print(f'You rolled {self._dice_list}')
            return self._dice_list

    def forced_dice_hold(self, dice_list):
        """
        Add the rest of the dice to the held list
        """
        for dice in dice_list:
            self._held_dice.append(dice)
        return self._held_dice