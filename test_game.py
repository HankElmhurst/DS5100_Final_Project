import unittest
import numpy as np
import pandas as pd
from die import Die
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        faces = np.array(['A','B'])
        d1 = Die(faces)
        d2 = Die(faces)
        self.game = Game([d1, d2])

    def test_play_and_show_wide(self):
        self.game.play(3)
        df = self.game.show_results()
        self.assertEqual(df.shape, (3, 2))

    def test_show_narrow_format(self):
        self.game.play(3)
        df = self.game.show_results(form='narrow')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(df.index, pd.MultiIndex)
        self.assertEqual(df.shape[1], 1)

    def test_show_invalid_format_raises(self):
        self.game.play(1)
        with self.assertRaises(ValueError):
            self.game.show_results(form='invalid')

if __name__ == '__main__':
    unittest.main(verbosity=2)
