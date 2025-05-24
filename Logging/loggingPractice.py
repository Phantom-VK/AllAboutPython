import logging

# Configure logging
logging.basicConfig(
    filename='file.log', #Will create a ile to save logs
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s -%(name)s- %(levelname)s-%(message)s', #Format of how debug msg should be seen/written
    datefmt='%d-%m-%Y %H:%M:%S'
)
# Levels
logging.debug("This is a debug msg")
logging.info("This is a info msg")
logging.warning("This is a warning msg")
logging.error("This is an error msg")
logging.critical("This is a critical msg")


logging.debug("This is a debug msg")
logging.info("This is a info msg")
logging.warning("This is a warning msg")
logging.error("This is an error msg")
logging.critical("This is a critical msg")


