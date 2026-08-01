# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - Initial Release

### Added
- Complete terminal-based Hangman game.
- MVC architecture separating logic (`game.py`), view (`ui.py`), and controller (`main.py`).
- Rich-powered live dashboard with dynamic color changes based on remaining lives.
- 5 categorized word banks: movies, food, space, cities, superheroes.
- Three difficulty tiers (Easy, Medium, Hard).
- Local persistent statistics stored in `stats.json`.
- Support for CLI arguments to bypass the menu and fast-track directly into a game.
