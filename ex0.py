print ("hello world")
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
fat_cat = """
I'll do a list:
\t* Cat food
\t*Fishies
\t*Catnip\n\t* Grass
"""
print (tabby_cat)
print (persian_cat)
print (blacklash_cat)
print (fat_cat)

while True:
       for i in ["/","- ","|","\\","|"]:
           print ("%s\r" % i, end='')


age = input("How old are you? ")
print(age)