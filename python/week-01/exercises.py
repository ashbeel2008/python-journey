"""
Week 1 — Python Fundamentals

Fill in each function. Run the tests with:

    python test_exercises.py

Rules:
- Type the code yourself.
- Don't change the function names or parameters — the tests depend on them.
- Remove the `pass` and replace it with your code.
"""


def welcome(name):
    """Return 'Welcome, <name>!'"""
    # Hint: f"Welcome, {name}!"
    pass


def player_status(name, health):
    """Return '<name>: <health> HP'"""
    pass


def format_time(total_seconds):
    """Return 'MM:SS' for the given number of seconds.
    Minutes may exceed 59 (3600 -> '60:00').
    """
    # Hint: divmod(total_seconds, 60)
    # Hint: f"{minutes:02d}:{seconds:02d}"
    pass


def check_health(health):
    """Return 'Alive' if health > 0, otherwise 'You died'."""
    pass


def count_items(inventory):
    """Return the number of items in the list."""
    pass


def apply_damage(health, damage):
    """Return health minus damage, but never below 0."""
    # Hint: max(0, ...)
    pass


def best_score(scores):
    """Return the highest score, or None if the list is empty."""
    pass


def count_blocks(mined):
    """Return a dict counting each block.
    ['dirt', 'stone', 'dirt'] -> {'dirt': 2, 'stone': 1}
    """
    # Hint: start with an empty dict, loop, and use .get(block, 0) + 1
    pass


def save_profile(path, profile):
    """Write `profile` (a dict) to `path` as JSON."""
    # Hint: import json at the top of this file
    # Hint: with open(path, "w", encoding="utf-8") as f:
    pass


def load_profile(path):
    """Read and return the JSON dict stored at `path`."""
    pass


def safe_int(text):
    """Return int(text), or None if it can't be converted."""
    # Hint: try / except ValueError
    pass
