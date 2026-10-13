# FIX: ChatGPT helped me move the game logic out of app.py.
# This makes the functions easier to understand and test using pytest.


def get_range_for_difficulty(difficulty: str):
    # FIX: Corrected the difficulty ranges.
    # The original Hard mode had a smaller range than Normal.
    if difficulty == "Easy":
        return 1, 20

    if difficulty == "Normal":
        return 1, 100

    if difficulty == "Hard":
        return 1, 200

    return 1, 100


def parse_guess(raw: str):
    # FIX: ChatGPT suggested improving input validation.
    # This prevents empty inputs, letters, and decimals from being accepted.
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)
        return True, value, None

    except ValueError:
        return False, None, "Enter a valid whole number."


def check_guess(guess, secret):
    # FIXME: The original hints were backwards.
    # FIX: ChatGPT helped me identify and correct the comparison messages.
    # I tested this with pytest, and the high and low guess tests passed.

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        # A high guess means the player needs to guess lower.
        return "Too High", "📉 Go LOWER!"

    # A low guess means the player needs to guess higher.
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    # FIX: ChatGPT suggested correcting the score calculation.
    # A win earns points based on attempts used.
    # Incorrect guesses subtract 5 points.

    if outcome == "Win":
        points = max(10, 100 - 10 * attempt_number)
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score


    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
