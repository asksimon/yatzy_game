from player import Player
from roll import Roll
from score import Score

def main():
    """
    Main game function.

    First select amount of players. 
    
    Second name the players.

    Third ask player to roll dice. And show result

    Fourth ask player to hold dice. Then roll again and show result

    Fifth ask player to select dice to hold.

    Sixth show final result of the rolls.

    Seventh ask player to choose a combination to score.

    Eighth count and show score of all players.

    Ninth check if all combinations are filled by player. If yes, end the game.
    """

    #Create dice and a scoreboard
    dice = Roll()
    scoreboard = Score()

    #Choose how many players are going to play. Up to 4.
    player_count = input("How many players wants to play (up to 4)? ")

    #Loop until correct amount of players.
    while(True):
        #Check if string is a number
        count_is_numeric = player_count.isnumeric()
        if count_is_numeric == False:
            player_count = input("Please type a number between 1 and 4. ")
        else:
            player_count = int(player_count)
            if player_count < 1 or player_count > 4:
                player_count = input("Invalid amount of players. Please select a number between 1 and 4 ")
            else:
                break
    
    #Name players
    if player_count == 1:
        name1 = input("Please name player 1: ")
        player_1 = Player(name1)
        player_list = [player_1]
    if player_count == 2:
        name1 = input("Please name player 1: ")
        player_1 = Player(name1)
        name2 = input("Please name player 2: ")
        player_2 = Player(name2)
        player_list = [player_1, player_2]
    if player_count == 3:
        name1 = input("Please name player 1: ")
        player_1 = Player(name1)
        name2 = input("Please name player 2: ")
        player_2 = Player(name2)
        name3 = input("Please name player 3: ")
        player_3 = Player(name3)
        player_list = [player_1, player_2, player_3]
    if player_count == 4:
        name1 = input("Please name player 1: ")
        player_1 = Player(name1)
        name2 = input("Please name player 2: ")
        player_2 = Player(name2)
        name3 = input("Please name player 3: ")
        player_3 = Player(name3)
        name4 = input("Please name player 4: ")
        player_4 = Player(name4)
        player_list = [player_1, player_2, player_3, player_4]
    
    #Loop game until a player get all combinations
    game = True
    while (game):
        
        #Change players after each round. Ask them if they want to roll the dice.
        for player in player_list:
            start = input(f"Does {player.name} wants to roll the dice (type Yes)? ")

            #Loop until correct answer.
            while(True):
                if start != "Yes":
                    start = input("Please type Yes when ready. ")
                else:
                    break

            #First roll. Then ask player which dice to hold.
            dice.roll_dice()
            hold1 = dice.hold_dice()

            #If player don't keep all dice roll a second time. Then ask player which dice to hold.
            if len(hold1) != 0:
                dice.reroll_dice(hold1)
                hold2 = dice.hold_dice()

                #If player don't hold all dice roll a final time. Hold all dice. Print list.
                if len(hold2) != 0:
                    final_roll = dice.reroll_dice(hold2)
                    final_combination = dice.forced_dice_hold(final_roll)
                    print(f'Your final combination is {final_combination}')

                #If player hold all dice. Put all dice in same list. Print list.
                else:
                    final_combination = dice.forced_dice_hold(hold2)
                    print(f'Your final combination is {final_combination}')

            #If player hold all dice. Put all dice in same list. Print list.
            else:
                final_combination = dice.forced_dice_hold(hold1)
                print(f'Your final combination is {final_combination}')

            
            #Ask players which combinations they wish to count.
            combination = input(f'Which combination do you want to score (Ones, Twos, Threes, Fours, Fives, Sixes, House or Yatzy)? ')

            while(True):    
                #Count the combination and score of said combination.
                if combination == "Ones":
                    score = scoreboard.ones(final_combination)
                    player.score(combination, score)
                    break
                elif combination == "Twos":
                    score = scoreboard.twos(final_combination)
                    player.score(combination, score)
                    break
                elif combination == "Threes":
                    score = scoreboard.threes(final_combination)
                    player.score(combination, score)
                    break
                elif combination == "Fours":
                    score = scoreboard.fours(final_combination)
                    player.score(combination, score)
                    break
                elif combination == "Fives":
                    score = scoreboard.fives(final_combination)
                    player.score(combination, score)
                    break
                elif combination == "Sixes":
                    score = scoreboard.sixes(final_combination)
                    player.score(combination, score)
                    break
                elif combination == "House":
                    score = scoreboard.house(final_combination)
                    player.score(combination, score)
                    break
                elif combination == "Yatzy":
                    score = scoreboard.yatzy(final_combination)
                    player.score(combination, score)
                    break
                else:
                    combination = input(f'Please type a valid combination (Ones, Twos, Threes, Fours, Fives, Sixes, House or Yatzy): ')
            
            #Print scoreboard of all players.
            for player_scores in player_list:
                player_scores.print_current_scoreboard(player_scores)

            #Check if all combinations have been counted for. If true, end the game.
            winner = player.check_scoreboard(player)
            if winner == True:
                game = False

if __name__ == "__main__":
    main()