# Age of Origins Automation Bot

## Overview

This project is a professional automation bot designed for the game **Age of Origins**. It automates repetitive in-game actions such as resource gathering, fleet management, training, and login rewards collection using advanced computer vision and UI automation techniques.

The bot leverages Python, OpenCV, PyAutoGUI, and Windows API libraries to interact with the game window, recognize UI elements, and perform human-like mouse movements and clicks.

---

## Features

- **Automated Game Launch & Window Management:**  
  Automatically launches the game, maximizes, and focuses the game window for reliable automation.

- **Template-Based UI Recognition:**  
  Uses OpenCV template matching to detect buttons and UI elements on the screen.

- **Human-like Mouse Movements:**  
  Mouse actions are animated along random Bézier curves for natural, undetectable interaction.

- **Resource Gathering Automation:**  
  Automatically searches for resources, increases gather amount, and sends fleets.

- **Camp & Factory Management:**  
  Automates training and recruiting in camps and production in factories.

- **Login Reward Collection:**  
  Detects and claims daily login rewards and handles popups.

- **Robust Logging:**  
  All actions are logged per day with step numbers and timestamps for easy debugging and auditing.

- **Exception Handling:**  
  All major functions include exception handling and detailed logging for reliability.

---

## Project Structure

```
scripts/
│
├── actions.py         # Mouse movement and click logic
├── constants.py       # Paths and constants for templates and screenshots
├── first_login.py     # Script for first login and reward collection
├── game_logic.py      # Core automation logic and workflow
├── image_utils.py     # Screenshot capture and template matching
├── logger.py          # Step-based daily logging
├── main.py            # Main entry point for the bot
├── window_utils.py    # Window activation and management
├── requirement.txt    # Python dependencies
├── setup.py           # Packaging setup
├── __init__.py
└── __pycache__/
```

---

## Getting Started

### Prerequisites

- **Run your IDE (e.g., VS Code) in Administrator mode**  
  (Required for window control and automation APIs)
- **Install and log in to Age of Origins**  
  (Game must be installed and accessible via desktop shortcut)
- **Supported base levels:** 15–19
- Windows OS
- Python 3.8+

### Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd Bot/scripts
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirement.txt
   ```

3. **Configure constants:**
   - Update `GAME_SHORTCUT` and `GAME_WINDOW_TITLE` in `constants.py` if needed.
   - Place template images in the correct folders under `Images/`.

### Running the Bot

- **Main automation:**
  ```sh
  python main.py
  ```

- **First login and reward collection:**
  ```sh
  python first_login.py
  ```

---

## Customization

- **Templates:**  
  Add or update template images in the `Images/` directory for different UI elements.

- **Logging:**  
  Logs are saved daily in the `logs/` directory with step numbers and timestamps.

- **Screen Regions:**  
  The bot dynamically detects window positions and sizes for multi-monitor setups.

---

## Disclaimer

This project is for educational and personal use only.  
Automating games may violate their terms of service. Use at your own risk.

---

## Author

- Shaksham Saxena  
- Shaksham18@gmail.com

---

## Acknowledgements

This project was developed with the assistance of [GitHub Copilot](https://github.com/features/copilot), an AI pair programmer that helped accelerate code writing, improve code quality, and provide professional suggestions throughout the development process.