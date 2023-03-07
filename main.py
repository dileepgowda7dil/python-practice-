name = input("Type ur name: ")
print("welcome " + str(name) + " to this adventure")
answer = input("u r on a dirt road, it has come to an end and u can go left or right. where would like to go? ").lower()

if answer == "right":
    answer = input("you have come to the river you can swim or go around by walking(swim/walk)? ").lower()
    if answer == "swim":
        print("you swam across and eaten by a crocodile")
    elif answer == "walk":
        print("you walked 10km and run out of food and died")
    else:
        print("not a valid option, you lose")

elif answer == "left":
    answer = input("u have come to the bridge it looks wobbly, do u want to cross the bridge or head back(cross/back)? ")
    if answer == "back":
        print("you  are in main road, you are killed by an accident")
    elif answer == "cross":
        answer = input("you have crossed the bridge and met a stranger, do you talk to them(yes/no)? ")
        if answer == "yes":
            print("you got gold from stranger and you are rich")
        elif answer == "no":
            print("stranger is offended and kills you, you lose")
        else:
            print(" you lose")
else:
    print("not a valid option")

print("thank you for playing")
