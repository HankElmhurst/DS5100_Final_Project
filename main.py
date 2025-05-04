import numpy as np
import pandas as pd
from die import Die
from game import Game
from analyzer import Analyzer

# Step 1: Define faces as a NumPy array (requirement)
faces = np.array(['A', 'B', 'C'])

# Step 2: Create 3 Die objects with the same face array
d1 = Die(faces)
d2 = Die(faces)
d3 = Die(faces)

# Step 3: Initialize a Game with the list of dice
game = Game([d1, d2, d3])

# Step 4: Play the game 1000 times
game.play(1000)

# Step 5: Show and verify sample results
print("Sample play results (first 5 rolls):")
print(game.show_results().head())

# Step 6: Create an Analyzer with the Game
analyzer = Analyzer(game)

# Step 7: Run full analysis
jackpot_count = analyzer.jackpot()
face_counts_df = analyzer.face_counts_per_roll()
combo_counts_df = analyzer.combo_count()
perm_counts_df = analyzer.permutation_count()

# Step 8: Print results
print(f"\nNumber of jackpots: {jackpot_count}")
print("\nFace counts (first 5 rows):")
print(face_counts_df.head())

print("\nTop 3 combinations:")
print(combo_counts_df.head(3))

print("\nTop 3 permutations:")
print(perm_counts_df.head(3))

