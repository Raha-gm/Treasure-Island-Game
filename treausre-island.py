print("Welcome to Treasure Island!")

choice1 = input("You've reached a crossroads. Left or right? ")

if choice1 == "left":
    print("Hooray! You've reached a lake.")
    choice2 = input("1 = Wait for a boat / 2 = Swim ")

    if choice2 == "1":
        print("Hooray! You've reached the castle.")
        choice3 = input("Choose one of the doors: red / blue / yellow ")

        if choice3 == "blue":
            print("You fell into the water. You lost!")
        elif choice3 == "yellow":
            print("Hooray! You found the treasure!")
        elif choice3 == "red":
            print("The castle caught fire. You lost!")

    elif choice2 == "2":
        print("A crocodile ate you. You lost!")

elif choice1 == "right":
    print("You fell into a hole. You lost!")

else:
    print("Invalid choice!")