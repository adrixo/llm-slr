from abc import ABC, abstractmethod
import requests
import pandas as pd
import urllib.parse

class BBDDSearchAPI(ABC):
    def __init__(self, api_key):
        self.api_key = api_key

    @abstractmethod
    def search(self, query: str) -> 'pd.DataFrame':
        '''
        Search in the database and return the results in a common format as pandas dataframe
        
        Parameters:
        query (str): The search query string.
        
        Returns:
        pandas.DataFrame: The search results in a pandas DataFrame.
        '''
        pass

class IEEEXploreSearchAPI(BBDDSearchAPI):
    def search(self, query):
        # URL encode the query
        encoded_query = urllib.parse.quote(query)

        # Construct the API URL
        url = (
            'http://ieeexploreapi.ieee.org/api/v1/search/articles'
            f'?apikey={self.api_key}'
            '&format=json'
            f'&querytext={encoded_query}'
        )
        # Send the GET request
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            for article in articles:
                print(f"Title: {article.get('title')}")
                print(f"DOI: {article.get('doi')}")
                print(f"Abstract: {article.get('abstract')}\n")

            return data
        else:
            print(f'Error: {response.status_code}')
            return None

class WebOfScienceSearchAPI(BBDDSearchAPI):
    def search(self, query):
        url = f"https://api.webofscience.com/search?apikey={self.api_key}&query={query}"
        response = requests.get(url)
        return response.json()

class SpringerLinkSearchAPI(BBDDSearchAPI):
    def search(self, query):
        url = f"https://api.springer.com/search?apikey={self.api_key}&query={query}"
        response = requests.get(url)
        return response.json()

class ScopusSearchAPI(BBDDSearchAPI):
    def search(self, query):
        url = f"https://api.elsevier.com/content/search/scopus?apikey={self.api_key}&query={query}"
        response = requests.get(url)
        return response.json()

def get_search_api(db_type, api_key):
    if db_type == "ieee_xplore":
        return IEEEXploreSearchAPI(api_key)
    elif db_type == "web_of_science":
        return WebOfScienceSearchAPI(api_key)
    elif db_type == "springerlink":
        return SpringerLinkSearchAPI(api_key)
    elif db_type == "scopus":
        return ScopusSearchAPI(api_key)
    else:
        raise ValueError(f"Tipo de base de datos no soportado: {db_type}")
