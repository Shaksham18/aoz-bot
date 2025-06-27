import sys
import time
import win32api
import win32con
import win32gui
import random
from image_utils import capture_screenshot, template_match
from logger import log_step

def animated_mouse_move(target_x, target_y, duration=1.0, steps=50):
    """
    Moves the mouse smoothly from its current position to (target_x, target_y) over 'duration' seconds,
    following a random quadratic Bézier curve for a more human-like path.
    """
    start_x, start_y = win32api.GetCursorPos()
    # Random control point for the curve (somewhere off the straight line)
    ctrl_x = start_x + (target_x - start_x) * random.uniform(0.3, 0.7) + random.randint(-80, 80)
    ctrl_y = start_y + (target_y - start_y) * random.uniform(0.3, 0.7) + random.randint(-80, 80)

    for i in range(1, steps + 1):
        t = i / steps
        # Quadratic Bézier formula
        x = int((1 - t)**2 * start_x + 2 * (1 - t) * t * ctrl_x + t**2 * target_x)
        y = int((1 - t)**2 * start_y + 2 * (1 - t) * t * ctrl_y + t**2 * target_y)
        win32api.SetCursorPos((x, y))
        time.sleep(duration / steps)

def click_button(region, x, y):
    """
    Simulates a mouse click at the specified screen coordinates, with animated mouse movement.
    """
    try:
        win32gui.SetForegroundWindow(region.hwnd)
    except Exception as e:
        log_step(f"Could not focus window: {e}")
    time.sleep(0.2)
    # Animate mouse move
    move_duration = random.uniform(1.0, 2.0)
    animated_mouse_move(x, y, duration=move_duration)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    log_step(f"Clicked at position: x={x}, y={y} (mouse moved in {move_duration:.2f}s)")
    time.sleep(1)

def find_and_click_button(region, screenshot_path, template_path, x_offset=0, y_offset=0, button_name="Button", max_val_threshold=0.5):
    """
    Finds a button using template matching and clicks it if found.
    """
    log_step(f"Looking for button: {button_name}")
    screen_gray = capture_screenshot(region, screenshot_path)
    max_val, max_loc = template_match(screen_gray, template_path)
    if max_val > max_val_threshold:
        x, y = max_loc
        x += region.left + x_offset
        y += y_offset
        log_step(f"Found {button_name} at ({x}, {y}), clicking...")
        click_button(region, x, y)
        return True, (x, y)
    log_step(f"{button_name} not found. Exiting script.")
    sys.exit(1)