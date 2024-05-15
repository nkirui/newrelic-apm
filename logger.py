import logging
import sys


# licence
# 100363be0cff714189be2b348de5761cFFFFNRAL

# userkey
# NRAK-GE57YJ01CSW9W6ZFRN86CD2KWNK

logger = logging.getLogger()

formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

stream_handler = logging.StreamHandler(sys.stdout)

# # not necessary
# file_handler = logging.FileHandler("app.log")

stream_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

logger.handlers = [stream_handler]

logger.setLevel(logging.INFO)