import logging

"""Logging"""
logger = logging.getLogger("XLS_LOGGER")
logger.setLevel(logging.logThreads)
filehandler = logging.FileHandler("logs.csv")
filehandler.setLevel(logging.INFO)
logging_format = logging.Formatter("%(asctime)s,%(name)s,%(levelname)s,%(message)s")
filehandler.setFormatter(logging_format)
logger.addHandler(filehandler)
