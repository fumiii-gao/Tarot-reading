# AuraTarot — Minimalist Tarot Reading

> A lightweight, zero-dependency Python tool for instant Tarot divination. Get your daily guidance, quick answers, or past-present-future insights straight from the terminal.

##  Features

- **Daily Fortune**: Draws a single Tarot card to reflect your overall energy, mood, and focus for the day.
- **Yes or No**: Need a quick answer? Focus on your question and get a definitive Yes/No response backed by card upright/reversed meanings.
- **Classic 3-Card**: Draws three cards representing the Past, Present, and Future of your current situation for deeper reflection.

## 🛠️ Architecture & Choices

- **Language**: Python 3.x (Standard Library only)
- **Zero Dependencies**: Intentionally built using built-in modules (`random`, `time`) to ensure instant execution with zero environment configuration.
- **Data Structure**: Card profiles (names, arcana, upright/reversed meanings) are decoupled into a clean data dictionary for easy future expansion (e.g., migrating to JSON/Database).

## 🚀 How to Run Locally

Clone the repository and run the main script directly—no `pip install` required!

```bash
git clone [https://github.com/fumiii-gao/Tarot-reading.git]
cd Tarot-reading
python main.py
