from setuptools import setup, find_packages
import os

# Ensure the 'sc' folder exists for screenshots
sc_dir = os.path.join(os.path.dirname(__file__), "sc")
os.makedirs(sc_dir, exist_ok=True)

setup(
    name="age_of_origins_bot",
    version="1.0.0",
    description="Automation bot for Age of Origins game",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy",
        "pyautogui",
        "PyGetWindow",
        "pywin32"
    ],
    python_requires=">=3.8",
)