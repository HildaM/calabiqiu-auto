import logging
import logging.config
import json
import os

def setup_logging(default_path='D:\\GitHub\\calabiqiu-auto\\src\\logging_configs\\config.json'):
    """Setup logging configuration"""
    if os.path.exists(default_path):
        with open(default_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.DEBUG)
        print("Failed to load configuration file. Using default configs")

def main():
    setup_logging()  # Setup logging with configuration file
    logger = logging.getLogger("root")  # Get the configured logger
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")

if __name__ == "__main__":
    main()
