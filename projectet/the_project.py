print("Welcome to hangman") #a small menu
print("In this game you will have to guess a word for which you have 10 attempts before the game is lost") #rulesblock
x1=input("Do you wish to play hangman, press y to continue, or n to exit the game ") # menu 2 so to speak 
x1=x1.upper()
letter=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


if x1==('Y'):
    x2=10
    word=["S","U","N","S","H","I","N","E"]
    g=len(word)
    correct=[]
    word2= []
    for i in word:
        word2.append("_") # here goes the part that is the small dashes under so that one can see what letters are correctly guessed
    print ( " ".join(word2) ) # part 2 of the "underslashes"
    
    while x2>0:
        index=0
        guess=input("Guess a letter please ")
        while len(guess)>1:
            guess=input("Please only enter one letter at a time as your guess ")
        correctguesses=[]
        guess=guess.upper()
        for x3 in word:
            if x3==guess:
                correctguesses.insert(0,index)
                correct.append(guess)
                word2.pop(index)
                word2.insert(index,guess)
                
            index=index+1
        print( " ".join(word2) )
            
                
        if correctguesses==[]:
            x2=x2-1
            print("Wrong guess, try again.")
        else:
            for indextopop in correctguesses:
                word.pop(indextopop)
            
