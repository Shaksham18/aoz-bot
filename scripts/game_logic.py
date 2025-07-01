import sys
import time
from typing import Tuple
import numpy as np

from image_utils import capture_screenshot, template_match
from actions import click_button
from logger import log_step
from constants import (
    CLAIM_REWARD, CLOSE, GAME_SCREEN, GATHER_SCREEN, LOGIN_REWARD, NAVIGATION_EXPAND_FLEET, NAVIGATION_SEARCH_RESOURCE, POPUP_SCREEN, RESOURCE_STEEL,
    RESOURCE_SCREEN, RESOURCE_INCREASE, RESOURCE_GO, RESOURCE_GATHER, RESOURCE_DECREASE, RESOURCE_SETOUT, SETOUT_SCREEN,
    TRAIN_BASIC_ROCKET_LAUNCHER, TRAIN_RECRUIT_BUTTON, CAMP1, CAMP2, FACTORY1, FACTORY2,
    TRAINING_SCREEN, FACTORY_SCREEN, SIDE_MENU_SCREEN, NAVIGATION_SIDE_MENU
)
from window_utils import WindowRegion

def click_and_log(
    region: WindowRegion,
    template_img: str,
    screen_gray: np.ndarray,
    x_offset: int = 20,
    y_offset: int = 20,
    desc: str = ""
) -> bool:
    """
    Matches a template in the given screenshot, logs the action, and clicks if found.

    Args:
        region (WindowRegion): The region of the window to operate in.
        template_img (str): Path to the template image.
        screen_gray (np.ndarray): Grayscale screenshot to search in.
        x_offset (int, optional): X offset for click position. Defaults to 20.
        y_offset (int, optional): Y offset for click position. Defaults to 20.
        desc (str, optional): Description for logging. Defaults to "".

    Returns:
        bool: True if click was performed, False otherwise.
    """
    try:
        max_val, max_loc = template_match(screen_gray, template_img)
        if max_val > 0.5:
            x, y = max_loc
            x += region.left + x_offset
            y += region.top + y_offset
            log_step(f"Adjusted Click Position for {desc}: x={x}, y={y}")
            click_button(region, x, y)
            return True
        else:
            log_step(f"{desc} button not found. Skipping.")
            return False
    except Exception as e:
        log_step(f"Exception in click_and_log: {e}")
        return False

def check_fleets(region: WindowRegion) -> bool:
    """
    Checks if fleets are available by looking for the fleet expansion button.

    Args:
        region (WindowRegion): The region of the window to operate in.

    Returns:
        bool: True if fleets are available, False otherwise.
    """
    try:
        log_step("Checking fleets availability...")
        fleet_screen_gray = capture_screenshot(region, GAME_SCREEN)
        fleet_max_val, _ = template_match(fleet_screen_gray, NAVIGATION_EXPAND_FLEET)
        if fleet_max_val < 0.5:
            log_step("Fleets available.")
            if handle_search_resource(region, fleet_screen_gray):
                return True
            else:
                log_step("Search Resource button not found. Exiting script.")
                return True
        else:
            log_step("No fleets available.")
            return False
    except Exception as e:
        log_step(f"Exception in check_fleets: {e}")
        return False

def handle_search_resource(region: WindowRegion, fleet_screen_gray: np.ndarray) -> bool:
    """
    Clicks the search resource button and then the steel resource.

    Args:
        region (WindowRegion): The region of the window to operate in.
        fleet_screen_gray (np.ndarray): Grayscale screenshot of the fleet screen.

    Returns:
        bool: True if resource search was handled, False otherwise.
    """
    try:
        search_resource_max_val, search_resource_max_loc = template_match(
            fleet_screen_gray, NAVIGATION_SEARCH_RESOURCE
        )
        if search_resource_max_val > 0.45:
            search_x, search_y = search_resource_max_loc
            search_x += region.left + 40
            search_y += region.top + 40
            log_step(f"Adjusted Click Position for Search Resource: x={search_x}, y={search_y}")
            click_button(region, search_x, search_y)
            time.sleep(1)
            handle_resource(region, RESOURCE_STEEL, "Steel")
            return True
        return False
    except Exception as e:
        log_step(f"Exception in handle_search_resource: {e}")
        return False

def handle_resource(region: WindowRegion, resource_template: str, resource_name: str) -> None:
    """
    Clicks on a resource in the side menu and performs actions.

    Args:
        region (WindowRegion): The region of the window to operate in.
        resource_template (str): Path to the resource template image.
        resource_name (str): Name of the resource for logging.
    """
    try:
        log_step("Capturing resource screen and matching resource template...")
        resource_screen_gray = capture_screenshot(region, RESOURCE_SCREEN)
        resource_max_val, resource_max_loc = template_match(resource_screen_gray, resource_template)
        log_step(f"Resource Max Value: {resource_max_val}, Location: {resource_max_loc}")
        if resource_max_val <= 0.5:
            log_step(f"{resource_name} not found. Skipping.")
            return

        resource_x, resource_y = resource_max_loc
        resource_x += region.left + 70
        resource_y += region.top + 80
        log_step(f"Adjusted Click Position for {resource_name}: x={resource_x}, y={resource_y}")
        click_button(region, resource_x, resource_y)
        time.sleep(1)

        log_step("Trying to increase resource amount...")
        if not click_and_log(region, RESOURCE_INCREASE, resource_screen_gray, desc="Increase"):
            return

        for i in range(5):
            log_step(f"Increasing resource amount (attempt {i+1})...")
            click_and_log(region, RESOURCE_INCREASE, resource_screen_gray, desc="Increase")

        time.sleep(1)

        log_step("Trying to click Go button...")
        if not click_and_log(region, RESOURCE_GO, resource_screen_gray, desc="Go Button"):
            return
        time.sleep(1)

        for gather_attempt in range(4, 0, -1):
            log_step(f"Gathering resources (attempt {5-gather_attempt})...")
            gather_screen_gray = capture_screenshot(region, GATHER_SCREEN)
            if click_and_log(region, RESOURCE_GATHER, gather_screen_gray, desc="Gather"):
                click_and_log(region, RESOURCE_GATHER, gather_screen_gray, desc="Gather")
                time.sleep(1)
                setout_screen_gray = capture_screenshot(region, SETOUT_SCREEN)
                if click_and_log(region, RESOURCE_SETOUT, setout_screen_gray, desc="Set Out"):
                    log_step("Set Out completed.")
                    return
                else:
                    log_step("Set Out button not found. Skipping.")
            else:
                log_step("Gather not found, trying to decrease resource amount...")
                if click_and_log(region, RESOURCE_DECREASE, gather_screen_gray, desc="Decrease"):
                    time.sleep(1)
                    if not click_and_log(region, RESOURCE_GO, resource_screen_gray, desc="Go Button"):
                        return
                    time.sleep(1)
                else:
                    log_step("Decrease button not found. Skipping.")
                    return
    except Exception as e:
        log_step(f"Exception in handle_resource: {e}")

def handle_camp(
    region: WindowRegion,
    side_menu_screen_gray: np.ndarray,
    camp_template: str,
    camp_name: str
) -> None:
    """
    Clicks on a camp in the side menu and performs training or recruiting.

    Args:
        region (WindowRegion): The region of the window to operate in.
        side_menu_screen_gray (np.ndarray): Grayscale screenshot of the side menu.
        camp_template (str): Path to the camp template image.
        camp_name (str): Name of the camp for logging.
    """
    try:
        log_step(f"Handling camp: {camp_name}")
        camp_max_val, camp_max_loc = template_match(side_menu_screen_gray, camp_template)
        if camp_max_val > 0.5:
            camp_x, camp_y = camp_max_loc
            camp_x += region.left + 70
            camp_y += region.top + 80
            log_step(f"Adjusted Click Position for {camp_name}: x={camp_x}, y={camp_y}")
            click_button(region, camp_x, camp_y)
            handle_training_or_recruit(region)
        else:
            log_step(f"{camp_name} not found. Skipping.")
    except Exception as e:
        log_step(f"Exception in handle_camp: {e}")

def handle_training_or_recruit(region: WindowRegion) -> None:
    """
    Handles training or recruiting after entering a camp/factory.

    Args:
        region (WindowRegion): The region of the window to operate in.
    """
    try:
        training_screen_gray = capture_screenshot(region, TRAINING_SCREEN)
        training_max_val, training_max_loc = template_match(training_screen_gray, TRAIN_BASIC_ROCKET_LAUNCHER)
        if training_max_val > 0.5:
            training_x, training_y = training_max_loc
            training_x += region.left + 480
            training_y += 20
            log_step(f"Adjusted Click Position for Training: x={training_x}, y={training_y}")
            click_button(region, training_x, training_y)
        else:
            recruit_max_val, recruit_max_loc = template_match(training_screen_gray, TRAIN_RECRUIT_BUTTON)
            if recruit_max_val > 0.5:
                recruit_x, recruit_y = recruit_max_loc
                recruit_x += region.left + 20
                recruit_y += 20
                log_step(f"Adjusted Click Position for Recruit: x={recruit_x}, y={recruit_y}")
                click_button(region, recruit_x, recruit_y)
                click_button(region, recruit_x - 1800, recruit_y - 920)
    except Exception as e:
        log_step(f"Exception in handle_training_or_recruit: {e}")

def handle_factory(
    region: WindowRegion,
    side_menu_screen_gray: np.ndarray,
    factory_template: str,
    factory_name: str
) -> None:
    """
    Clicks on a factory in the side menu and performs production.

    Args:
        region (WindowRegion): The region of the window to operate in.
        side_menu_screen_gray (np.ndarray): Grayscale screenshot of the side menu.
        factory_template (str): Path to the factory template image.
        factory_name (str): Name of the factory for logging.
    """
    try:
        log_step(f"Handling factory: {factory_name}")
        factory_max_val, factory_max_loc = template_match(side_menu_screen_gray, factory_template)
        if factory_max_val > 0.5:
            factory_x, factory_y = factory_max_loc
            factory_x += region.left + 70
            factory_y += region.top + 80
            log_step(f"Adjusted Click Position for {factory_name}: x={factory_x}, y={factory_y}")
            click_button(region, factory_x, factory_y)
            time.sleep(1)
            handle_training_or_recruit(region)
        else:
            log_step(f"{factory_name} not found. Skipping.")
    except Exception as e:
        log_step(f"Exception in handle_factory: {e}")

def handle_side_menu(region: WindowRegion) -> None:
    """
    Opens the side menu and interacts with camps and factories.

    Args:
        region (WindowRegion): The region of the window to operate in.
    """
    try:
        log_step("Handling side menu...")
        base_screen_gray = capture_screenshot(region, GAME_SCREEN)
        side_menu_max_val, side_menu_max_loc = template_match(base_screen_gray, NAVIGATION_SIDE_MENU)
        if side_menu_max_val > 0.5:
            side_menu_x, side_menu_y = side_menu_max_loc
            side_menu_x += region.left + 20
            side_menu_y += 30
            log_step(f"Adjusted Click Position for Side Menu: x={side_menu_x}, y={side_menu_y}")
            click_button(region, side_menu_x, side_menu_y)
            time.sleep(1)
            side_menu_screen_gray = capture_screenshot(region, SIDE_MENU_SCREEN)
            for camp, name in [
                (CAMP1, "Camp 1"),
                (CAMP2, "Camp 2"),
                (FACTORY1, "Factory 1"),
                (FACTORY2, "Factory 2"),
            ]:
                handle_camp(region, side_menu_screen_gray, camp, name)
        else:
            log_step("Side Menu Button not found. Exiting script.")
            sys.exit(1)
    except Exception as e:
        log_step(f"Exception in handle_side_menu: {e}")

def check_login_rewards(region: WindowRegion) -> None:
    """
    Checks for login rewards and clicks to claim them if available.

    Args:
        region (WindowRegion): The region of the window to operate in.
    """
    try:
        log_step("Checking for login rewards...")
        login_screen_gray = capture_screenshot(region, GAME_SCREEN)
        login_max_val, login_max_loc = template_match(login_screen_gray, LOGIN_REWARD)
        if login_max_val > 0.5:
            login_x, login_y = login_max_loc
            login_x += region.left - 20
            login_y += region.top - 100
            click_and_log(region, CLAIM_REWARD, login_screen_gray, desc="Claim Reward")
            time.sleep(2)
            click_button(region, login_x, login_y)
            log_step("Login reward claimed.")
            time.sleep(2)
        for _ in range(5):
            popup_screen_gray = capture_screenshot(region, POPUP_SCREEN)
            click_and_log(region, CLOSE, popup_screen_gray, desc="Close Popups")
            time.sleep(2)
        else:
            log_step("No login rewards found.")
    except Exception as e:
        log_step(f"Exception in check_login_rewards: {e}")

