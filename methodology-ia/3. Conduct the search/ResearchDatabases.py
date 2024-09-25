from abc import ABC, abstractmethod
import time
import requests
import pandas as pd
import urllib.parse
import pandas as pd
from tqdm import tqdm

class BBDDSearchAPI(ABC):
    def __init__(self, api_key):
        self.api_key = api_key

    @abstractmethod
    def search(self, query: str, init_year:str, end_year:str, max_results:int) -> 'pd.DataFrame':
        '''
        Search in the database and return the results in a common format as pandas dataframe
        
        Parameters:
        query (str): The search query string.
        
        Returns:
        pandas.DataFrame: The search results in a pandas DataFrame.
        '''
        pass

class IEEEXploreSearchAPI(BBDDSearchAPI):
    def search(self, query: str, init_year:str, end_year:str, max_results:int):
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
    def search(self, query: str, init_year:str, end_year:str, max_results:int):
        url = f"https://api.webofscience.com/search?apikey={self.api_key}&query={query}"
        response = requests.get(url)
        return response.json()

class SpringerLinkSearchAPI(BBDDSearchAPI):
    def search(self, query: str, init_year:str, end_year:str, max_results:int):
        url = f"https://api.springer.com/search?apikey={self.api_key}&query={query}"
        response = requests.get(url)
        return response.json()

class ScienceDirectAPI(BBDDSearchAPI):
    def search(self, query: str, init_year: str, end_year: str, max_results: int):
        # Inicializa el array donde se almacenarán todos los resultados
        all_entries = []

        # Definir el tamaño del bloque (máximo por solicitud)
        results_per_page = 100
        offset = 0

        # Mientras no tengamos todos los resultados
        for offset in tqdm(range(0, max_results, results_per_page), desc="Buscando resultados", unit="página"):
            # Construye el cuerpo de la solicitud con los filtros
            body = {
                "qs": query,  # Consulta de búsqueda
                "pub": "",  # Dejar vacío si no se quiere limitar a una publicación específica
                "filters": {
                    "openAccess": False,  # Filtrar por acceso abierto (True/False)
                    "date": {
                        "from": f"{init_year}-01-01",  # Fecha de inicio
                        "to": f"{end_year}-12-31"     # Fecha de fin
                    },
                },
                "display": {
                    "offset": offset,  # Desplazamiento para paginación
                    "show":results_per_page,
                }
                
            }

            # Establece las cabeceras
            headers = {
                'X-ELS-APIKey': self.api_key,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }

            # URL de la API de ScienceDirect Search V2
            url = 'https://api.elsevier.com/content/search/sciencedirect'

            # Envía la solicitud PUT
            response = requests.put(url, json=body, headers=headers)

            # Verifica si la solicitud fue exitosa
            if response.status_code == 200:
                data = response.json()
                entries = data.get('results', [])

                # Si no hay más resultados, salir del bucle
                if not entries:
                    break

                for entry in entries:
                    title = entry.get('title','')
                    journal = entry.get('sourceTitle','')
                    doi = entry.get('doi', '')
                    publication_date = entry.get('publicationDate', '')

                    # Añadir solo las entradas con DOI, título y fecha
                    all_entries.append({
                        'title': title,
                        'doi': doi,
                        'year': publication_date[:4] if publication_date != 'No date available' else 'No year available',
                        'journal':journal
                    })

                # Incrementa el offset para la próxima solicitud
                offset += results_per_page
                # Esperar un segundo para no alcanzar los límites de la API
                time.sleep(1)

            else:
                print(f'Error: {response.status_code}')
                print(response.text)
                break

        # Retorna todos los resultados obtenidos en formato JSON
        # Crear un DataFrame a partir de los registros
        df_all_entries = pd.DataFrame(all_entries)
    
        return df_all_entries

def get_search_api(db_type, api_key):
    if db_type == "ieee_xplore":
        return IEEEXploreSearchAPI(api_key)
    elif db_type == "web_of_science":
        return WebOfScienceSearchAPI(api_key)
    elif db_type == "springerlink":
        return SpringerLinkSearchAPI(api_key)
    elif db_type == "science_direct":
        return ScienceDirectAPI(api_key)
    else:
        raise ValueError(f"Tipo de base de datos no soportado: {db_type}")
