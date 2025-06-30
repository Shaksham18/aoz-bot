import os
import time
import threading

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

_STEP_COUNTER = {"value": 1}
_STEP_LOCK = threading.Lock()

def get_next_step():
    with _STEP_LOCK:
        step = _STEP_COUNTER["value"]
        _STEP_COUNTER["value"] += 1
    return step

def log_step(message):
    """
    Appends a message to the daily log file with a timestamp and sequential step number.
    Log file is named as bot_YYYYMMDD.log.
    """
    step = get_next_step()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_filename = f"bot_{time.strftime('%Y%m%d')}.log"
    log_file = os.path.join(LOG_DIR, log_filename)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [Step {step}] {message}\n")