"""
Main entry point for the UI automation bot.
"""
import time
from window_utils import activate_game_window, launch_game, close_game_window
from actions import find_and_click_button, click_button
from game_logic import check_fleets, handle_side_menu, log_step
from constants import GAME_SHORTCUT, GAME_WINDOW_TITLE

def main():
    try:
        # Step 0: Launch the game from desktop shortcut
        launch_game(GAME_SHORTCUT)
        time.sleep(15)  # Wait for the game to start
        log_step("Game launched successfully.")
        region = activate_game_window(GAME_WINDOW_TITLE)
    except Exception as e:
        log_step(f"Exception occurred: {e}")
        raise
    finally:
        close_game_window(GAME_WINDOW_TITLE)
        log_step("=== Bot finished ===")

if __name__ == "__main__":
    main()
