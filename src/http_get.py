import requests


def http_get(url: str) -> dict:
    try:
        response = requests.get(url)
        response.raise_for_status()
    
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except Exception as err:
        print(f"An error occurred: {err}")

    else:
        return response.json()

