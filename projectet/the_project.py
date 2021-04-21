print("Welcome to hangman") #a small menu
print("In this game you will have to guess a word for which you have 10 attempts before the game is lost")
x1=input("Do you wish to play hangman, press y to continue, or n to exit the game ") 
x1=x1.upper()
letter=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

'''
if x1==('Y'):
    x2=10
    word=["S","U","N"]
    g=len(word)
    correct=[]
    
    while x2>=0:
        index=0
        guess=input("Guess a letter please ")
        while len(guess)>1:
            guess=input("Please only enter one letter at a time as your guess ")
        while g>=len(word):
            guess=guess.upper()
            for x3 in word:
                index=index+1
                if x3==guess:
                    word.pop(index-1)
                    correct.append(guess)
                    index=0
'''
                
if x1==('Y'):
    x2=10
    word=["S","U","N"]
    g=len(word)
    correct=[]
    
    
    while g>=len(word):
        index=0
        guess=input("Guess a letter please ")
        while len(guess)>1:
            guess=input("Please only enter one letter at a time as your guess ")
        while x2>=10:
            guess=guess.upper()
            for x3 in word:
                index=index+1
                if x3==guess:
                    word.pop(index-1)
                    correct.append(guess)
                    index=0

