import unittest
import numpy as np
import pandas as pd
from die import Die

class TestDie(unittest.TestCase):
    def setUp(self):
        self.faces = np.array([1, 2, 3])
        self.die = Die(self.faces)

    def test_init_requires_numpy_array(self):
        with self.assertRaises(TypeError):
            Die([1, 2, 3])  # not a numpy array

    def test_init_requires_distinct_faces(self):
        with self.assertRaises(ValueError):
            Die(np.array([1, 1, 2]))  # duplicates

    def test_default_weights(self):
        df = self.die.show()
        self.assertTrue((df['weight'] == 1.0).all())

    def test_change_weight_invalid_face(self):
        with self.assertRaises(IndexError):
            self.die.change_weight(999, 2.0)

    def test_change_weight_invalid_weight_type(self):
        with self.assertRaises(TypeError):
            self.die.change_weight(1, "invalid")

    def test_roll_returns_list_of_correct_length(self):
        result = self.die.roll(5)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 5)

    def test_show_returns_copy(self):
        df1 = self.die.show()
        df2 = self.die.show()
        df1.iloc[0,0] = None
        self.assertNotEqual(df1.iloc[0,0], df2.iloc[0,0])

if __name__ == '__main__':
    unittest.main(verbosity=2)
