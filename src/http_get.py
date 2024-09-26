import logging
import requests
from time import time
from requests import HTTPError

from .ThresholdExceededException import ThresholdExceededException

logger = logging.getLogger(__name__)


def http_get(url: str, threshold: int) -> dict:
    try:
        t0 = time()
        response = requests.get(url)
        
        exec_time = time() - t0
        if exec_time > threshold:
            raise ThresholdExceededException(exec_time, threshold)
        
        response.raise_for_status()
    
    except HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")

    except ThresholdExceededException as threshold_err:
        logger.error(f"An error occurred: {threshold_err}")

    except Exception as err:
        logger.error(f"An error occurred: {err}")

    else:
        data_dict = response.json()
        logger.info(f"Result: {data_dict}")

        return data_dict

