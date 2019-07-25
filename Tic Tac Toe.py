player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

print(l1)
print(l2)
print(l3)

turn = "player1"

count = 0
won = False

while count<9 and not won:

    if turn == "player1":
        print(player1 + "'s turn")
        X = input("Enter number where you want to place 'X': ")

        if X == "1":
            if l1[0] == "X" or l1[0] == "O":
                print("Please choose another number")
            else:
                l1[0] = "X"
                turn = "player2"
                count += 1
        elif X == "2":
            if l1[1] == "X" or l1[1] == "O":
                print("Please choose another number")
            else:
                l1[1] = "X"
                turn = "player2"
                count += 1
        elif X == "3":
            if l1[2] == "X" or l1[2] == "O":
                print("Please choose another number")
            else:
                l1[2] = "X"
                turn = "player2"
                count += 1
        elif X == "4":
            if l2[0] == "X" or l2[0] == "O":
                print("Please choose another number")
            else:
                l2[0] = "X"
                turn = "player2"
                count += 1
        elif X == "5":
            if l2[1] == "X" or l2[1] == "O":
                print("Please choose another number")
            else:
                l2[1] = "X"
                turn = "player2"
                count += 1
        elif X == "6":
            if l2[2] == "X" or l2[2] == "O":
                print("Please choose another number")
            else:
                l2[2] = "X"
                turn = "player2"
                count += 1
        elif X == "7":
            if l3[0] == "X" or l3[0] == "O":
                print("Please choose another number")
            else:
                l3[0] = "X"
                turn = "player2"
                count += 1
        elif X == "8":
            if l3[1] == "X" or l3[1] == "O":
                print("Please choose another number")
            else:
                l3[1] = "X"
                turn = "player2"
                count += 1
        elif X == "9":
            if l3[2] == "X" or l3[2] == "O":
                print("Please choose another number")
            else:
                l3[2] = "X"
                turn = "player2"
                count += 1

    else:
        print(player2 + "'s turn")
        O = input("Enter number where you want to place 'O': ")

        if O == "1":
            if l1[0] == "X" or l1[0] == "O":
                print("Please choose another number")
            else:
                l1[0] = "O"
                turn = "player1"
                count += 1
        elif O == "2":
            if l1[1] == "X" or l1[1] == "O":
                print("Please choose another number")
            else:
                l1[1] = "O"
                turn = "player1"
                count += 1
        elif O == "3":
            if l1[2] == "X" or l1[2] == "O":
                print("Please choose another number")
            else:
                l1[2] = "O"
                turn = "player1"
                count += 1
        elif O == "4":
            if l2[0] == "X" or l2[0] == "O":
                print("Please choose another number")
            else:
                l2[0] = "O"
                turn = "player1"
                count += 1
        elif O == "5":
            if l2[1] == "X" or l2[1] == "O":
                print("Please choose another number")
            else:
                l2[1] = "O"
                turn = "player1"
                count += 1
        elif O == "6":
            if l2[2] == "X" or l2[2] == "O":
                print("Please choose another number")
            else:
                l2[2] = "O"
                turn = "player1"
                count += 1
        elif O == "7":
            if l3[0] == "X" or l3[0] == "O":
                print("Please choose another number")
            else:
                l3[0] = "O"
                turn = "player1"
                count += 1
        elif O == "8":
            if l3[1] == "X" or l3[1] == "O":
                print("Please choose another number")
            else:
                l3[1] = "O"
                turn = "player1"
                count += 1
        elif O == "9":
            if l3[2] == "X" or l3[2] == "O":
                print("Please choose another number")
            else:
                l3[2] = "O"
                turn = "player1"
                count += 1

    print(l1)
    print(l2)
    print(l3)

    if l1[0] == l1[1] and l1[1] == l1[2]:
        if l1[1] == "X":
            print(player1 + " won")
        else:
            print(player2 + " won")
        won = True
    elif l2[0] == l2[1] and l2[1] == l2[2]:
        if l2[1] == "X":
            print(player1 + " won")
        else:
            print(player2 + " won")
        won = True
    elif l3[0] == l3[1] and l3[1] == l3[2]:
        if l3[1] == "X":
            print(player1 + " won")
        else:
            print(player2 + " won")
        won = True
    elif l1[0] == l2[0] and l2[0] == l3[0]:
        if l2[0] == "X":
            print(player1 + " won")
        else:
            print(player2 + " won")
        won = True
    elif l1[1] == l2[1] and l2[1] == l3[1]:
        if l2[1] == "X":
            print(player1 + " won")
        else:
            print(player2 + " won")
        won = True
    elif l1[2] == l2[2] and l2[2] == l3[2]:
        if l2[2] == "X":
            print(player1 + " won")
        else:
            print(player2 + " won")
        won = True
    elif l1[0] == l2[1] and l2[1] == l3[2]:
        if l2[1] == "X":
            print(player1 + " won")
        else:
            print(player2 + " won")
        won = True
    elif l1[2] == l2[1] and l2[1] == l3[0]:
        if l2[1] == "X":
            print(player1 + " won")
        else:
            print(player2 + " won")
        won = True

if count == 9 and not won:
    print("Match Draw")
