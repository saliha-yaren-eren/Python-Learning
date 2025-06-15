from sys import argv
from os.path import exists
from sys import exit
"""print ("hello world")
print('Yay! Printing.')
print('I "said" do not thouch this')
#kşgjkdsg
print("Hens",25+30/6)
print("Is it greater?", 3>5)
print(5<9)
cars=50
print(cars)
print("cars =",cars, "hklglkh")
print("Hey %s there." % "you")
x=35 
y=74
z=180
print("If I add %d, %d, and %d I get %d." % (x,y,z,x+y+z))
print(round(1.744))
w="There are %d types \n of people." % 10
binary= "binary"
do_not= "don't"
e= "Those who know %s and those who %s." % (binary, do_not)
print (e)
print(w)
print("I said: %r." %w)
print(" I also said: '%s'." % e)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)
print("."*10)
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one","two","three","four"))
print(formatter  % (formatter%(1,2,3,4), formatter, formatter, formatter))
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
blacklash_cat = "I'm \\ a \\ cat."
fat_cat = ""
I'll do a list:
\t* Cat food
\t*Fishies
\t*Catnip\n\t* Grass
""
print (tabby_cat)
print (persian_cat)
print (blacklash_cat)
print (fat_cat)"""
"""while True:
       for i in ["/","- ","|","\\","|"]:
           print ("%s\r" % i, end='')


age = input("How old are you? ")
print(age)

#ex13
script, first, second, third = argv
print("The script is called:",script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third) 

#ex14
script, user_name = argv
prompt="> "
print("Hi %s I'm the %s script.\nI'd like to ask you a few questions." % (user_name, script))
print("Do you like me %s?" % user_name)
likes = input(prompt)
print("Where do you live % s?" % user_name)
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print("Alright, so you said %r about liking me.\n" +
"You live in %r. Not sure where that is.\n" +
"And you have a %r computer. Nice." % (likes, lives, computer))

#ex15
script, filename = argv
txt = open(filename)
print("Here's your file %r:" % filename)
print(txt.read())

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())

#ex16
script, filename = argv
print("we're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")
print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finally, we close it.")
target.close()

#ex17
script, from_file, to_file = argv
print("Copying from %s to %s" % (from_file, to_file))
in_file = open(from_file)
indata = in_file.read()
#kısa hali: in_file = open(from_file).read()
#kısa halinde in_file için close komutuna gerek kalmaz.
print("The input file is %d bytes long" % len(indata))
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
out_file = open(to_file, 'w')
out_file.write(indata)
print("Alright, all done.")
out_file.close()
in_file.close()

#ex18
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))
def print_one(arg1):
    print("arg1: %r" % arg1)
def print_none():
    print("I got nothing.")
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

#ex19
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheese" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party")
    print("Get a blanket.\n")
cheese_and_crackers(20, 30)
amount_of_cheese=10
amount_of_crackers=50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
cheese_and_crackers(4+5,5+9)
cheese_and_crackers(amount_of_cheese+8,amount_of_crackers-9)

#ex20
script, input_file= argv
def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file=open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

#ex21
def add(a, b):
    print("ADDING %d + %d" % (a,b))
    return a+b
def subtract(a,b):
    print("SUBTRACTING %d - %d" % (a,b))
    return a-b
def multiply(a,b):
    print("MULTIPLYING %d * %d" % (a,b))
    return a*b
def divide(a,b):
    print("DIVIDING %d / %d" % (a,b))
    return a/b

print("Let's do some math with just functions!")
age = add(30, 5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)
print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight,divide(iq,2))))
print("That becomes: ", what, "Can you do it by hand?")

#ex24
print ("Let's practice everything.")
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = ""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
""

print ("- - - - - - - - - - - - - - ")
print (poem)
print ("- - - - - - - - - - - - - - ")


five = 10 - 2 + 3 - 6
print ("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print ("With a starting point of: %d" % start_point)
print ("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print ("We can also do that this way:")
print ("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))


#ex25
def break_words(stuff):
    ""This function will break up words for us.""
    words = stuff.split(' ')
    return words

def sort_words(words):
    ""Sorts the words.""
    return sorted(words)

def print_first_word(words):
    ""Prints the first word after popping it off.""
    word = words.pop(0)
    print (word)

def print_last_word(words):
    ""Prints the last word after popping it off.""
    word = words.pop(- 1)
    print (word)

def sort_sentence(sentence):
    ""Takes in a full sentence and returns the sorted words.""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    ""Prints the first and last words of the sentence.""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    ""Sorts the words then prints the first and last one.""
    words = sort_sentence(sentence)
    print_first_word(words)

#ex29
people = 20
cats=30
dogs=15
if people<cats:
    print("too many cats")
if people>cats:
    print("not many cats")
if people<dogs:
    print("drooled")
if people>dogs:
    print("dry")
dogs+=5
if people >= dogs:
    print("people are greater than dogs")
if people <= dogs:
    print("people are less than dogs")
if people == dogs:
    print("people are equal dogs")

#ex30
people= 30
cars=40
buses=15
if cars>people:
    print("weeshould take the cars")
elif cars<people:
    print("we should not take the cars")
else:
    print("we can not decide")

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

#ex32
the_count= [[1,2],[3,4,5]]
fruits=['apples', 'oranges', 'pears', 'apricots']
change=[1, 'pennies', 2, 'dimes', 3, 'quarters']
for number in the_count:
    print("This is count %r" % number)
    for number2 in number:
        print("This is count %d" % number2)
for fruit in fruits:
    print("A fruit of type: %s" % fruit)
for i in change:
    print("I got %r" % i)
elements=[]
for i in range(0, 6):
    print("Adding %d to the list." % i)
    elements.append(i)
for i in elements:
    print("Element was: %d" % i)

#ex33
i=0
numbers=[]
while i<6:
    print("At the top i is %d" % i)
    numbers.append(i)
    i+=1
    print("Number now: ", numbers)
    print("At the bottom i is %d" % i)
print("The numbers: ")
for num in numbers:
    print(num)

#ex35
def gold_room():
    print("This room is full of gold. How much do you take?")
    next= input("> ")
    if "0" in next or "1" in next:
        how_much=int(next)
    else:
        dead("Man, learn to type a number.")
    if how_much<50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
def bear_room():
    print("There is a bear here.\nThe bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved=False
    while True:
        next=input("> ")
        if next=="take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next=="taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved=True
        elif next=="taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next=="open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what means.")
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    next=input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
def dead(why):
    print(why, "Good job!")
    exit(0)
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    next=input("> ")
    if next=="left":
        bear_room()
    elif next=="right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
start()

#ex36
print('''
Bir gece odanda uyuyorken bir fısıltıyla uyanırsın.
Odanın köşesindeki eski ayna aniden parlamaya başlar.
Aynaya dokunduğunda, zamanın dışına çıkarsın — antik, büyülü bir kalenin içine çekilirsin.
Bu kale farklı çağların iç içe geçtiği bir yerdir.
Orta Çağ zindanları, teknolojik laboratuvarlar ve unutulmuş tapınaklar bir arada bulunur.
Amaç: Kaleden kaçmak ve kendi zamanına dönmek.

Ancak dikkatli ol!
Kimi kapıların arkasında tuzaklar, kimilerinde canavarlar, kimilerindeyse yardım edebilecek eski zaman yolcuları var.
Her kararın seni hayatta tutabilir ya da sonsuza dek bu zaman boşluğuna hapsolmana neden olabilir...
''')
def mirror_room():
    print("Now you are in Mirror Room.")
    print('''
                       [Gizli Tapınak]
                        ↑         ↑
                  [Zaman Tüneli]  |
                   ↑        ↑     |
         [Zindan] ←      [Ayna Odası]      → [Gelecek Laboratuvarı]
                             ↓
                      [Saat Kulesi]
    ''')
    print("Where do you wanna go?")
    choice=int(input("1.Zindan\n2.Gelecek Laboratuvarı\n3.Saat Kulesi\n4.Gizli Tapınak\n5.Zaman Tüneli\n> "))
    if choice==1:
        zindan()
    elif choice==2:
        gelecek_laboratuvari()
    elif choice==3:
        saat_kulesi()
    elif choice==4:
        gizli_tapinak()
    elif choice==5:
        zaman_tüneli()
    else:
        print("Write acceptable number!")
        mirror_room()
def zaman_tüneli():
    print('''There are 3 portals:
    1.Red Portal
    2.Blue Portal
    3.Green Portal
    There is a sentence down of the Green Portal:
    Only the person who can figure out time can go inside this portal.
    Be carefull about your choose if you choose wrong portal you can go time space and you never come back!
    If you wanna come back Mirror Room now, press "0".
    ''')
    choice=int(input("> "))
    if choice==1:
        zindan()
    elif choice==2:
        print("You are in Time Space now. You will be here forever!")
        exit(0)
    elif choice==3:
        print("You are back to real time. Congratulations!")
    elif choice==0:
        print("You gonna back to Mirror Room.")
        mirror_room()
    else:
        print("Write acceptable number!")
        mirror_room()
def zindan():
    print("There is a writing: 'You do not lose in darkness. Lİght comes from east. Do not forget 7...")
    print("You can press 0 if you want go back Mirror Room.")
    while True:
        choice = int(input("> "))
        if choice == 0:
            mirror_room()
            break
        else:
            print("Write acceptable number!")

def gelecek_laboratuvari():
    print("I always move in the time but never go back. I neither stop nor sleep. What is I?")
    answer=input("> ")
    if answer=='time':
        print("Code has been solved! Time code: AXR-1927")
        print("You can press 0 if you want go back Mirror Room.")
        while True:
            choice = int(input("> "))
            if choice == 0:
                mirror_room()
                break
            else:
                print("Write acceptable number!")
    else:
        print("Try again!")
        gelecek_laboratuvari()

def saat_kulesi():
    print("Tİme only start to flow again with true kod. Three letters, four numbers... Only the past and the future know this password.")
    i=0
    answer2=False
    while i<4 and answer2==False:
        answer=input("> ")
        if answer=='AXR-1927' and i<3:
            print("Real Time Portal was opened. You must find true Portal to go real time.")
            answer2=True
            print("You can press 0 if you want go back Mirror Room.")
            while True:
                choice = int(input("> "))
                if choice == 0:
                    mirror_room()
                    break
                else:
                    print("Write acceptable number!")
        elif answer!='AXR-1927' and i<3:
            print("Wrong answer! Try again!")
            i+=1
        else:
            print("You have been tried three time. ")
            print("You are in Time Space now. You will be here forever!")
            exit(0)
def gizli_tapinak():
    print("I am neither full nor empty, what is inside me is not known. Whoever goes into me are lost, whoever comes out is changed. What is me?")
    answer=input("> ")
    if answer=='mirror':
        print("There is a message for you from time traveler.")
        print("Do not forget the code AXR-1927 when you go through mirror. However first you must go to the tower where time has stoped.")
        print("You can press 0 if you want go back Mirror Room.")
        while True:
            choice = int(input("> "))
            if choice == 0:
                mirror_room()
                break
            else:
                print("Write acceptable number!")


    else:
        print("Wrong answer! Time travel lost!")
        print("You can press 0 if you want go back Mirror Room.")
        while True:
            choice = int(input("> "))
            if choice == 0:
                mirror_room()
                break
            else:
                print("Write acceptable number!")

mirror_room()"""

#ex37
kl=[1,2,3,4,5,6,7,8,9]
del kl[2]
print(kl)
jk=[1,2,3,4,5,6,7,8,9]
del jk[1:2]
print(jk)
mk={'a':1, 'b': 2}
del mk['a']
print(mk)
keys=mk.keys()
print(keys)
print(mk.values())
print(mk.items())
print(mk.get('b'))
mk.update({'b': 5 ,'c': 9})
print(mk)
print(mk.pop('b'))
print(mk)
kl.append(50)
print(kl)
kl.remove(1)
print(kl)
kl.pop(-2)
print(kl)
kl.insert(4,80)
print(kl)
del jk
kl.clear()
print(kl)
hu={1,2,3,4,5}
hu.add(7)
print(hu)
hu.remove(3)
print(hu)
df={5,6,7,8,9}
print(hu.union(df))
print(hu.intersection(df))
metin='hello world'
print(metin.upper())
print(metin.lower())
print(metin.replace('hello', 'hi'))
print(metin.split())