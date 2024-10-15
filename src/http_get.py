import logging
import requests
from time import monotonic
from requests import HTTPError

from .ThresholdExceededException import ThresholdExceededException

logger = logging.getLogger(__name__)


def http_get(url: str, threshold: int) -> dict or None:
    try:
        t0 = monotonic()
        response = requests.get(url)
        
        exec_time = monotonic() - t0
        if exec_time > threshold:
            raise ThresholdExceededException(threshold, exec_time)
        
        response.raise_for_status()
    
    except HTTPError as http_err:
        logger.error(f"URL {url} doesn't exists!")
        raise http_err

    except ThresholdExceededException as threshold_err:
        logger.error(f"An error occurred: {threshold_err}")
        raise threshold_err

    except Exception as err:
        logger.error(f"An error occurred: {err}")
        raise err

    else:
        data_dict = response.json()

        return data_dict

