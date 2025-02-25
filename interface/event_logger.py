import logging

logging.basicConfig(
    filename="storage/logs/simulation.log", 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(event):
    logging.info(event)
    print(f"[LOG]: {event}")
