import requests
from pydantic import HttpUrl

def http_get_request(url: HttpUrl) -> str:
    """
    Get the data from the website
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        return response.text

