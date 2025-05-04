# DS5100 Final Project

**Metadata**  
- **Author:** Hang Yu, zdd3ga  
- **Course:** DS5100 � Programming for Data Science  
- **Date:** May 2025  
- **License:** MIT  

## Synopsis

This repository implements three core classes for rolling and analyzing weighted dice:

1. **Die**  
```python
import numpy as np
from die import Die

faces = np.array(['A', 'B', 'C'])
d = Die(faces)
d.change_weight('A', 2.0)       # make 'A' twice as likely
rolls = d.roll(5)               # e.g. ['A','C','B','A','A']
print(d.show())                 # DataFrame of faces & weights
```

2. **Game**
```python
from game import Game

dice = [Die(faces) for _ in range(3)]
game = Game(dice)
game.play(100)                  # roll 3 dice 100 times
wide_df   = game.show_results() # wide format
	
# narrow format: MultiIndex 	+ one column
narrow_df = game.show_results('narrow')
```

3. **Analyzer**
```python
from analyzer import Analyzer

analyzer = Analyzer(game)
print(analyzer.jackpot())               # count of all?same rolls
print(analyzer.face_counts_per_roll())  # DataFrame: roll � face counts
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