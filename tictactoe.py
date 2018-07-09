BOARD = [
    ['0', '1', '2'],
    ['3', '4', '5'],
    ['6', '7', '8']
]
# print ("0 | 1 | 2")
# print("----------- ")
# print("3 | 4 | 5 ")
# print("-----------")
# print("6 | 7 | 8 ")

def print_board():
    for item in BOARD:
        str="--------\n"
        for column in item:
            str += column + " | "
        print(str)

str = ""
print("str is now: " + str)

str = str + "a"
print("str is now: " + str)

playerA = 1
playerB = -1

# def take_turn(player):
#     if player == 1:
#         print("It's A's turn!")
#     elif player == -1:
#         print("It's B's turn!")
#
#     if playerA==("0"):
#         for line in BOARD=0:
#             print("x")
#
#     if playerA raw_input=0-8
#     print("x")
#
#     if playerB==("0"):
#     for line in BOARD=0:
#         print("O")
#
#     if playerA raw_input=0-8
#     print("O")
#
#     if player == 1:
#         print("It's A's turn!")
#     elif player == -1:
#         print("It's B's turn!")

#def game_over():
#return (True):

#def main():
    # have your main method code here

    #take_turn(playerA)


    #for line in BOARD:
    #    print(line)

    #if game_over():
    #    print("Game over!")


#main()
