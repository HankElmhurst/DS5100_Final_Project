import unittest
import numpy as np
import pandas as pd
from die import Die
from game import Game
from analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        faces = np.array([1,2,3])
        dice = [Die(faces) for _ in range(3)]
        self.game = Game(dice)
        self.game.play(5)
        self.analyzer = Analyzer(self.game)

    def test_init_requires_game_object(self):
        with self.assertRaises(ValueError):
            Analyzer("not a game")

    def test_jackpot_count(self):
        # force two jackpots
        self.analyzer.game._play_df = pd.DataFrame({ 
            0:[1,1], 
            1:[1,1], 
            2:[1,1] 
            }, index=[0,1])
        self.assertEqual(self.analyzer.jackpot(), 2)

    def test_face_counts_per_roll_structure(self):
        df = self.analyzer.face_counts_per_roll()
        self.assertIsInstance(df, pd.DataFrame)
        # columns should match the full set of possible faces
        expected_faces = sorted(self.analyzer.game.dice[0].
                                show()     # get the full set of faces via Die.show()
                                .index.tolist())
        self.assertListEqual(sorted(df.columns.tolist()), expected_faces)

    def test_combo_count_returns_dataframe(self):
        df = self.analyzer.combo_count()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('Count', df.columns)

    def test_permutation_count_returns_dataframe(self):
        df = self.analyzer.permutation_count()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('Count', df.columns)

if __name__ == '__main__':
    unittest.main(verbosity=2)
