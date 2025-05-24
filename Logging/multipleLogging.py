import logging

# logger for module1

logger1 = logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

logger2 = logging.getLogger("module2")
logger2.setLevel(logging.WARNING)
logger3 = logging.getLogger("module3")
logger3.setLevel(logging.INFO)

logging.basicConfig(
    # filename='file.log', #Will create a ile to save logs
    # filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s -%(name)s- %(levelname)s-%(message)s', #Format of how debug msg should be seen/written
    datefmt='%d-%m-%Y %H:%M:%S'
)


# Log msgs with different logger
logger3.info("Debug msg for module3")
logger1.debug("Debug msg for module1")
logger2.warning("Debug msg for module2")
logger3.error("Debug msg for module3")

