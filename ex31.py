#ex31
print("You enter a dark room with two doors. Do you go thourgh door #1 or door #2?")
door=input("> ")
if door=="1":
    print("Tere is a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2.Scream at the bear.")
    bear=input("> ")
    if bear=="1":
        print("The bear eats your face off. Good job!")
    elif bear=="2":
        print("the bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)
elif door=="2":
    print("You stare into the endless abyss at cthulhu's retina.")
    print("1. blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. understanding revolvers yelling melodies.")
    insanity=input("> ")
    if insanity=="1" or insanity=="2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")
else:
    print("You stumble around and fall on a knife and die. Good job!")