import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='python_logs.log')
logging.info("I am info!")
logging.debug("I am debug!")
logging.error("I am error!")
logging.critical("I am terrible CRITICAL!!")