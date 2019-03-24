#import random module
import random

#selecting random word
def choose(): 
    # list of words 
    words = ['game of thrones', 'the umbrella academy', 'the walking dead', 'the order', 
            'true detective', 'the window', 'shameless', 'dirty john', 
            'arrow', 'pretty little liars', 'the big band theory','the flash','suits',
             'the good doctor','friends','lost','mordern family','sherlock','dexter','you',
             'stranger things','black mirror','the crown','house of cards','queer eye',
             'narcos','13 reasons why','making a murderer','dear white people','daredevil']
    pick = random.choice(words) 

    return pick


#Function to shuffle the words
def jumble(_string): 
	# sample() method suffling the characters of the word 
	jumbled = []
	words = _string.split(' ')
	for word in words:
		random_word = random.sample(word, len(word)) 

		# join() mehtod join the elements 
		# of the iterator(e.g. list) with particular character . 
		jumbled.append(''.join(random_word))
	return ' '.join(jumbled)

# Fucntion for showing final score. 
def thank(p1n, p1): 
    print(p1n, 'Your score is :', p1) 

    print('Thanks for playing...') 


# Function for playing the game. 
def play(): 
    # enter player name 
    p1name = input("player , Please enter your name :")  

    # variable for counting score. 
    pp1 = 0
    
    # list to store selected elements
    # to avoid repetition
    crossed = []
    
    # keep looping 
    for z in range(0,10): 

        # choose() function calling 
        picked_word = choose() 
        
        # check for repetition
        if picked_word in crossed:
            picked_word = choose()
        
        # add element to already 
        # selected elements         
        crossed.append(picked_word)
        
        # jumble() fucntion calling 
        qn = jumble(picked_word) 
        print("jumbled word is :", qn) 

        # pLAYING

        ans = input("what is in your mind? ") 

        # checking ans is equal to picked_word or not 
        if ans == picked_word:
                    # incremented by 1 
                    pp1 = pp1 + 1
                    print('Your score is :', pp1) 
                
        else:
            print("Better luck next time...correct word is :", picked_word)  
    thank(p1name , pp1) 


if __name__ == '__main__': 
    
    # play() function calling 
    play() 
