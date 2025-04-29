# DS5100_Final_Project
Final Project: Monte Carlo Simulated Games


## Project Overview

This project implements a command-line Scrabble Helper tool using Python.  
Given a list of valid Scrabble words and letter-to-score mappings, the program identifies the highest-scoring word that can be formed from a user-provided (or randomly generated) set of letters.

This project is part of the **Programming for Data Science (DS5100)** course at the University of Virginia.



## What the Program Does

- Loads letter scores from `english_letters.txt`
- Loads valid Scrabble words from `scrabble_words.txt`
- Accepts user input (or generates random letters)
- Computes all valid words that can be formed
- Scores each valid word using standard Scrabble rules
- Returns the **highest-scoring word** and its score


## Files in This Repo

| File | Description |
|------|-------------|
| `final_project.ipynb` | Jupyter notebook implementing the Scrabble Helper |
| `english_letters.txt` | Letter-to-score mapping (A 1, B 3, etc.) |
| `scrabble_words.txt` | Valid English Scrabble words |
| `README.md` | This file |
| `.gitignore` | Ignores temp and Jupyter checkpoint files |
| `LICENSE` | Open source license for this project |

---

## How to Run It

1. Clone the repo:
   In bash environment:
   git clone https://github.com/YOUR_USERNAME/DS5100_Final_Project.git
   cd DS5100_Final_Project