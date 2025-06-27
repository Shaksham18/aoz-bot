"""
Main entry point for the UI automation bot.
"""

import time
from window_utils import activate_game_window, launch_game, close_game_window
from actions import find_and_click_button, click_button
from game_logic import check_fleets, handle_side_menu, log_step
from constants import (
    GAME_SHORTCUT, GAME_WINDOW_TITLE,
    GAME_SCREEN, NAVIGATION_OUT, NAVIGATION_IN
)

def main():
    """
    Main function to orchestrate the automation flow:
    1. Activates the game window.
    2. Finds and clicks the navigation button.
    3. Checks for available fleets (up to 3 times).
    4. Clicks to go inside the base.
    5. Handles the side menu, camps, and factories.
    """
    log_step("=== Bot started === ")
    try:
        # Step 0: Launch the game from desktop shortcut
        launch_game(GAME_SHORTCUT)
        time.sleep(15)  # Wait for the game to start
        log_step("Game launched successfully.")
        region = activate_game_window(GAME_WINDOW_TITLE)
        time.sleep(15)
        # Section 1: Navigation button
        found, (nav_x, nav_y) = find_and_click_button(
            region,
            GAME_SCREEN,
            NAVIGATION_OUT,
            x_offset=20,
            y_offset=50,
            button_name="NavigationOut",
        )

        # Section 2: Fleet button (repeat up to 3 times or until no fleets available)
        fleet_attempts = 0
        while check_fleets(region) and fleet_attempts < 3:
            fleet_attempts += 1
            time.sleep(1)

        time.sleep(2)  # Wait for fleets to be processed
        # Section 3: Go Inside Base
        found, (nav_x, nav_y) = find_and_click_button(
            region,
            GAME_SCREEN,
            NAVIGATION_IN,
            x_offset=20,
            y_offset=50,
            button_name="NavigationIn",
            max_val_threshold=0.4,
        )

        time.sleep(1)

        # Section 4: Side Menu and Camps
        handle_side_menu(region)
    except Exception as e:
        log_step(f"Exception occurred: {e}")
        raise
    finally:
        close_game_window(GAME_WINDOW_TITLE)
        log_step("=== Bot finished ===")

if __name__ == "__main__":
    main()
