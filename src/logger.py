import logging

logger = logging.getLogger()
handler = logging.FileHandler("logfile.txt")
logger.addHandler(handler)
