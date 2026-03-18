# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose: To guess a randomly generated secret number within a limited amount of attempts, utilizing higher/lower hints.
- [x] Detail which bugs you found: 1) The 'secret' was stringified on even attempts causing hints to break. 2) The score inexplicably increased by 5 points for a wrong guess on an even attempt. 3) The hint messages were contradictory (e.g., Too High outputted "📈 Go HIGHER!").
- [x] Explain what fixes you applied: Refactored the game logic into `logic_utils.py` to be tested independently. Removed the stringification bug in `app.py`. Corrected the `update_score` mathematics to consistently subtract 5 for a wrong answer. Swapped the "HIGHER" and "LOWER" string values in `check_guess`.

## 📸 Demo

- [x] Demo completed and verified via Streamlit and Pytest locally. The repository is functioning correctly.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
