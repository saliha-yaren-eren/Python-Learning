#ex14
from sys import argv
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