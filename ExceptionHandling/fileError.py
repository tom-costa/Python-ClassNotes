import logging

# logging methods
logging.basicConfig(filename="logFile2.log", level=logging.ERROR)
logging.basicConfig(filename="logFile1.log", level=logging.DEBUG)
logging.critical("Critical")
logging.error("Error")
logging.warning("Warning")
logging.info("Info")
logging.debug("Debug")