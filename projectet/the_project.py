# coding: utf-8
print("Welcome to hangman") #a small menu
print("In this game you will have to guess a word for which you have 10 attempts before the game is lost") #rulesblock
x1=input("Do you wish to play hangman, press y to continue, or n to exit the game: ") # menu 2 so to speak 
x1=x1.upper()
letters=["1","2","3","4","5","6","7","8","9","0","Å","Ä","Ö"] 
guessedLetters=[]
correctguesses=[]


if x1==('Y'):
    x2=10 #the amount of attempts
    word=["S","U","N","S","H","I","N","E"] 
    g=len(word)#making it so that the function works with other words if i ever add a random word generator
    word2= [] #here we put both the undershlashes and the correct letters
    for i in word:
        word2.append("_") # here goes the part that is the small dashes under so that one can see what letters are correctly guessed
    print ( " ".join(word2) ) # part 2 of the "underslashes"
    index2=0
    
    
    while word2!=word:
        if x2==0:
            print("seems like you're out of guesses, better luck next time!") #here you end up if you guess too many wrongs
            print("exiting...")
            print("exiting...")
            print("exiting...")
            print("exiting...")
            exit()

        index=0
        guess=input("Guess a letter please: ") #guessing screen
        guess=guess.upper()
        correctguesses=[]
        while len(guess)>1:
            guess=input("Please only enter one letter at a time as your guess: ") #only one letter
            guess=guess.upper()
        for x5 in guessedLetters:
            if x5==guess:
                guess=input("You have already tried that letter, try again: ") # here you come if you guess a guessed letter
                guess=guess.upper()
        for x6 in letters:
            if x6==guess:
                guess=input("that is not a valid letter, try again:") # in case of retarded guesses, does not work with shifted letters or altgr.
        guessedLetters.append(guess)
        for x3 in word:
            if x3==guess:
                if guess == word[index]:
                    correctguesses.insert(0,index)
                    word2.pop(index)
                    word2.insert(index,guess)
                
                else:
                    index += 1
            index += 1
            
        
         
        print( " ".join(word2) )
            
            
  
  
              
        if correctguesses==[]:
            x2=x2-1
            print("Wrong guess, try again.")
            print("You have",x2,"tries left.")# writing out of the incorrect guess and the amount of attempts left
        else:
            print:("you lose challanger, please come again") #"losing screen"

    print("You win challanger, please come again") #"winning screen"
    exit()
else:
    print("then please come back when you feel like playing challanger")
    exit()#if you answer n you come here 
        
            
            
