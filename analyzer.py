import pandas as pd
from game import Game

class Analyzer:
    """
    Analyzer performs statistical analysis on a Game object's most recent play.
    """

    def __init__(self, game):
        """
        Initializes the Analyzer with a Game object.

        Args:
            game (Game): A Game instance.

        Raises:
            ValueError: If input is not a Game instance.
        """
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object.")

        self.game = game

    def jackpot(self):
        """
        Counts how many times all dice rolled the same face, 
        in the most recent roll.


        Returns:
            int: Number of jackpot rolls.
        """    
        # Access the private results DataFrame
        df = self.game.show_results(form='wide')
        
        # A jackpot is a row where all values are identical
        # `nunique(axis=1)` gives number of distinct faces per row
        jackpot_mask = df.nunique(axis=1) == 1
        
        # Sum the True values and convert to int
        return int(jackpot_mask.sum())

    def face_counts_per_roll(self):
        """
        Counts occurrences of each face per roll.

        Returns:
            pd.DataFrame: Roll index, face columns, count values.
        """
        df = self.game.show_results()
        return df.apply(lambda row: row.value_counts(), axis=1).fillna(0).astype(int)

    def combo_count(self):
        """
        Counts order-independent combinations and their frequencies.

        Returns:
            pd.DataFrame: MultiIndex of combinations with count.
        """
        df = self.game.show_results()
        combos = df.apply(lambda row: tuple(sorted(row)), axis=1)
        combo_counts = combos.value_counts().to_frame('Count')
        combo_counts.index.name = 'Combination'
        return combo_counts

    def permutation_count(self):
        """
        Counts order-dependent permutations and their frequencies.

        Returns:
            pd.DataFrame: MultiIndex of permutations with count.
        """
        df = self.game.show_results()
        perms = df.apply(lambda row: tuple(row), axis=1)
        perm_counts = perms.value_counts().to_frame('Count')
        perm_counts.index.name = 'Permutation'
        return perm_counts

