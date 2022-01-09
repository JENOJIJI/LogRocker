import random

commads = ['scissors','rock', 'paper']

def ComputerGame(player):
    computer = commads[random.randint(0,2)]
    print(f"computer: {computer}")
    if player == computer:
        return ["tie!", 0]
    elif player == "rock":
        if computer == "paper":
            return ["You lose! computer used paper", 0, 'paper']
        else:
            return ["You win! you smashes computer", 1, 'scissor']
    elif player == "paper":
        if computer == "scissors":
            return ["You lose! computer used scissor", 0, 'scissor']
        else:
            return ["You win! you used paper",1, 'rock']
    elif player == "scissors":
        if computer == "rock":
            return ["You lose... computer smashes you", 0, 'scissor']
        else:
            return ["You win! you cut computer", 1, 'paper']
    else:
        return ["That's not a valid play. Check your spelling!", 0, '']
