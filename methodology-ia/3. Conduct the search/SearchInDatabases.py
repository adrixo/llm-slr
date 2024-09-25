from ResearchDatabases import IEEEXploreSearchAPI, WebOfScienceSearchAPI, SpringerLinkSearchAPI, ScienceDirectAPI, get_search_api
import os
from dotenv import load_dotenv
import json

load_dotenv()

def main():

    # DDBB and queries from brainstorming
    ddbb_queries = {
        "ieee_xplore": '("llm" OR "large language model" OR "gpt" OR "llama" OR "mistral") AND ("recommender" OR "recsys") AND ("consumer hardware" OR "limitations" OR "issues" OR "efficient" OR "activity")',
        "web_of_science": '("llm" OR "large language model" OR "gpt" OR "llama" OR "mistral") AND ("recommender" OR "recsys") AND ("consumer hardware" OR "limitations" OR "issues" OR "efficient" OR "activity")',
        "springerlink": '("llm" OR "large language model" OR "gpt" OR "llama" OR "mistral") AND ("recommender" OR "recsys") AND ("consumer hardware" OR "limitations" OR "issues" OR "efficient" OR "activity")',
        "scopus": '("llm" OR "large language model" OR "gpt" OR "llama" OR "mistral") AND ("recommender" OR "recsys") AND ("consumer hardware" OR "limitations" OR "issues" OR "efficient" OR "activity")',
        "science_direct": '"llm" and "recommender"'
    }

    # API keys
    api_keys = {
        "ieee_xplore": "tu_api_key",
        "web_of_science": "tu_api_key",
        "springerlink": "tu_api_key",
        "scopus": "tu_api_key"
    }

    # Try first with ieee_xplore
    db_type = "science_direct"  # Cambia esto según el tipo de BBDD
    # Get from a .env file the api_key
    api_key = os.getenv("SCOPUS_API_KEY")
    query = ddbb_queries["science_direct"]
    search_api = get_search_api(db_type, api_key)
    df_resultados = search_api.search(query,"2017","2025",1000)

    # Deduplicar por DOI ()
    # Eliminar duplicados por DOI
    df_resultados_deduplicados = df_resultados.drop_duplicates(subset='doi', keep='first')
    
    # Guardar el DataFrame como CSV
    df_resultados_deduplicados.to_csv('resultados_busqueda.csv', index=False)
    
    # Mostrar un resumen de la información del DataFrame por pantalla
    print("\nResumen del DataFrame:")
    print(f"Número total de resultados: {len(df_resultados_deduplicados)}")
    print(f"Columnas: {', '.join(df_resultados_deduplicados.columns)}")
    print("\nPrimeras 5 filas:")
    print(df_resultados_deduplicados.head())
    print("\nInformación estadística:")
    print(df_resultados_deduplicados.describe(include='all'))
    print("\nDistribución de años:")
    print(df_resultados_deduplicados['year'].value_counts().sort_index())

if __name__ == "__main__":
    main()
