import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Debug message")
logging.info("Application started")
logging.warning("Low disk space")
logging.error("Database connection failed")
logging.critical("System crashed")