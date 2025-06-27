import cv2
import numpy as np
import pyautogui
import time
import os
from logger import log_step

def capture_screenshot(region, save_path):
    """
    Captures a screenshot of the specified window region and saves it.
    Returns a grayscale image.
    """
    log_step(f"Capturing screenshot to {save_path}")
    time.sleep(0.5)
    screenshot = pyautogui.screenshot(
        region=(region.left, region.top, region.width, region.height)
    )
    screenshot.save(save_path)
    screen_np = np.array(screenshot)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
    log_step(f"Screenshot saved and converted to grayscale: {save_path}")
    return screen_gray

def template_match(screen_gray, template_path):
    """
    Performs template matching to find a UI element in the screenshot.
    Returns (max_val, max_loc).
    """
    log_step(f"Performing template match with: {template_path}")
    if not os.path.exists(template_path):
        log_step(f"Template image not found: {template_path}")
        raise FileNotFoundError(f"Template image not found: {template_path}")
    template = cv2.imread(template_path, 0)
    if template is None:
        log_step(f"Failed to load template image: {template_path}")
        raise ValueError(f"Failed to load template image: {template_path}")
    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    log_step(f"Template match result: max_val={max_val}, max_loc={max_loc}")
    return max_val, max_loc