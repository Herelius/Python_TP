import logging
import argparse
import re

from src import format_url, http_get, read_params

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="This function reads params and returns them.")
    
    # Add personalized arguments
    parser.add_argument("--protocol", type=str, required=True, choices=['http', 'https'], help="Can be (http or https)")
    parser.add_argument("--hostname", type=lambda x: re.match(r'^(?:[^:\n]+://)?([^:#/\n]*)', x).group(0), required=True, help="Hostname")
    parser.add_argument("--uri", type=str, required=True, help="URI")
    parser.add_argument("--threshold", type=int, required=True, help="Threashold")

    # Parsing arguments
    args = parser.parse_args()
    
    
    logging.info("Start")
    logging.info("========================================")
    
    # PART http_get:
    # ------------------------------------------------------------------------------------
    url = "https://dummyjson.com/products"
    logging.info(f"Starting executing function 'http_get' ...")
    result_http_get = http_get(url, args.threshold)
    
    logging.info(f"Result of 'http_get' function: parameter 'url' = {url}:")
    logging.info(f"{result_http_get}\n")
    # ------------------------------------------------------------------------------------
    
    # PART read_params:
    # ------------------------------------------------------------------------------------
    logging.info(f"Starting executing function 'read_params' ...")
    result_read_params = read_params(args)
    
    logging.info(f"Result of 'http_get' function:")
    logging.info(f"{result_read_params}\n")
    # ------------------------------------------------------------------------------------
    
    # PART format_url:
    # ------------------------------------------------------------------------------------
    logging.info(f"Starting executing function 'format_url' ...")
    result_format_url = format_url(args.protocol, args.hostname, args.uri)

    logging.info(f"Result of 'format_url' function: parameter 'protocol' = '{args.protocol}', 'hostname' = '{args.hostname}', uri = '{args.uri}:")
    logging.info(f"{result_format_url}\n")
    # ------------------------------------------------------------------------------------
    
    logging.info("========================================")
    logging.info("END")
    
