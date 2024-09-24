from ResearchDatabases import IEEEXploreSearchAPI, WebOfScienceSearchAPI, SpringerLinkSearchAPI, ScopusSearchAPI, get_search_api
import os
from dotenv import load_dotenv

load_dotenv()

def main():

    # DDBB and queries from brainstorming
    ddbb_queries = {
        "ieee_xplore": "(\\\"llm\\\" OR \\\"large language model\\\" OR \\\"gpt\\\" OR \\\"llama\\\" OR \\\"mistral\\\") AND (\\\"recommender\\\" OR \\\"recsys\\\") AND (\\\"consumer hardware\\\" OR \\\"limitations\\\" OR \\\"issues\\\" OR \\\"efficient\\\" OR \\\"activity\\\")",
        "web_of_science": "(\\\"llm\\\" OR \\\"large language model\\\" OR \\\"gpt\\\" OR \\\"llama\\\" OR \\\"mistral\\\") AND (\\\"recommender\\\" OR \\\"recsys\\\") AND (\\\"consumer hardware\\\" OR \\\"limitations\\\" OR \\\"issues\\\" OR \\\"efficient\\\" OR \\\"activity\\\")",
        "springerlink": "(\\\"llm\\\" OR \\\"large language model\\\" OR \\\"gpt\\\" OR \\\"llama\\\" OR \\\"mistral\\\") AND (\\\"recommender\\\" OR \\\"recsys\\\") AND (\\\"consumer hardware\\\" OR \\\"limitations\\\" OR \\\"issues\\\" OR \\\"efficient\\\" OR \\\"activity\\\")",
        "scopus": "(\\\"llm\\\" OR \\\"large language model\\\" OR \\\"gpt\\\" OR \\\"llama\\\" OR \\\"mistral\\\") AND (\\\"recommender\\\" OR \\\"recsys\\\") AND (\\\"consumer hardware\\\" OR \\\"limitations\\\" OR \\\"issues\\\" OR \\\"efficient\\\" OR \\\"activity\\\")"
    }

    # API keys
    api_keys = {
        "ieee_xplore": "tu_api_key",
        "web_of_science": "tu_api_key",
        "springerlink": "tu_api_key",
        "scopus": "tu_api_key"
    }

    # Try first with ieee_xplore
    db_type = "ieee_xplore"  # Cambia esto según el tipo de BBDD
    # Get from a .env file the api_key
    api_key = os.getenv("IEEE_XPLOR_API_KEY")
    query = '("llm" OR "large language model" OR "gpt" OR "llama" OR "mistral") AND ("recommender" OR "recsys")'

    search_api = get_search_api(db_type, api_key)
    resultados = search_api.search(query)
    print(resultados)

if __name__ == "__main__":
    main()
