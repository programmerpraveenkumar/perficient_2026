import logging

# Basic logging to console
# logging.warning("This is a warning message.")

# Configuring a logger to write to a file
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("This message will go to the file.")