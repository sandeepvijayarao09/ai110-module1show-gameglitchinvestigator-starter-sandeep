from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, message = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, message = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, message = check_guess(40, 50)
    assert result == "Too Low"

def test_score_too_high_even_attempt():
    # Ensure that guessing too high on any attempt (including even attempts)
    # properly subtracts 5 points from the score, not adding them.
    initial_score = 100
    new_score = update_score(initial_score, "Too High", attempt_number=2)
    assert new_score == 95, "Score should decrease by 5 points for a wrong answer."

def test_hint_directions():
    # Ensure that if the player guesses too high, they get told to go lower.
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message, "Hint should tell the user to go lower"

    # Ensure that if the player guesses too low, they get told to go higher.
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message, "Hint should tell the user to go higher"
