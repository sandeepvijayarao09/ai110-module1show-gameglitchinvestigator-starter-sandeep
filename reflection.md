# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked visually fine, but playing it revealed functional bugs. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. **The hints lie on even attempts:** If you made an even-numbered attempt (like the 2nd or 4th attempt), the hints were completely incorrect and based on string comparisons.
2. **The score goes haywire:** Whenever a wrong guess was submitted on an even attempt, the score would randomly *increase* by 5 points instead of penalizing the player.
3. **Contradictory Hints:** The game logic properly told you your guess was "Too High", but the actual message displayed instructed you to go "HIGHER!", which is contradictory.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used my AI Assistant (Agent) for this project through VS Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI successfully identified the `TypeError` stringification logic in the starter app.py. It pointed out that converting `secret` to a string on even attempts caused lexicographical number comparison in `logic_utils.py` instead of numerical comparison, completely throwing off the hints. I verified this by looking at how `st.session_state.attempts % 2 == 0` triggered this branch, and removed that logic.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When first installing dependencies, the AI agent tried to simply run `pytest tests/test_game_logic.py`, but this failed with a module import error because `logic_utils` wasn't in the Python path. It had to fix its command to add `PYTHONPATH=.` in the terminal to allow `pytest` to find the local file.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I verified fixes by writing automated unit tests and also manually playing the streamit application.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I wrote `test_score_too_high_even_attempt` in `test_game_logic.py` that passed an initial score of 100 on attempt 2 (even) and verified that the score dropped to 95. This proved that my fix to the arbitrary `+ 5` score logic worked mathematically.
- Did AI help you design or understand any tests? How?
Yes, the AI agent wrote the test fixtures to specifically target the directional hint strings ("HIGHER" vs "LOWER") to ensure they matched the outcome ("Too Low" or "Too High").

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the entire python script every time a user interacts with a widget (like clicking a button). `session_state` is a special dictionary that allows streamlit to "remember" variables across these reruns, like the player's current score or attempt count; otherwise, those variables would reset to zero every single time the script reran.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to continue the habit of writing targeted pytest test cases for mathematically intense calculations like the scoring mechanism to mathematically prove accuracy rather than manually clicking 20 times to verify.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I will ensure my environment is fully virtualized and my pythonpath is set *before* asking the AI to run tests to save time on setup errors.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It taught me that AI is not infallible; it can easily generate logic that looks right but functions completely backward in edge cases like type mismatches. Human review is absolutely essential.
