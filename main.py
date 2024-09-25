import logging

from src import format_url, http_get, read_params

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    logging.info("Start")
    logging.info("========================================")
    
    # PART http_get:
    # ------------------------------------------------------------------------------------
    url = "https://dummyjson.com/products"
    logging.info(f"Starting executing function 'http_get' ...")
    result_http_get = http_get(url)
    
    logging.info(f"Result of 'http_get' function: parameter 'url' = {url}:")
    logging.info(f"{result_http_get}\n")
    # ------------------------------------------------------------------------------------
    
    # PART read_params:
    # ------------------------------------------------------------------------------------
    logging.info(f"Starting executing function 'read_params' ...")
    result_read_params = read_params()
    
    logging.info(f"Result of 'http_get' function:")
    logging.info(f"{result_read_params}\n")
    # ------------------------------------------------------------------------------------
    
    # PART format_url:
    # ------------------------------------------------------------------------------------
    logging.info(f"Starting executing function 'format_url' ...")
    protocol = "https"
    hostname = "google.com"
    uri = "fr"
    result_format_url = format_url(protocol, hostname, uri)

    logging.info(f"Result of 'format_url' function: parameter 'protocol' = '{protocol}', 'hostname' = '{hostname}', uri = '{uri}:")
    logging.info(f"{result_format_url}\n")
    # ------------------------------------------------------------------------------------
    
    logging.info("========================================")
    logging.info("END")
    
