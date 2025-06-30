"""
Main entry point for the UI automation bot.
"""
import time
from window_utils import activate_game_window, launch_game, close_game_window
from game_logic import check_login_rewards, log_step
from constants import GAME_SHORTCUT, GAME_WINDOW_TITLE

def main():
    try:
        # Step 0: Launch the game from desktop shortcut
        launch_game(GAME_SHORTCUT)
        time.sleep(15)  # Wait for the game to start
        log_step("Game launched successfully.")
        region = activate_game_window(GAME_WINDOW_TITLE)
        time.sleep(30)

        # Section 1: Check for login rewards
        log_step("Checking for login rewards...")
        check_login_rewards(region)

    except Exception as e:
        log_step(f"Exception occurred: {e}")
        raise
    finally:
        close_game_window(GAME_WINDOW_TITLE)
        log_step("=== Bot finished ===")

if __name__ == "__main__":
    main()
