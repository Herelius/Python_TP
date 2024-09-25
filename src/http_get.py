import logging
import requests
from requests import HTTPError

logger = logging.getLogger(__name__)


def http_get(url: str) -> dict:
    try:
        response = requests.get(url)
        print(response.elapsed.total_seconds())
        response.raise_for_status()
    
    except HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")

    except Exception as err:
        logger.error(f"An error occurred: {err}")

    else:
        data_dict = response.json()
        logger.info(f"Result: {data_dict}")

        return data_dict

