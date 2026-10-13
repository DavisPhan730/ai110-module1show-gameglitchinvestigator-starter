# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guessed 60 when secret was 51|Told me to guess lower|Said "Go HIGHER!"|Wrong hint displayed|
|Started game without guessing|Attempts should start at 0|Attempts started at 1|No error shown|
|Won, clicked New Game, then guessed new secret|Game should accept new guesses|Nothing happened until I refreshed|No visible response|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
I used ChatGPT to help me set up the game, understand the bugs, and figure out what I should test. One helpful suggestion was to use Developer Debug Info to compare my guesses with the secret number, which helped me confirm that the hints were backwards. I also learned that the New Game button wasn't fully resetting the game because refreshing the page made it work again. I haven't rejected a specific AI code suggestion yet, but I plan to review any suggested fixes before using them instead of just copying everything.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
I tested the game by entering different numbers and checking whether the results made sense. For example, when the secret number was 51, I entered 60 and the game incorrectly told me to go higher. I also tested the New Game button after winning and noticed that I couldn't submit another guess until I refreshed the page. These tests helped me identify the problems, but I still need to rerun them after fixing the code to make sure everything works properly.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I learned that Streamlit reruns the Python script whenever you interact with certain parts of the app, like clicking a button. Session state is what helps the app remember information, such as your score, attempts, and secret number, between those reruns. Without session state, the game could lose important information every time the page updates. I also learned that resetting a game means updating all the necessary state variables, not just changing the secret number.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One habit I want to keep using is testing different situations instead of assuming the program works after one successful attempt. Next time I use AI for coding, I want to ask it to explain the problem before suggesting changes so I understand what I'm doing. This project showed me that AI-generated code can look correct at first but still have bugs that only appear when you actually test it.
