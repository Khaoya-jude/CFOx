from app.mcp.server import start_mcp_server, get_mcp_client
from app.orchestration.scheduler import start_scheduler

import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cfox-main")

def main():
    logger.info("Starting CFOx application...")

    start_mcp_server()
    logger.info("MCP server started.")

    scheduler = start_scheduler()
    logger.info("Scheduler started.")

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        logger.info("Shutting down CFOx application...")

if __name__ == "__main__":
    main()