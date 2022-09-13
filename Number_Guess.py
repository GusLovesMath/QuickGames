def Guess_Number(n=10):
    
    """
    Game where you have three tries to guess the right number.
    """
    import random as r

    number = r.randint(0 , n + 1)
    guess_number = ['first', 'second', 'third']

    Guess = 0
    while Guess <= 3:

        if Guess == 3:
            print('You lost the game, run again to try again :(')
            break

        elif int(input(f'What is your {guess_number[Guess]} guess of range 0 to {n}: ')) != number:
            Guess +=1
            print('Try again :(\n')

        else:
            print(f'You guessed the right number, {number}!')
            break
        
# Run it!
#Guess_Number()
