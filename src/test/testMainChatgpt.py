import os
import time
import json
import logging.config
import pyautogui
import pydirectinput

# Constants
BASE_PATH = os.path.abspath("..")
FAILSAFE = False
MIN_SEARCH_TIME = 5
CONFIDENCE_LEVEL = 0.8

# Initialize pyautogui
pyautogui.FAILSAFE = FAILSAFE


def resource_path(relative_path):
    """Return the absolute path of the resource, useful for accessing resources post-packaging."""
    return os.path.join(BASE_PATH, relative_path)


def setup_logging():
    """Set up logging configuration from a specified path."""
    default_path = resource_path('../logging_configs/config.json')
    if os.path.exists(default_path):
        with open(default_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.DEBUG)
        logging.warning("Failed to load configuration file. Using default configs")


def locate_image(image_path):
    """Locate the center of an image on the screen with predefined settings."""
    try:
        return pyautogui.locateCenterOnScreen(image_path, minSearchTime=MIN_SEARCH_TIME, confidence=CONFIDENCE_LEVEL)
    except pyautogui.ImageNotFoundException:
        return None


def loop_until_found(image_path, max_attempts=100):
    """Loop until an image is found or the attempt limit is reached."""
    for attempt in range(max_attempts):
        if locate_image(image_path):
            logging.info(f"Image found: {image_path}")
            return True
        logging.debug(f"Attempt {attempt + 1}: Image not found, retrying...")
        time.sleep(5)
    logging.info("Reached maximum retry attempts without finding the image.")
    return False


def click_image(image_path):
    """Locate an image and perform a click at its position."""
    location = locate_image(image_path)
    if location:
        pydirectinput.click(location.x, location.y)
        return True
    return False


def main():
    setup_logging()
    logger = logging.getLogger("root")
    logger.info("Script starting...")

    # Initialize script
    time.sleep(3)
    logger.info("Initialization complete.")

    # Main operational loop
    count = 0
    while True:
        count += 1
        logger.debug(f"Round {count} begins.")

        # Auto-click start button
        if not click_image(resource_path('../images/start1.png')):
            logger.debug("Start1 image not found, checking for Start2.")
            click_image(resource_path('../images/start2.png'))

        # Auto-click to enter the link, considering the player may not be ready
        loop_until_found(resource_path('../images/enter.png'), max_attempts=120)
        pydirectinput.moveTo(970, 920)
        pydirectinput.click()

        # Automatically identify the select role screen and handle unprepared player situations
        loop_until_found(resource_path('../images/ao.png'), max_attempts=50)
        location = locate_image(resource_path('../images/ao.png'))
        if location:
            pydirectinput.moveTo(location.x, location.y)
            logger.debug(f"Audrey selected at x={location.x}, y={location.y}")
        else:
            # Default click position if image not found
            pydirectinput.moveTo(575, 996)
        pydirectinput.click()

        # Auto-lock in the selected character
        loop_until_found(resource_path('../images/lock1.png'), max_attempts=50)
        pydirectinput.moveTo(918, 779)
        pydirectinput.click()

        # Waiting for the match to end
        logger.debug("Match in progress, sleeping for 210 seconds...")
        time.sleep(210)
        logger.debug("Match ended.")

        # Image recognition for score and game events
        loop_until_found(resource_path('../images/r-45.png'), max_attempts=50)
        # Simulate movement to wait for game end
        pydirectinput.press('w')
        time.sleep(10)
        pydirectinput.press('d')
        time.sleep(10)

        # Handle game ending
        loop_until_found(resource_path('../images/next.png'), max_attempts=50)
        pydirectinput.moveTo(1628, 949)
        pydirectinput.click()

        # Logging and looping
        logger.debug("End of round operations completed, preparing for next round.")
        logger.debug("==================================================")

if __name__ == "__main__":
    main()

