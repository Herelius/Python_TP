import re
import argparse


def read_params(args) -> dict:
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
