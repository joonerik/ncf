import random

players = ["Bjørn", "Joon", "Pille", "Sigurd", "Harvey", "Preben", "Scott", "Klokk"]
black_team = []
color_team = []
turn = "black"


def print_team(drawn_players):
    unrevealed_list = ["?", "?", "?", "?"]
    if len(unrevealed_list) == 5:
        unrevealed_list[: len(drawn_players)] = drawn_players
        print(" ", unrevealed_list[3], " ", unrevealed_list[4])
        print("   ", unrevealed_list[2], " ")
        print(" ", unrevealed_list[0], " ", unrevealed_list[1])
    elif len(unrevealed_list) == 4:
        unrevealed_list[: len(drawn_players)] = drawn_players
        print(" ", unrevealed_list[3], " ", unrevealed_list[2])
        print(" ", unrevealed_list[0], " ", unrevealed_list[1])


print(players)
print("BLACK TEAM")
print_team(black_team)
print()
print("COLOR TEAM")
print_team(color_team)
input("Press enter to draw the next player...")
print()
print()

while len(players) > 0:
    # Shuffle the players
    random.shuffle(players)
    # Get the first player from the shuffled list
    new_player = players.pop(0)
    if turn == "black":
        black_team.append(new_player)
        turn = "color"
    else:
        color_team.append(new_player)
        turn = "black"
    print("Drawn player:", new_player)
    print("BLACK TEAM")
    print_team(black_team)
    print()
    print("COLOR TEAM")
    print_team(color_team)
    input("Press enter to draw the next player...")
    print()
    print()

print("Thank you for using the OFFICIAL NCF DRAWING TOOL")
