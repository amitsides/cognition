import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("agentic_cognition_mas.log"),
        logging.StreamHandler()
    ]
)

def get_logger(name):
    """Get a logger with the specified name."""
    return logging.getLogger(name)