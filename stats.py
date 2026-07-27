import json


def save_stats(wins: int, losses: int) -> None:
    """
    Persists the current win/loss record to a local JSON file.

    Args:
        wins: Total number of rounds won.
        losses: Total number of rounds lost.
    """
    with open("stats.json", 'w') as file:
        stats = {"wins": wins, "losses": losses}
        json.dump(stats, file)


def load_stats() -> dict:
    """
    Loads the win/loss record from the local JSON file.
    Creates a fresh file with zeroed stats if missing or corrupted.

    Returns:
        A dictionary containing 'wins' and 'losses' integers.
    """
    try:
        with open("stats.json", "r") as file:
            stats = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        with open("stats.json", "w") as file:
            stats = {"wins": 0, "losses": 0}
            json.dump(stats, file)

    return stats