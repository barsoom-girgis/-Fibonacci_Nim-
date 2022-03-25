# Barsoom Girgis Sedkey Rizk
# ID "20210088"
# Task 2
# Game NO# 8
# Fibonacci Nim


# set player
player = 1
# set the started  no#  of coins
coins = int(input("please enter the number of coins on the pile  "))
print("the number of coins is now  ", coins)
old_move = coins
while True:

    # start first move of coins
    print("player ", player)
    # make a while  loop that check if player take the all number of coins or not
    # if no# of moves greater than or equal no# of coins it will be illegal move and make the player to play again
    while True:
        move = int(input("what is your move "))

        if move >= coins or move >= old_move * 2:
            print("Illegal move ")
        else:
            break
    old_move = move
    # update the number of objects
    coins = coins - move
    # show the statue
    print("the number of coins left is ", coins)

    # switch between two players
    if player == 1:
        player = 2
    else:
        player = 1

    # show the win/lose/draw  statue
    if coins == 1:
        print("player   ", player, "  wins ")
        break

print(" game is over ")