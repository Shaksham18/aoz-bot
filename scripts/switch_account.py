"""
Main entry point for the UI automation bot.
"""
import time
from window_utils import activate_game_window, launch_game, close_game_window
from actions import find_and_click_button, click_button
from game_logic import check_fleets, handle_side_menu, log_step

def main():
    try:
        # Step 0: Launch the game from desktop shortcut
        launch_game(r"C:/Users/shaks/Desktop/Age of Origins.lnk")  # <-- Update path as needed
        time.sleep(15)  # Wait for the game to start
        log_step("Game launched successfully.")
        region = activate_game_window("Age of Origins")
    except Exception as e:
        log_step(f"Exception occurred: {e}")
        raise
    finally:
        close_game_window("Age of Origins")
        log_step("=== Bot finished ===")

if __name__ == "__main__":
    main()
