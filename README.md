<h1 align="center">☠️ Hangman: Terminal Edition</h1>

<div align="center">

**A polished terminal implementation of the classic Hangman game built with Python and Rich.**

Modern terminal UI • Persistent statistics • Clean MVC architecture

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-MVC-success)
![Rich](https://img.shields.io/badge/UI-Rich-9cf)
![License](https://img.shields.io/badge/License-MIT-yellow)

<br>

<img src="assests/AnimationFinal2.gif" alt="Hangman Terminal Edition Demo" width="850">

</div>

### 📖 Table of Contents

1. [Features](#features)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [License](#license)
7. [Why I Built This](#why-i-built-this)

---

### ✨ Features

- **Live dashboard** — redraws after every guess; gallows panel and status panel side by side
- **Lives that change color** as you get closer to losing — green, orange, then red, so the danger is visible at a glance
- **5 categories** — movies, food, space, cities, superheroes
- **Three difficulty tiers** — Easy (10 lives), Medium (8), Hard (5, hints disabled)
- **Hints** cost one life, and they're turned off entirely on hard mode
- **Gracefully handles invalid input** — type garbage into the prompt and it just tells you what you did wrong
- **Stats that persist between sessions**, even if the file gets deleted or corrupted — it just rebuilds itself
- **Graceful Ctrl+C handling** — no traceback, just a goodbye message and your win/loss record written on the way out

---

### 🏗️ Architecture

`game.py` has no idea `rich` exists, and `ui.py` never changes game state — it only reads it. That split made it a lot easier to test the game logic on its own.

| File | Role | Responsibility |
|---|---|---|
| `main.py` | Controller | CLI args, menu, game loop — wires everything together |
| `game.py` | Model | The `Hangman` class — word, guesses, attempts remaining |
| `ui.py` | View | The `rich` theme, gallows art, panel rendering |
| `stats.py` | Storage | Reads/writes `stats.json`, rebuilds it if missing or broken |
| `words.py` | Data | Category → word-list mapping, random word selection |

---

### 🚀 Installation

Requires **Python 3.10+**.

```bash
git clone https://github.com/husenwalikar/hangman-cli.git
cd hangman-cli
pip install -r requirements.txt
```

The only runtime dependency is `rich`.

---

### 🎮 Usage

#### Option 1: Interactive Menu
```bash
python main.py
```
You'll land on a menu with three commands: `play`, `results`, `exit`.

#### Option 2: CLI Fast-Track
```bash
# Example: Play the 'movies' category on 'hard' difficulty
python main.py --category movies --difficulty hard
```
Categories: `movies`, `food`, `space`, `cities`, `superheroes`
Difficulties: `easy`, `medium`, `hard`
*(Both flags are required together — passing only one gets you a warning.)*

<details>
<summary><b>View all CLI options</b></summary>
<br>

```text
usage: main.py [-h] [-c CATEGORY] [-d {easy,medium,hard}]

Hangman Quick Round

options:
  -h, --help            show this help message and exit
  -c CATEGORY, --category CATEGORY
                        Selecting a category
  -d {easy,medium,hard}, --difficulty {easy,medium,hard}
                        Selecting the difficulty
```

</details>

---

### 🗂️ Project Structure

```text
Hangman/
 ┣ assets/
 ┃ ┗ AnimationFinal2.gif
 ┣ .gitignore
 ┣ CHANGELOG.md
 ┣ LICENSE
 ┣ README.md
 ┣ game.py
 ┣ main.py
 ┣ requirements.txt
 ┣ stats.py
 ┣ ui.py
 ┣ words.py
 ┗ stats.json (generated automatically)
```

See [CHANGELOG.md](CHANGELOG.md) for release history.

> `stats.json` is generated automatically the first time the game runs. Since it stores local statistics, it is already ignored by `.gitignore`.
---

### 📜 License

MIT — see [LICENSE](LICENSE) for details.

---

### 💭 Why I Built This

I kept starting side projects, scoping them way too big, and abandoning them halfway through. So this time I picked something small and dumb on purpose — Hangman — and made myself build it like it actually mattered: a real `Hangman` class instead of a pile of loose variables, a proper MVC split, and a `rich`-powered dashboard, a library I'd never touched before this.

The live dashboard, MVC architecture, and self-healing statistics weren't necessary for a simple Hangman game. I built them anyway because I wanted to practice writing software that was maintainable, not just functional.

---

<p align="center">
  <i>Created by Husen</i><br>
  <a href="https://github.com/husenwalikar">GitHub</a> · <a href="https://www.linkedin.com/in/husensab-walikar-870aab373/">LinkedIn</a>
</p>
