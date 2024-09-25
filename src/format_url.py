import re


def format_url(protocol: str, hostname: str, uri: str) -> str:
    # Verify
    regex_protocol = r"http|https"
    if not re.match(regex_protocol, protocol):
        raise Exception(f"Error : Protocol must be http or https.")

    regex_hostname = r'^(?:[^:\n]+://)?([^:#/\n]*)'
    if not re.match(regex_hostname, hostname):
        raise Exception(f"Error : {args.hostname} is not a hostname.")

    if uri.startswith("/"):
        return f"{protocol}://{hostname}{uri}"

    else: 
        return f"{protocol}://{hostname}/{uri}"
        
