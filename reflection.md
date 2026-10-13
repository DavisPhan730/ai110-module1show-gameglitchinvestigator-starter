# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, everything looked normal, but I started noticing problems while playing. When the secret number was 51 and I guessed 60, the game told me to go higher instead of lower. I also noticed that the attempt counter started at 1 even though I hadn't guessed anything yet. Another issue happened after I won because clicking New Game changed the secret number, but I couldn't submit another guess until I refreshed the page. I figured these problems were related to the hint logic, attempt counter, and game reset code.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|-------|-------------------|-----------------|------------------------|-------------------------|
|Guessed 60 when secret was 51|Told me to guess lower|Said "Go HIGHER!"|Wrong hint displayed|app.py - check_guess()|
|Started game without guessing|Attempts should start at 0|Attempts started at 1|No error shown|app.py - session-state initialization|
|Won, clicked New Game, then guessed new secret|Game should accept new guesses|Nothing happened until I refreshed|No visible response|app.py - New Game/reset logic

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used ChatGPT to help me understand the bugs, fix the code, and create tests. One suggestion that worked was resetting the game status to "playing" when starting a new game, and I verified it by winning and starting another round without refreshing. ChatGPT also suggested running pytest tests, but the original tests it suggested didn't match how my check_guess() function returned results. I had to change the tests so they checked the outcome and message separately instead of comparing the whole result to one string. After making that change, I ran pytest again and all three tests passed.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I checked whether my fixes worked by running the game again and comparing the results to what happened before. I also used pytest to test three situations: guessing the correct number, guessing too high, and guessing too low. All three tests passed, which showed that the guessing logic was working correctly. I also tested the New Game button after winning and confirmed that I could start another round without refreshing the browser. ChatGPT helped me create the tests and understand why they were failing before I corrected them.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I learned that Streamlit reruns the Python script whenever you interact with certain parts of the app, like clicking a button. Session state helps the app remember information such as your score, attempts, and secret number between those reruns. Without session state, the game could lose important information whenever it updates. I also learned that starting a new game means resetting all the important variables, not just generating a new secret number.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep using is testing different situations instead of assuming the program works after one successful attempt. Next time I use AI for coding, I want to ask it to explain the problem before suggesting changes so I understand what I'm doing. I also want to check AI-generated code more carefully because I ran into errors while trying to use some of the suggestions. This project showed me that AI-generated code can look correct but still have problems that only show up when you actually run and test it.
