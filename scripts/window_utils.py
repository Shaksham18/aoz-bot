from dataclasses import dataclass
import os
import time
import pygetwindow as gw
import win32gui
import win32con
from logger import log_step

@dataclass
class WindowRegion:
    """
    Stores information about a window's region on the screen.
    """
    hwnd: int
    left: int
    top: int
    width: int
    height: int

def activate_game_window(window_title):
    """
    Finds and activates the game window by its title.
    Returns a WindowRegion object.
    """
    log_step(f"Activating game window: {window_title}")
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        log_step(f"Window with title '{window_title}' not found.")
        raise RuntimeError(f"Window with title '{window_title}' not found.")
    game_window = windows[0]
    hwnd = win32gui.FindWindow(None, game_window.title)
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)  # Maximize the window
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.5)
    log_step(f"Game window activated and maximized: {window_title}")
    return WindowRegion(
        hwnd=hwnd,
        left=game_window.left,
        top=game_window.top,
        width=game_window.width,
        height=game_window.height,
    )

def launch_game(shortcut_path):
    """
    Launches the game using the provided shortcut or executable path.
    """
    log_step(f"Launching game from: {shortcut_path}")
    if not os.path.exists(shortcut_path):
        log_step(f"Game shortcut not found: {shortcut_path}")
        raise FileNotFoundError(f"Game shortcut not found: {shortcut_path}")
    os.startfile(shortcut_path)
    time.sleep(5)  # Wait for the game to start (adjust as needed)
    log_step("Game launch command issued.")

def close_game_window(window_title):
    """
    Closes the game window by sending WM_CLOSE.
    """
    log_step(f"Closing game window: {window_title}")
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
        time.sleep(2)
        log_step("Game window closed.")
    else:
        log_step(f"Game window '{window_title}' not found for closing.")