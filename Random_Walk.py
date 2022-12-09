def random_walks(Print=True, Stats=False, Hist=False):

    """
    A simulator that takes m walkers which take n steps and returns
    the outcome
    Print will print the outcome of the displacements of the walkers.
    Stats will print the general statistical outcomes.
    Hist will plot a histogram of the outcomes.
    """

    import numpy as np
    from random import randint

    n = int(input(f'Number of steps to take: '))
    m = int(input(f'Number of walkers that will take {n} steps: '))

    print(f'You have choosen {"{:,}".format(m)} walkers that will take {"{:,}".format(n)} steps. \n')

    # function that goes on one random walk
    def walks():
        steps = np.zeros(n)

        for i in range(1, n):
            step = randint(0, 1)

            if step == 1:
                steps[i] = steps[i - 1] + 1

            else:
                steps[i] = steps[i - 1] - 1

        return steps

    # going through m random walks with n steps.
    rand_walks = []
    for i in range(m):
        rand_walks.append(walks()[-1])

    # printing values of outcome
    if (Print is True and m <= 5000):
        print(rand_walks)

    else:
        print('Will only print outcome for number of walkers less than 50.')

    # printing statistics
    if Stats:
        from pandas import DataFrame
        print('Here are the general statistics:')
        df = DataFrame(rand_walks)
        print(df.describe())

    # plotting histogram of data
    if Hist:
        import matplotlib.pyplot as pl
        # if in Jupyter Notebooks uncomment line for better plot display
        #%config InlineBackend.figure_format = 'retina'
        pl.matplotlib.rcParams.update({'font.size': 14})
        pl.figure(figsize=(9, 6.5))
        pl.hist(rand_walks, bins=np.arange(min(rand_walks), max(rand_walks) + 1, 1), color='C3', edgecolor='black', linewidth=0.5)
        pl.title(f'Displacements of {"{:,}".format(m)} Random Walkers Taking {"{:,}".format(n)} of Steps')
        pl.xlabel('Distance from Origin of The Walkers')
        pl.ylabel('Number of Occurances')
        pl.grid(alpha=0.1)
        pl.show()

random_walks(Print=True, Stats=True, Hist=True)

