from setuptools import setup, find_packages

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