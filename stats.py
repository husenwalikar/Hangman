import json


def save_stats(wins: int, losses: int) -> None:
    with open("stats.json", 'w') as file:
        stats = {"wins": wins, "losses": losses}
        json.dump(stats, file)


def load_stats() -> dict:
    try:
        with open("stats.json", "r") as file:
            stats = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        with open("stats.json", "w") as file:
            stats = {"wins": 0, "losses": 0}
            json.dump(stats, file)

    return stats