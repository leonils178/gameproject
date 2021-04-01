print("Welcome to hangman")
word=[sun]
print("In this game you will have to guess a word for which you have 10 attempts before the game is lost")
x1=("Do you wish to play hangman, press y to continue, or n to exit the game ") 
x1=x1.upper
letter=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


if x1==('Y'):
    x2=10
    word=["S","U","N"]
    correct=[]
    
    while x2>=0:
        guess=input("Guess a letter please")
        while len(guess)>1:
            guess=input("Please only enter one letter at a time as your guess")
            
        guess=guess.upper
        index=0#look out for bugs here
        for x3 in word:
            index=index+1
            if guess==x3:
                
                print("Correct guess, you have",len(word),"letters left to guess")
                index=0
                
        else:
            x2=x2-1
            print("Wrong guess, you have",x2,"attempts left to guess the correct letters")
            index=0
        
