# Perform the search automatically in each database

Certainly! Here's how you can access each of the mentioned scientific databases programmatically using Python, along with examples to help you start retrieving articles.

---

### **1. IEEE Xplore**

**Access Method:**

- **IEEE Xplore API**: IEEE provides a RESTful API that allows you to search and retrieve metadata of articles.
- **Requirements**:
  - **API Key**: Register at the [IEEE Developer Portal](https://developer.ieee.org/) to obtain an API key.
  - **Python Libraries**: Use the `requests` library to make HTTP requests.

**Example in Python:**

```python
import requests

# Replace with your actual API key
API_KEY = 'your_ieee_api_key'

# Define your search query
query = 'machine learning'

# Construct the API URL
url = (
    'http://ieeexploreapi.ieee.org/api/v1/search/articles'
    f'?apikey={API_KEY}'
    '&format=json'
    '&max_records=10'
    '&start_record=1'
    f'&querytext={query}'
)

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    articles = data.get('articles', [])
    for article in articles:
        print(article.get('title'))
else:
    print(f'Error: {response.status_code}')
```

**Notes:**

- Replace `'your_ieee_api_key'` with your actual IEEE Xplore API key.
- The `querytext` parameter specifies your search query.
- The API returns metadata; full-text access requires appropriate subscriptions.

---

### **2. Web of Science**

**Access Method:**

- **Web of Science API**: Allows access to bibliographic data and citation metrics.
- **Requirements**:
  - **API Key and Credentials**: Obtain from the [Clarivate Developer Portal](https://developer.clarivate.com/).
  - **Python Libraries**: Use `requests` for RESTful APIs.

**Example in Python:**

```python
import requests

# Replace with your actual API key
API_KEY = 'your_wos_api_key'

# Define your search query
query = 'TS=("machine learning")'

# Construct the API URL
url = (
    'https://api.clarivate.com/api/woslite/v1/wos'
    f'?databaseId=WOS'
    f'&usrQuery={query}'
    '&count=10'
    '&firstRecord=1'
)

# Set the headers with your API key
headers = {
    'X-ApiKey': API_KEY,
    'Accept': 'application/json'
}

# Send the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    records = data.get('Data', {}).get('Records', {}).get('records', [])
    for record in records:
        print(record.get('Title', 'No Title Found'))
else:
    print(f'Error: {response.status_code}')
```

**Notes:**

- Replace `'your_wos_api_key'` with your actual Web of Science API key.
- The query uses the Web of Science search syntax (`TS` stands for Topic Search).
- Access may require institutional credentials and subscriptions.

---

### **3. SpringerLink**

**Access Method:**

- **Springer Nature Open Access API**: Provides metadata for open-access articles and books.
- **Requirements**:
  - **API Key**: Obtain a free API key from the [Springer Nature API Portal](https://dev.springernature.com/).
  - **Python Libraries**: Use `requests` to interact with the API.

**Example in Python:**

```python
import requests

# Replace with your actual API key
API_KEY = 'your_springer_api_key'

# Define your search query
query = 'machine learning'

# Construct the API URL
url = (
    f'https://api.springernature.com/meta/v2/json'
    f'?q={query}'
    f'&api_key={API_KEY}'
    '&p=10'  # Number of results per page
)

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    records = data.get('records', [])
    for record in records:
        print(record.get('title'))
else:
    print(f'Error: {response.status_code}')
```

**Notes:**

- Replace `'your_springer_api_key'` with your actual API key.
- The parameter `p` specifies the number of results per page.
- Only open-access content is available through this API.

---

### **4. Scopus**

**Access Method:**

- **Elsevier Scopus API**: Provides access to Scopus data, including articles and citations.
- **Requirements**:
  - **API Key**: Register at the [Elsevier Developer Portal](https://dev.elsevier.com/).
  - **Python Libraries**: Use `pybliometrics`, which simplifies interaction with the Scopus API.
  - **Configuration**: Set up `pybliometrics` with your API key.

**Installation:**

```bash
pip install pybliometrics
```

**Configuration:**

- Run `pybliometrics`'s interactive configuration:

  ```bash
  python -m pybliometrics.scopus.utils.create_config
  ```

- Enter your API key and other requested information.

**Example in Python:**

```python
from pybliometrics.scopus import ScopusSearch

# Define your search query
query = 'TITLE-ABS-KEY("machine learning")'

# Perform the search
s = ScopusSearch(query, subscriber=True)

# Print the number of results
print(f"Number of results: {s.get_results_size()}")

# Iterate through the results
for result in s.results:
    print(result.title)
```

**Notes:**

- Set `subscriber=True` if you have institutional access; otherwise, set it to `False`.
- The query uses Scopus search syntax.
- Full access may require an institutional subscription.

---

### **General Considerations for All APIs**

- **API Keys and Access**:
  - Ensure you have valid API keys and necessary permissions.
  - Some APIs may require institutional subscriptions or additional authentication.

- **Rate Limits and Usage Policies**:
  - Be mindful of each API's rate limits to avoid exceeding them.
  - Read and comply with the terms of service for each API.

- **Data Handling**:
  - APIs typically return data in JSON format.
  - Use Python's built-in `json` module or pandas for data parsing and manipulation.

- **Error Handling**:
  - Check the HTTP status codes returned by API requests.
  - Implement try-except blocks to handle exceptions and errors gracefully.

---

### **Additional Resources**

- **IEEE Xplore API**:
  - [Developer Portal](https://developer.ieee.org/)
  - [API Documentation](https://developer.ieee.org/docs)
- **Web of Science API**:
  - [Developer Portal](https://developer.clarivate.com/)
  - [API Documentation](https://developer.clarivate.com/apis)
- **Springer Nature API**:
  - [API Portal](https://dev.springernature.com/)
  - [API Documentation](https://dev.springernature.com/docs)
- **Elsevier Scopus API**:
  - [Developer Portal](https://dev.elsevier.com/)
  - [pybliometrics Documentation](https://pybliometrics.readthedocs.io/)

---

By following these steps and using the provided examples, you can start retrieving articles programmatically from each database using Python. Make sure to explore the full capabilities of each API by consulting their official documentation, as there are many additional parameters and features that can enhance your searches.