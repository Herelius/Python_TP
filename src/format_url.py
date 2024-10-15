import requests
import logging

logger = logging.getLogger(__name__)


def format_url(protocol: str, hostname: str, uri: str) -> str:
    url = f"{protocol}://{hostname}{uri}" if uri.startswith("/") else f"{protocol}://{hostname}/{uri}"
    response = requests.get(url)
    if response.status_code == 200:
        logger.info(f'{url} Web site exists')
        return url

    print('Web site does not exist') 

        
