import random
import sys
import time


def restart_game():
    while True:
        answer = input("Would you like to play again? Y/N   ").lower()
        if answer == "y":
            game_start()
        elif answer == "n":
            print("Good game!")
            sys.exit(0)
        else:
            print("I don't understand...")


def check_win_condition_player1(top, middle, bottom):
    if top[1] == "X" and top[2] == "X" and top[3] == "X":
        return True
    elif middle[4] == "X" and middle[5] == "X" and middle[6] == "X":
        return True
    elif bottom[7] == "X" and bottom[8] == "X" and bottom[9] == "X":
        return True
    elif top[1] == "X" and middle[4] == "X" and bottom[7] == "X":
        return True
    elif top[2] == "X" and middle[5] == "X" and bottom[8] == "X":
        return True
    elif top[3] == "X" and middle[6] == "X" and bottom[9] == "X":
        return True
    elif top[1] == "X" and middle[5] == "X" and bottom[9] == "X":
        return True
    elif top[3] == "X" and middle[5] == "X" and bottom[7] == "X":
        return True


def check_win_condition_computer_or_player2(top, middle, bottom):
    if top[1] == "O" and top[2] == "O" and top[3] == "O":
        return True
    elif middle[4] == "O" and middle[5] == "O" and middle[6] == "O":
        return True
    elif bottom[7] == "O" and bottom[8] == "O" and bottom[9] == "O":
        return True
    elif top[1] == "O" and middle[4] == "O" and bottom[7] == "O":
        return True
    elif top[2] == "O" and middle[5] == "O" and bottom[8] == "O":
        return True
    elif top[3] == "O" and middle[6] == "O" and bottom[9] == "O":
        return True
    elif top[1] == "O" and middle[5] == "O" and bottom[9] == "O":
        return True
    elif top[3] == "O" and middle[5] == "O" and bottom[7] == "O":
        return True


# start the game
def game_start():
    top    = {1: " ", 2: " ", 3: " "}
    middle = {4: " ", 5: " ", 6: " "}
    bottom = {7: " ", 8: " ", 9: " "}

    print("~ WELCOME TO TIC-TAC-TOE ~\n")

    # the game board
    print("1", "|", "2", "|", "3")
    print(" -------")
    print("4", "|", "5", "|", "6")
    print(" -------")
    print("7", "|", "8", "|", "9")
    print("\nTo select your position, input the number to the corresponding placement.")

    while True:
        number_of_players = input("How many players are playing:   ")
        if number_of_players == "1" or number_of_players == "2":
            while True:
                while True:
                    try:
                        # start player1 turn
                        if " " not in top.values() and " " not in middle.values() and " " not in bottom.values():
                            print("It's a tie!")
                            restart_game()
                        choice = int(input("Player 1, please pick a space to put your 'X':   "))
                        if 0 < choice < 4:
                            if top[choice] == "X" or top[choice] == "O":
                                print("That space is already taken.")
                            else:
                                top[choice] = "X"
                                break
                        elif 3 <= choice < 7:
                            if middle[choice] == "X" or middle[choice] == "O":
                                print("That space is already taken.")
                            else:
                                middle[choice] = "X"
                                break
                        elif 6 <= choice < 10:
                            if bottom[choice] == "X" or bottom[choice] == "O":
                                print("That space is already taken.")
                            else:
                                bottom[choice] = "X"
                                break
                    except:
                        print("I don't understand...")

                # update the board
                print(top[1], "|", top[2], "|", top[3])
                print(" -------")
                print(middle[4], "|", middle[5], "|", middle[6])
                print(" -------")
                print(bottom[7], "|", bottom[8], "|", bottom[9])

                # check to see if player1 has won
                player_win = check_win_condition_player1(top, middle, bottom)
                if player_win:
                    print("Player 1 Wins!")
                    restart_game()

                # start computer turn
                if number_of_players == "1":
                    while True:
                        if " " not in top.values() and " " not in middle.values() and " " not in bottom.values():
                            print("It's a tie!")
                            restart_game()
                        computer_choice = random.randint(1, 9)
                        if 0 < computer_choice < 4:
                            if top[computer_choice] == "X" or top[computer_choice] == "O":
                                continue
                            else:
                                top[computer_choice] = "O"
                                break
                        elif 3 <= computer_choice < 7:
                            if middle[computer_choice] == "X" or middle[computer_choice] == "O":
                                continue
                            else:
                                middle[computer_choice] = "O"
                                break
                        elif 6 <= computer_choice < 10:
                            if bottom[computer_choice] == "X" or bottom[computer_choice] == "O":
                                continue
                            else:
                                bottom[computer_choice] = "O"
                                break
                    input("Press any key for computer placement.")
                    print(". ", end="")
                    time.sleep(0.5)
                    print(". ", end="")
                    time.sleep(0.5)
                    print(".")
                    time.sleep(0.5)
                    # update the board
                    print(top[1], "|", top[2], "|", top[3])
                    print(" -------")
                    print(middle[4], "|", middle[5], "|", middle[6])
                    print(" -------")
                    print(bottom[7], "|", bottom[8], "|", bottom[9])

                    # check to see if the computer won
                    computer_win = check_win_condition_computer_or_player2(top, middle, bottom)
                    if computer_win:
                        print("The computer wins!")
                        restart_game()

                    # check to see if there is a tie
                    if " " not in top.values() and " " not in middle.values() and " " not in bottom.values():
                        print("It's a tie!")
                        restart_game()
                elif number_of_players == "2":
                    while True:
                        try:
                            # start player2 turn
                            if " " not in top.values() and " " not in middle.values() and " " not in bottom.values():
                                print("It's a tie!")
                                restart_game()
                            choice = int(input("Player 2, please pick a space to put your 'O':   "))
                            if 0 < choice < 4:
                                if top[choice] == "X" or top[choice] == "O":
                                    print("That space is already taken.")
                                else:
                                    top[choice] = "O"
                                    break
                            elif 3 <= choice < 7:
                                if middle[choice] == "X" or middle[choice] == "O":
                                    print("That space is already taken.")
                                else:
                                    middle[choice] = "O"
                                    break
                            elif 6 <= choice < 10:
                                if bottom[choice] == "X" or bottom[choice] == "O":
                                    print("That space is already taken.")
                                else:
                                    bottom[choice] = "O"
                                    break

                        except:
                            print("I don't understand...")

                    # update the board
                    print(top[1], "|", top[2], "|", top[3])
                    print(" -------")
                    print(middle[4], "|", middle[5], "|", middle[6])
                    print(" -------")
                    print(bottom[7], "|", bottom[8], "|", bottom[9])

                    # check to see if player 2 wins
                    computer_win = check_win_condition_computer_or_player2(top, middle, bottom)
                    if computer_win:
                        print("Player 2 Wins!")
                        restart_game()
        else:
            print("Invalid input")


game_start()
