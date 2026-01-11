import logging
import os


def get_logger(name):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        os.makedirs("logs", exist_ok=True)

        formatter = logging.Formatter('%(asctime)s -%(name)s - %(message)s')

        file_handler = logging.FileHandler("logs/framework.log", mode="w")
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger