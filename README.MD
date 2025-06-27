# Age of Origins Automation Bot

This project automates gameplay actions in the "Age of Origins" Windows game using Python. It can launch the game, interact with the UI, manage fleets, resources, camps, and factories, and logs every step for easy debugging and auditing.

---

## Features

- **Automatic Game Launch:** Starts the game from a desktop shortcut.
- **Window Management:** Maximizes and focuses the game window.
- **UI Automation:** Uses image recognition (OpenCV) and mouse/keyboard simulation to interact with game elements.
- **Human-like Mouse Movements:** Mouse moves along a random Bézier curve for realism.
- **Resource & Fleet Management:** Automates resource gathering, fleet checks, and camp/factory actions.
- **Logging:** All actions are logged step-by-step in `logs/bot.log` with sequential step numbers.
- **Graceful Exit:** Closes the game window after automation is complete.

---

## Folder Structure

```
scripts/
│
├── actions.py           # Mouse actions and button clicking logic
├── constants.py         # All path and configuration constants
├── first_login.py       # (Reserved for first-time login automation)
├── game_logic.py        # Main automation logic for game actions
├── image_utils.py       # Screenshot and template matching utilities
├── logger.py            # Thread-safe step logger
├── main.py              # Main entry point for the bot
├── switch_account.py    # (Reserved for account switching automation)
├── window_utils.py      # Game window management (launch, maximize, close)
└── __pycache__/         # Python bytecode cache
logs/
└── bot.log              # Automation log file (auto-created)
```

---

## Requirements

- Python 3.8+
- Windows OS
- [OpenCV](https://pypi.org/project/opencv-python/)
- [numpy](https://pypi.org/project/numpy/)
- [pyautogui](https://pypi.org/project/pyautogui/)
- [pygetwindow](https://pypi.org/project/PyGetWindow/)
- [pywin32](https://pypi.org/project/pywin32/)

Install dependencies:
```bash
pip install opencv-python numpy pyautogui PyGetWindow pywin32
```

---

## Usage

1. **Update the Game Shortcut Path:**
   - In `constants.py`, set the correct path to your "Age of Origins" desktop shortcut:
     ```python
     GAME_SHORTCUT = r"C:/Users/<YourUsername>/Desktop/Age of Origins.lnk"
     ```

2. **Run the Bot:**
   ```bash
   python scripts/main.py
   ```

3. **View Logs:**
   - All actions are logged in `logs/bot.log`.

---

## Customization

- **Image Templates:**  
  Place your template images in the `Images/` directory as referenced in the scripts.
- **Timing:**  
  Adjust `time.sleep()` durations in scripts for your system/game speed.
- **Expand Logic:**  
  Add more automation logic in `game_logic.py` or new scripts as needed.

---

## Notes

- The bot uses image recognition; UI changes or resolution changes may require new screenshots/templates.
- All mouse movements are animated and randomized for realism.
- The bot will close the game window automatically after completion.

---

## Disclaimer

This project is for educational purposes only. Use responsibly and in accordance with the game's terms of service.

---