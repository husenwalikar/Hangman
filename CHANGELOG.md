# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-08-02
### Added
- Added MIT LICENSE file.
- Added CHANGELOG.md based on Keep a Changelog standard.

### Changed
- Revised README.md for improved clarity, structure, and formatting.

### Fixed
- Fixed typo in the `assets` folder name.
- Corrected image paths and the demo GIF in README.md.
- Resolved remote merge conflicts.

## [1.0.0] - 2026-07-28
### Added
- Complete terminal-based Hangman game logic (`game.py`, `main.py`).
- MVC architecture separating logic, view, and controller.
- Overhauled UI with a `rich`-powered live dashboard (`ui.py`).
- Added `stats.py` to handle local persistent statistics via `stats.json`.
- Added 200 total words across 5 categories in `words.py`.
- Added docstrings to `stats.py` and `game.py`.
- Added support for CLI arguments to fast-track into a game.

### Changed
- Updated `requirements.txt` and `.gitignore`.
- Optimized game logic and kept code DRY with modular functions.

### Fixed
- Fixed CLI inputs and various game loop bugs.
- Fixed persistence bugs to correctly manage the local stats dictionary.

### Removed
- Removed tracked system files (`__pycache__`, `.idea`).
- Removed cached personal stats (`stats.json`) from the repository to prevent uploading local scores.
