# coding: utf-8
import random
def wordGenerator(): #the wordgenerator of the program as a function
    randomIndex=random.randint(0,9)
    word1=["H","A","M","B","U","R","G","E","R"]
    word2=["U","N","I","C","O","R","N"]
    word3=["A","U","T","O","M","O","B","I","L","E"]
    word4=["C","O","M","P","U","T","E","R"]
    word5=["R","I","V","E","R"]
    word6=["C","H","A","I","R"]
    word7=["C","E","I","L","I","N","G"]
    word8=["M","E","G","A","L","O","M","A","N","I","A","C"]
    word9=["B","O","A","T"]
    word10=["P","E","N","C","I","L"]
    list=[word1,word2,word3,word4,word5,word6,word7,word8,word9,word10]
    return list[randomIndex]
    
    
print("Welcome to hangman") #a small menu
print("In this game you will have to guess a word for which you have 10 attempts before the game is lost") #rulesblock
theChoise=input("Do you wish to play hangman, press y to continue, or n to exit the game: ") # menu 2 so to speak 
theChoise=theChoise.upper()
letters=["1","2","3","4","5","6","7","8","9","0","Å","Ä","Ö"] 
guessedLetters=[]
correctGuesses=[]


if theChoise==('Y'):
    lifes=10 #the amount of attempts
    word=wordGenerator()    
    guessedWord= [] #here we put both the undershlashes and the correct letters
    for i in word:
        guessedWord.append("_") # here goes the part that is the small dashes under so that one can see what letters are correctly guessed
    print ( " ".join(guessedWord) ) # part 2 of the "underslashes"
    
    
    
    while guessedWord!=word:
        if lifes==0:
            print("seems like you're out of guesses, better luck next time!") #here you end up if you guess too many wrongs
            print(" ".join(word))
            print("exiting...")
            print("exiting...")
            print("exiting...")
            print("exiting...")
            exit()

        index=0
        guess=input("Guess a letter please: ") #guessing screen
        guess=guess.upper()
        correctGuesses=[]
        while len(guess)>1:
            guess=input("Please only enter one letter at a time as your guess: ") #only one letter
            guess=guess.upper()
        for failSafe1 in guessedLetters:
            if failSafe1==guess:
                guess=input("You have already tried that letter, try again: ") # here you come if you guess a guessed letter
                guess=guess.upper()
        while guess.isalpha()==False:
                guess=input("that is not a valid letter, try again: ") # in case of retarded guesses, does not work with shifted letters or altgr.
        guessedLetters.append(guess)
        for wordCheker in word:
            if wordCheker==guess:
                if guess == word[index]:
                    correctGuesses.insert(0,index)
                    guessedWord.pop(index)
                    guessedWord.insert(index,guess)
                
                else:
                    index += 1
            index += 1
            
        
         
        print( " ".join(guessedWord) )
            
            
  
  
              
        if correctGuesses==[]:
            lifes=lifes-1
            print("Wrong guess, try again.")
            print("You have",lifes,"tries left.")# writing out of the incorrect guess and the amount of attempts left
        else:
            print:("you lose challanger, please come again")#"losing screen"

    print("You win challanger, please come again") #"winning screen"

else:
    print("then please come back when you feel like playing challanger")
        
            
            
