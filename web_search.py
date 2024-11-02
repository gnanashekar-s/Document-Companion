# web_search.py
import requests

def search_wikipedia(keyword):
    """
    Fetches a summary for the keyword from Wikipedia using the Wikipedia API.
    Returns a summary string if found, else returns None.
    """
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{requests.utils.quote(keyword)}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        
        if 'extract' in data:
            return data['extract']  # Return the summary text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None