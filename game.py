import pandas as pd
from die import Die

class Game:
    """
    A Game object consists of rolling one or more Die objects a given number of times.
    Stores only the result of the most recent play.
    """

    def __init__(self, dice):
        """
        Initializes a Game with a list of similar Die objects.

        Args:
            dice (list): A list of Die objects.
        """
        self.dice = dice
        self._play_df = pd.DataFrame()

    def play(self, num_rolls):
        """
        Rolls the dice a given number of times and stores the result.

        Args:
            num_rolls (int): Number of times to roll the dice.
        """
        results = {i: die.roll(num_rolls) 
                   for i, die in enumerate(self.dice)}
        self._play_df = pd.DataFrame(results)
        self._play_df.index.name = 'Roll'

    def show_results(self, form='wide'):
        """
        Returns the results of the most recent play.

        Args:
            form (str): Either 'wide' (default) or 'narrow'.

        Returns:
            pd.DataFrame: Results in the specified format.

        Raises:
            ValueError: If form is not 'wide' or 'narrow'.
        """
        if form == 'wide':
            return self._play_df.copy()
        elif form == 'narrow':
            # stack the output into a 1 column data frame named "outcome"
            return self._play_df.stack().to_frame(name='outcome')
        else:
            raise ValueError("Form must be 'wide' or 'narrow'.")