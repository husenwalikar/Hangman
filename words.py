import random

categories: dict[str, list[str]] = {
    "movies": [
        "inception", "gladiator", "godfather", "interstellar", "dune", "lalaland", 
        "walle", "incendies", "prisoners", "tumbbad", "zodiac", "avengers", 
        "titanic", "whiplash", "parasite", "avatar", "arrival", "seven", 
        "memento", "obsession", "hereditary", "matrix", "alien", "jaws", 
        "rocky", "fargo", "psycho", "halloween", "vertigo", "shining", 
        "goodfellas", "casino", "scarface", "predator", "terminator", "robocop", 
        "diehard", "platoon", "glory", "unforgiven"
    ],
    "food": [
        "spaghetti", "hamburger", "croissant", "guacamole", "pancake", "burrito", 
        "dumpling", "chocolate", "pizza", "sushi", "popcorn", "ramen", 
        "taco", "nachos", "pretzel", "noodle", "waffle", "gelato", 
        "brownie", "cupcake", "sashimi", "steak", "bacon", "cheese", 
        "sandwich", "hotdog", "bagel", "donut", "cookie", "muffin", 
        "macaron", "lasagna", "ravioli", "curry", "kebab", "shawarma", 
        "falafel", "risotto", "truffle", "caviar"
    ],
    "space": [
        "supernova", "asteroid", "satellite", "telescope", "astronaut", "blackhole", 
        "meteorite", "exoplanet", "nebula", "galaxy", "cosmos", "quasar", 
        "pulsar", "orbit", "eclipse", "gravity", "spaceship", "vacuum", 
        "lunar", "solar", "zenith", "comet", "planet", "starlight", 
        "constellation", "wormhole", "singularity", "eventhorizon", "lightyear", "parallax", 
        "meteor", "plasma", "antimatter", "darkmatter", "celestial", "equinox", 
        "solstice", "asteroidbelt", "supercluster", "void"
    ],
    "cities": [
        "tokyo", "barcelona", "amsterdam", "singapore", "vancouver", "marrakech", 
        "istanbul", "kyoto", "seoul", "london", "berlin", "dubai", 
        "moscow", "chicago", "seattle", "osaka", "mumbai", "venice", 
        "prague", "cairo", "havana", "paris", "rome", "madrid", 
        "athens", "lisbon", "vienna", "budapest", "warsaw", "kiev", 
        "dublin", "oslo", "stockholm", "helsinki", "copenhagen", "sydney", 
        "melbourne", "auckland", "toronto", "montreal"
    ],
    "superheroes": [
        "spiderman", "wolverine", "ironman", "daredevil", "catwoman", "thor", 
        "aquaman", "hawkeye", "batman", "superman", "deadpool", "punisher", 
        "spawn", "hellboy", "rorschach", "nightwing", "cyclops", "flash", 
        "cyborg", "magneto", "venom", "hulk", "captainamerica", "blackwidow", 
        "doctorstrange", "antman", "blackpanther", "starlord", "groot", "rocket", 
        "gamora", "drax", "vision", "scarletwitch", "quicksilver", "falcon", 
        "wintersoldier", "warmachine", "shazam", "greenlantern"
    ],
}


def select_word(category: str) -> str:
    category_list = categories[category]
    return random.choice(category_list)