# Part 1: ask what the gamers device is like pc, tablet, phone
device = str(input("What device are you playing on"))
if device == "phone":  
    print("you might be cooked if you are playing a shooter game and might not be able to play fun paid games")
elif device == "tablet": 
    print("Your device might be to big for shooter games and might not be able to play fun paid games")
elif device == "pc":  
    print("you will be  good in every game sometimes and you can play almost any game")
elif device == "console": 
    print("You can play some games")
elif device == "gaming phone": 
    print("Why do you have that, but you still can play some games")
elif device == "gaming ipad": 
    print("Why do you have that, but you can still play games")
# Part 2: as what gamethe gamer is going to play
game = str(input("What game are you playing"))
print(game ," sounds fun")
# Part 3: ask if you are warmed up for what the gamer is playing
warm_up = str(input("Are you warmed up for", game))

if warm_up == yes or warm_up == yeah or warm_up == yup: # type: ignore
    print("good")
else:
    print("You should warm up")
