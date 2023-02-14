# Rock Paper Scissors
# 
# Let's play! You have to return which player won! In case of a draw return 
# Draw!.
# 
# Examples(Input1, Input2 --> Output):
# 
# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"
def rps(p1, p2):
    dict = {
                "scissors": 0,
                "paper": 1,
                "rock": 2
            }
    
    #                           Player 2
    #                scissors     paper      rock 
    #                   [0]        [1]        [2]
    #  Player 1     -------------------------------
    #  scissors [0] |    D          1          2
    #  paper    [1] |    2          D          1
    #  rock     [2] |    1          2          D

    result = [
                ["Draw!"        , "Player 1 won!", "Player 2 won!"],
                ["Player 2 won!", "Draw!"        , "Player 1 won!"],
                ["Player 1 won!", "Player 2 won!", "Draw!"]
            ]

    return result[dict[p1]][dict[p2]]

print(rps("scissors", "paper"))
print(rps("scissors", "rock"))
print(rps("paper", "paper"))