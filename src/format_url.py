import re


def format_url(protocol: str, hostname: str, uri: str) -> str:
    regex_protocol = r"http|https"
    if not re.match(regex_protocol, protocol):
        raise ValueError("Error : Protocol must be http or https.")
    
    regex_hostname = r'^(?:[^:\n]+://)?([^:#/\n]*)'
    if not re.match(regex_hostname, hostname):
        raise ValueError(f"Error : {hostname} is not a hostname.")
    
    if uri.startswith("/"):
        return f"{protocol}://{hostname}{uri}"
    
    else: 
        return f"{protocol}://{hostname}/{uri}"
        
