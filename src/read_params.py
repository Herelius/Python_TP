import re


def read_params(args) -> dict:
    result = {
        "protocol": args.protocol,
        "hostname": args.hostname,
        "uri": args.uri,
        "threshold": args.threshold,
    }

    return result

