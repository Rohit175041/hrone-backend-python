import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),  # Console
        logging.FileHandler("logs/hrone.log", mode="a", encoding="utf-8")  # File
    ]
)

logger = logging.getLogger("hrone-backend")
