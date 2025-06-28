import os

# Base directories
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
IMAGES_DIR = os.path.join(BASE_DIR, "Images")
SC_DIR = os.path.join(BASE_DIR, "sc")

# Log file
LOG_FILE = os.path.join(LOG_DIR, "bot.log")

# Game shortcut and window title
GAME_SHORTCUT = r"C:/Users/shaks/Desktop/Age of Origins.lnk"  # Update as needed
GAME_WINDOW_TITLE = "Age of Origins"

# Template image paths
NAVIGATION_OUT = os.path.join(IMAGES_DIR, "navigation", "out.png")
NAVIGATION_IN = os.path.join(IMAGES_DIR, "navigation", "in.png")
NAVIGATION_EXPAND_FLEET = os.path.join(IMAGES_DIR, "navigation", "expand_fleet.png")
NAVIGATION_SEARCH_RESOURCE = os.path.join(IMAGES_DIR, "navigation", "search_resource.png")
NAVIGATION_SIDE_MENU = os.path.join(IMAGES_DIR, "navigation", "side_menu.png")
CAMP1 = os.path.join(IMAGES_DIR, "navigation", "camp1.png")
CAMP2 = os.path.join(IMAGES_DIR, "navigation", "camp2.png")
FACTORY1 = os.path.join(IMAGES_DIR, "navigation", "factory1.png")
FACTORY2 = os.path.join(IMAGES_DIR, "navigation", "factory2.png")
TRAIN_BASIC_ROCKET_LAUNCHER = os.path.join(IMAGES_DIR, "train", "BasicRocketLauncher.png")
TRAIN_RECRUIT_BUTTON = os.path.join(IMAGES_DIR, "train", "recruitButton.png")
TRAIN_BASIC_SHREDDER = os.path.join(IMAGES_DIR, "train", "BasicShredder.png")
RESOURCE_STEEL = os.path.join(IMAGES_DIR, "resource", "steel", "steel.png")
RESOURCE_INCREASE = os.path.join(IMAGES_DIR, "resource", "increase.png")
RESOURCE_GO = os.path.join(IMAGES_DIR, "resource", "go.png")
RESOURCE_GATHER = os.path.join(IMAGES_DIR, "resource", "gather.png")
RESOURCE_DECREASE = os.path.join(IMAGES_DIR, "resource", "decrease.png")
RESOURCE_SETOUT = os.path.join(IMAGES_DIR, "resource", "setout.png")
CLAIM_REWARD = os.path.join(IMAGES_DIR, "firstLogin", "claim_reward.png")
LOGIN_REWARD = os.path.join(IMAGES_DIR, "firstLogin", "login_reward.png")
OUT_OF_SHADE = os.path.join(IMAGES_DIR, "firstLogin","out_of_shade.png")

# Screenshot paths
GAME_SCREEN = os.path.join(SC_DIR, "game_screen.png")
TRAINING_SCREEN = os.path.join(SC_DIR, "training_screen.png")
FACTORY_SCREEN = os.path.join(SC_DIR, "factory_screen.png")
RESOURCE_SCREEN = os.path.join(SC_DIR, "resource_screen.png")
GATHER_SCREEN = os.path.join(SC_DIR, "gather_screen.png")
SETOUT_SCREEN = os.path.join(SC_DIR, "setout_screen.png")
SIDE_MENU_SCREEN = os.path.join(SC_DIR, "side_menu_screen.png")