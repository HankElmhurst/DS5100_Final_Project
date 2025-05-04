# DS5100 Final Project

**Metadata**  
- **Author:** Hang Yu, zdd3ga  
- **Course:** DS5100 Programming for Data Science  
- **Date:** May 2025  
- **License:** MIT  

## Synopsis

The **DS5100 Final Project** provides three modular Python classes for modeling, playing, and analyzing weighted dice and related games:

1. **Die**
Create a custom die with any set of faces and weights.

```python
import numpy as np
from die import Die

faces = np.array(['A', 'B', 'C'])
d = Die(faces)
d.change_weight('A', 2.0)       # make 'A' twice as likely
rolls = d.roll(5)               # e.g. ['A','C','B','A','A']
print(d.show())                 # View current faces & weights in a data frame
```

2. **Game**
Simulate repeated rolls of one or more dice.

```python
from game import Game

dice = [Die(faces) for i in range(3)]
game = Game(dice)
game.play(100)                          # roll 3 dice 100 times
wide_df   = game.show_results()         # wide format
narrow_df = game.show_results('narrow') # Narrow(stacked) format
```

3. **Analyzer**
Analyze statistical patterns from a completed game.

```python
from analyzer import Analyzer

analyzer = Analyzer(game)
print(analyzer.jackpot())               # count of all?same rolls
print(analyzer.face_counts_per_roll())  # DataFrame: roll face counts
print(analyzer.combo_count())           # combos & their counts
print(analyzer.permutation_count())     # permutations & their counts
```

## API

Die
* __init__(self, faces: np.ndarray)
* change_weight(self, face: Any, weight: float) -> None
* roll(self, n: int = 1) -> List[Any]
* show(self) -> pd.DataFrame
Game
* __init__(self, dice: List[Die])
* play(self, n: int) -> None
* show_results(self, form: str = 'wide') -> pd.DataFrame
Analyzer
* __init__(self, game: Game)
* jackpot(self) -> int
* face_counts_per_roll(self) -> pd.DataFrame
* combo_count(self) -> pd.DataFrame
* permutation_count(self) -> pd.DataFrame


## Installation
```bash
# for development
pip install -e .