#ex38
ten_thing= "Apple Orange Crows Telephone Light Sugar"
print("Must be ten words.")
other_things= ["Day", "Nİght", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
word=ten_thing.split(' ')
while len(word)!=10:
    last=other_things.pop()
    word.append(last)
print(word)
print(word[1])
print(word[-1])
print(word.pop())
print(' '.join(word))
print('#'.join(word[3:5]))