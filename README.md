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

- [ ] Describe the game's purpose.
The purpose of this game is to guess a secret number within a limited number of attempts. The game gives hints to help players figure out whether their guesses are too high or too low. Players can also earn points based on their guesses.
- [ ] Detail which bugs you found.
When I first ran the game, I noticed that the hints were backwards. For example, when the secret number was 51 and I guessed 60, the game told me to go higher instead of lower. I also noticed that the attempt counter started at 1 even though I hadn't guessed anything yet. Another bug happened after winning because clicking New Game changed the secret number, but I couldn't play again until I refreshed the page.
- [ ] Explain what fixes you applied.
I used ChatGPT to help me understand the problems and figure out how to fix them. I corrected the hint messages, changed the attempt counter to start at 0, and updated the New Game button to reset the game status. I also moved the guessing functions into logic_utils.py to make the code easier to understand and test. After making these changes, I ran three pytest tests, and all three passed.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The player starts a new game on Normal difficulty with 8 attempts available.
2. The player enters 40, and the game says "Go HIGHER!" because the guess is too low.
3. The player enters 70, and the game says "Go LOWER!" because the guess is too high.
4. The player's score decreases by 5 points for each incorrect guess.
5. The player enters 50, and the game displays "Correct!" and announces the win.
6. The player clicks New Game, and the game resets so another round can begin.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results


I used pytest to check that the game recognizes correct guesses and gives the proper hints for guesses that are too high or too low.

tests/test_game_logic.py::test_winning_guess PASSED                  [ 33%]
tests/test_game_logic.py::test_guess_too_high PASSED                 [ 66%]
tests/test_game_logic.py::test_guess_too_low PASSED                  [100%]


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
