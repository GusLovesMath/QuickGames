def dice_roll(Count=True, Rolls=False, Stats=True, Hist=False):

    """
    A dice simulator the rolls m dice n times.
    Count=True returns the frequency each value appears.
    Rolls=True prints the entire list of values rolled.
    Hist=True plots a histogram of the rolls.
    """
    
    from random import randint

    m = int(input('Number of dice you would like to roll: '))
    n = int(input(f'Number of times you would like to roll {"{:,}".format(m)} dice: '))
    print(f'You have choosen to roll {"{:,}".format(m)} dice {"{:,}".format(n)} times.\n')


    # Restricted amount of dice that can be rolled
    if m > 1200:
        print('That is too many dice my friend.')

    else:
        rolls = []

        # Goes through n rolls and sums them for the amount if m dice rolled
        for i in range(n):
            rolls.append(sum([randint(1, 6) for dices in range(m)]))

        if n < 20 or (Rolls is True and n <= 750):
            print(rolls)

        else:
            vals = rolls[:10] + ['....'] + rolls[-10:]
            print(vals)

            if n > 750:
                print('Will not show list of values for number of rolls greater than 750.')


        # Counts the frequency of values rolled
        if Count and m <= 40:
            from collections import Counter
            orderd = Counter(rolls)
            # orders rolls from smalles rolled to greatest with its frequency
            print(sorted(orderd.items(), key=lambda i: i[0]))
            
        else:
            print('Counter is unavailable for number of dice greater than 40.')


        # printing statistics
        if Stats:
            from pandas import DataFrame
            print('Here are the general statistics:')
            df = DataFrame(rolls)
            print(df.describe())


        # Plots a histogram of values rolled
        if Hist:
            import matplotlib.pyplot as pl
            import numpy as np
            # if using Jupyter Notebooks uncomment this line for better plot display
            #%config InlineBackend.figure_format = 'retina'
            pl.matplotlib.rcParams.update({'font.size': 14})
            pl.figure(figsize=(9, 6.5))
            pl.hist(rolls, bins=np.arange(min(rolls), max(rolls) + 1, 1), color='c', edgecolor='black', linewidth=0.5)
            pl.title(f'Histogram of {"{:,}".format(m)} Dice Rolled {"{:,}".format(n)} Times')
            pl.ylabel('Frequency Occured')
            pl.xlabel('Dice Roll Values')
            pl.grid(alpha=0.1)
            pl.show()

dice_roll(Count=True, Rolls=True, Stats=True, Hist=True)