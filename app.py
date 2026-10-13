import random
import streamlit as st

# FIX: ChatGPT helped me move the game logic into logic_utils.py.
# This keeps the game interface separate from the guessing logic.
from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

# Game settings
st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}

attempt_limit = attempt_limit_map[difficulty]
low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

# FIX: ChatGPT helped me understand how session state works.
# Session state remembers game information when Streamlit reruns.
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

# FIXME: The original counter started at 1 before any guesses.
# FIX: ChatGPT suggested starting at 0 so attempts count correctly.
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

# FIX: Initialize the input key before using it.
# ChatGPT helped me fix an AttributeError caused by this missing variable.
if "guess_key" not in st.session_state:
    st.session_state.guess_key = 0

# FIX: Track difficulty so a difficulty change starts a fresh game.
if "current_difficulty" not in st.session_state:
    st.session_state.current_difficulty = difficulty

if st.session_state.current_difficulty != difficulty:
    st.session_state.current_difficulty = difficulty
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.guess_key += 1

st.subheader("Make a guess")

# FIX: Display the correct range and remaining attempts.
st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {max(0, attempt_limit - st.session_state.attempts)}"
)

# Debug information helped me compare guesses with the secret number.
# ChatGPT suggested using this section to reproduce the bugs.
with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

# FIX: Changing the input key clears the old guess on a new game.
raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}_{st.session_state.guess_key}"
)

col1, col2, col3 = st.columns(3)

with col1:
    submit = st.button("Submit Guess 🚀")

with col2:
    new_game = st.button("New Game 🔁")

with col3:
    show_hint = st.checkbox("Show hint", value=True)

# FIXME: The original New Game button did not reset game status.
# FIX: ChatGPT suggested resetting all game variables.
# I tested this by winning and starting another game successfully.
if new_game:
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.guess_key += 1
    st.rerun()

# Stop accepting guesses once the game is over.
if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    # FIX: Validate input before counting it as an attempt.
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.error(err)

    elif guess_int < low or guess_int > high:
        st.error(f"Enter a number between {low} and {high}.")

    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)

        # FIXME: The original code sometimes converted the secret to a string.
        # FIX: ChatGPT suggested keeping the secret as an integer.
        # This makes number comparisons consistent.
        outcome, message = check_guess(
            guess_int,
            st.session_state.secret
        )

        if show_hint:
            st.warning(message)

        # FIX: Use the corrected scoring function from logic_utils.py.
        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"

            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )

        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"

            st.error(
                f"Out of attempts! "
                f"The secret was {st.session_state.secret}. "
                f"Score: {st.session_state.score}"
            )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
