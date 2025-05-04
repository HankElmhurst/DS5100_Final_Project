import numpy as np
import pandas as pd
import random

class Die:
    """
    A Die has faces and associated weights, and can be rolled to select a face.
    Faces must be unique. Weights default to 1.0 and can be updated.
    """

    def __init__(self, faces):
        """
        Initializes the Die object with faces and equal weights.

        Args:
            faces (np.ndarray): A NumPy array of unique face values (strings or numbers).

        Raises:
            TypeError: If faces is not a NumPy array.
            ValueError: If face values are not unique.
        """
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be provided as a NumPy array.")
        if len(np.unique(faces)) != len(faces):
            raise ValueError("Face values must be unique.")

        self._df = pd.DataFrame({"weight": np.ones(len(faces))}, index=faces)

    def change_weight(self, face, new_weight):
        """
        Change the weight for a given face.

        Args:
            face: The face value whose weight is to be changed.
            new_weight: A numeric value (int or float) for the new weight.

        Raises:
            IndexError: If face is not in the die.
            TypeError: If new_weight is not numeric or castable as float.
        """
        if face not in self._df.index:
            raise IndexError("Face not found in the die.")
        try:
            self._df.loc[face, "weight"] = float(new_weight)
        except ValueError:
            raise TypeError("Weight must be numeric or castable to float.")

    def roll(self, n_rolls=1):
        """
        Roll the die a number of times.

        Args:
            n_rolls (int): Number of times to roll. Defaults to 1.

        Returns:
            list: List of outcomes.
        """
        return random.choices(
            population=self._df.index.tolist(),
            weights=self._df["weight"].tolist(),
            k=n_rolls
        )

    def show(self):
        """
        Show current die faces and weights.

        Returns:
            pd.DataFrame: A copy of the die's internal state.
        """
        return self._df.copy()