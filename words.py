import random

categories: dict[str, list[str]] = {
    "movies": [
        "inception", "gladiator", "godfather", "interstellar","dune","lalaland","walle","incendies","prisoners", "tumbbad", "zodiac",
        "avengers", "titanic", "whiplash", "parasite", "avatar", "arrival","seven", "memento", "obsession", "hereditary"
    ],
    "food": [
        "spaghetti", "hamburger", "croissant", "guacamole",
        "pancake", "burrito", "dumpling", "chocolate"
    ],
    "space": [
        "supernova", "asteroid", "satellite", "telescope",
        "astronaut", "blackhole", "meteorite", "exoplanet"
    ],
    "cities": [
        "tokyo", "barcelona", "amsterdam", "singapore",
        "vancouver", "marrakech", "istanbul", "kyoto"
    ],
    "superheroes": [
        "spiderman", "wolverine", "ironman", "daredevil",
        "catwoman", "thor", "aquaman", "hawkeye"
    ],
}

# def select_word(category: str) -> str:
def select_word(category: str) -> str:
    category_list = categories[category]
    return random.choice(category_list)

# word = select_word("movies")
# print(word)