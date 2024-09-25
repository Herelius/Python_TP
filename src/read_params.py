import re
import argparse


def read_params() -> dict:
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="This function ")

    # Add personalized arguments
    parser.add_argument("--protocol", type=str, required=True, help="Can be (http or https)")
    parser.add_argument("--hostname", type=str, required=True, help="Hostname")
    parser.add_argument("--uri", type=str, required=True, help="URI")
    parser.add_argument("--threshold", type=int, required=True, help="Threashold")

    # Parsing arguments
    args = parser.parse_args()

    # Verify inputs
    regex_protocol = r"http|https"
    if not re.match(regex_protocol, args.protocol):
        raise Exception(f"Error : Protocol must be http or https.")

    regex_hostname = r'^(?:[^:\n]+://)?([^:#/\n]*)'
    if not re.match(regex_hostname, args.hostname):
        raise Exception(f"Error : {args.hostname} is not a hostname.")

    result = {
        "protocol": args.protocol,
        "hostname": args.hostname,
        "uri": args.uri,
        "threshold": args.threshold,
    }

    return result


if __name__ == '__main__':
    read_params()
