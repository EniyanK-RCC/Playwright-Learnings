import logging
# Creating custom logger
logger = logging.getLogger("GooglePageLogger")
logger.setLevel(logging.INFO)

# Creating handlers
file_handler = logging.FileHandler("GooglePage.log")
console_handler = logging.StreamHandler()

# Setting the logging level for each handler
file_handler.setLevel(logging.INFO)
console_handler.setLevel(logging.INFO)

# Creating logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adding handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Preventing logging from propagating to the root logger
logger.propagate = False