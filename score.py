class Score:
    def __init__(self):
        pass

    def ones(self, dice_list):
        """
        Function checks ones.
        -- Update result
        -- Return result
        """
        result = 0
        for index, number in enumerate(dice_list):
            if number == 1:
                result +=1
        return result

    def twos(self, dice_list):
        """
        Function checks twos.
        -- Update result
        -- Return result
        """
        result = 0
        for index, number in enumerate(dice_list):
            if number == 2:
                result +=2
        return result

    
    def threes(self, dice_list):
        """
        Function checks threes.
        -- Update result
        -- Return result
        """
        result = 0
        for index, number in enumerate(dice_list):
            if number == 3:
                result +=3
        return result

    def fours(self, dice_list):
        """
        Function checks fours.
        -- Update result
        -- Return result
        """
        result = 0
        for index, number in enumerate(dice_list):
            if number == 4:
                result +=4
        return result

    def fives(self, dice_list):
        """
        Function checks fives.
        -- Update result
        -- Return result
        """
        result = 0
        for index, number in enumerate(dice_list):
            if number == 5:
                result +=5
        return result

    def sixes(self, dice_list):
        """
        Function checks sixes.
        -- Update result
        -- Return result
        """
        result = 0
        for index, number in enumerate(dice_list):
            if number == 6:
                result +=6
        return result

    def house(self, dice_list):
        """
        Function checks house.
        -- Update result
        -- Return result
        """
        dice_list.sort()
        result = 0
        if (dice_list[0] == dice_list[1] == dice_list[2] and dice_list[3] == dice_list[4]
            or dice_list[0] == dice_list[1] and dice_list[2] == dice_list[3] == dice_list[4]):
            for die in dice_list:
                result += die
            return result
        return False

    def yatzy(self, dice_list):
        """
        Function checks yatzy, all dice are the same.
        -- Return bool
        """
        dice_list.sort()
        if len(set(dice_list)) == 1:
            return True
        return False