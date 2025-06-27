import os
import time
import threading

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "bot.log")

_STEP_COUNTER = {"value": 1}
_STEP_LOCK = threading.Lock()

def get_next_step():
    with _STEP_LOCK:
        step = _STEP_COUNTER["value"]
        _STEP_COUNTER["value"] += 1
    return step

def log_step(message):
    """
    Appends a message to the log file with a timestamp and sequential step number.
    """
    step = get_next_step()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [Step {step}] {message}\n")