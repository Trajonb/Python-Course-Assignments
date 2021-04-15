def Number_Guessing_Game():
    print('ᴡᴇʟᴄᴏᴍᴇ! My name is Trajon, what is yours?')
    player_name = str(input())
    with open('Highscore1.txt','w+') as f:
        f.write(player_name + ':')
    replay = 'Y' #makes the game able to rerun if they select 'Y" after winning or losing
    games_played = 0
    running_highscore = 5
    current_highscore = 0 
    while replay == 'Y' or replay == 'y': #replays game 
        from random import randint
        my_number = randint(1,100) #a random number is created 
        guesses = 0
        print('Lets Play A Game ' + player_name) 
        print('I am thinking of a integer between 1 and 100')
        print('Now it is your turn to guess what it is!')
        print('Be careful though! You only get 5 tries!')
        #print(my_number)
        while guesses < 5: #keeps track of gueesing to know when to end game 
            try_loop = True
            while try_loop == True:
                try:
                    guess = input('Guess: ')
                    guess = int(guess)
                    try_loop = False
                except:
                    print('oops! Thats not right!')
            guesses = guesses + 1

            if guess < my_number: #lets player know they guessed to low and to try again
                print('Your guess is too low!')
                print('Try again!')

            if guess > my_number: #lets player know they guessed to high and to try again 
                print('Your guess is too high!')
                print('Try again!')

            if guess == my_number:
                break
        if guess == my_number:
            guesses = str(guesses)
            if int(guesses) == 1: #if player guesses it with in one try
                print('Wow, I cant believe you guessed it in ' + str(guesses) + ' try.')
                games_played = games_played + 1
                guesses =int(guesses)
                current_highscore = guesses 
                if current_highscore < running_highscore:
                    running_highscore = current_highscore
                print('Highscore: ', running_highscore)
                replay = input('Would you like to play again?(Y/N)')
            elif int(guesses) > 1: #if player gueeses it after more than 1 try 
                print('Wow, I can not believe you guessed it in ' + str(guesses) + ' tries.')
                games_played = games_played + 1
                guesses =int(guesses)
                current_highscore = guesses 
                if current_highscore < running_highscore: #if the current highscore is lower than the running
                    running_highscore = current_highscore  #one it makes the current highscore the new highscore
                print('Highscore: ', running_highscore)
                replay = input('Would you like to play again? (Y/N)')
                
        if guess != my_number:
            my_number = str(my_number)
            print('Just kidding! You failed! The number I was thinking of is ' + my_number + '.')
            games_played = games_played + 1 
            guess = int(guesses)
            current_highscore = guesses 
            if current_highscore < running_highscore: #same as above 
                running_highscore = current_highscore
            print('HighScore: ', running_highscore)
            replay = input('Would you like to play again?(Y/N):')
    if replay == 'N' or replay == 'n': #if player select 'N' the game will end by maing replay='N"
        print('Ok! Goodbye!')
            
Number_Guessing_Game()            
    
        
