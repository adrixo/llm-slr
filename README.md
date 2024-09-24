# Repository of Systematic Literature Review on LLMs applied to Recommendation Systems employing IA assesing tools

This repository contains the code and resources for a systematic literature review (SLR) on the application of Large Language Models (LLMs) in recommendation systems and, at the same time, the evaluation of IA tools for performing SLR.

## Introduction

The systematic literature review (SLR) aims to identify and analyze the current state of research in the application of LLMs in recommendation systems. The SLR provides a comprehensive overview of the approaches, techniques, and evaluation metrics used in these fields, helping researchers and practitioners stay informed about the latest developments and trends.

At the same time, the SLR aims to evaluate the performance of IA tools for performing SLR and we use it in parallel to the human assessors in each step of the SLR for further evaluation of the IA tools and scripts.

## Methodology (HUMAN AND IA ASSESSMENT)

We have developed this systematic literature review following the guidelines of [Kitchenham and Charters](https://dl.acm.org/doi/10.1145/1134285.1134500). But in this case, we have used IA in a parallel way in each step of the SLR.
This allow us to evaluate the performance of the IA in each step of the SLR and to compare the results with the results obtained by the human assessors.


Previous work using this methodology: [SLR Music Recommendation](https://www.mdpi.com/2079-9292/10/13/1555)


The methodology is the following (for each step we have a folder with the IA assesment results):

### **1. Formulate the research questions**: Define the specific question or problem that the SLR aims to address.

- **RQ1**: What are the kinds of use of LLMs on the recommender systems nowadays? ( De acuerdo a este articulo https://dl.acm.org/doi/10.1145/3604915.3609494, existen tres formas: LLM como sistema de recomendación, LLM en el sistema de recomendación y sistema de recomendación en el LLM)
- **RQ2**: ¿Cuales son los principales modelos LLMs empleados en sistemas de recomendación y sus características: OSS API, licencia, numero de parámetros, (Sacar lista y tablita)
- **RQ3**: What evaluation metrics and methods have been employed to validate the effectiveness of these LLMs RS? [ MRR, etc.]
- **RQ4**: Which publicly available datasets are mainly used? Dominios de aplicación
- **RQ5**: It’s reproducible on consumer-level hardware or low (gpu) resources laboratory? Se excluyen trabajoss trabajos que usen APIs. Solo modelos pequeños como phi, etc.  API | High resoruces | Low Resources
- **RQ6**: What are the main open lines of research en los sistemas de recomedación que utilizan LLMs? (principales problemas)
    - Dividirla en dos: Lineas abiertas y problemas


> **IA ASSESSMENT IN THIS STEP**

> In this step a LLM as ChatGPT could be used for brainstorming the research questions in a collaborative way with the human assessors.
> Posible prompts are in the folder for this step in methodology/1_Formulate_the_research_questions.


### **2. Develop the search strategy**: Create a comprehensive search strategy using appropriate search terms, databases, and other resources.

#### 2.1 PICOC

- **Population (P)**: Recommender systems.
- **Intervention (I)**: LLM for recommender systems.
- **Comparison (C)**: there is no comparison intervention in this work due to the main objective of this work is review all the available llm integration approaches on recommender systems in the literature and explore new lines of research in this domain.
- **Outcomes (O)**: works about LLM on the recommender systems field.
- **Context (C)**: works related to recommender systems employing LLM in the industry or academia.

> **IA ASSESSMENT IN THIS STEP**

> In this step a LLM as ChatGPT could be used for brainstorming the PICOC in a collaborative way with the human assessors.
> Posible prompts are in the folder for this step in methodology/2. Develop a search strategy/2.1 PICOC.md

#### **2.2 Inclusion/exclusion criteria**

- **IC 1**: The paper covers a recommender system.
- **IC 2**: The recommender system employs a LLM.
- **IC 3:** The paper is written in English.
- **IC 4:** The work is published in peer review conferences, books or articles.
- **IC 5:** The work was published after 2017.

Most of the exclusion criteria are related to the inclusion criteria previously shown:

- **EC 1**: The paper is not concerned with a recommender system.
- **EC 2**: The recommender system does not employs a LLM.
- **EC 3:** The work is not written in English.
- **EC 4:** The work is not published in peer review conferences, books or articles.
- **EC 5:** The work was published prior to 2017.

> **IA ASSESSMENT IN THIS STEP**

> In this step a LLM as ChatGPT could be used for brainstorming the inclusion-exclusion criteria in a collaborative way with the human assessors.
> Posible prompts are in the folder for this step in methodology/2. Develop a search strategy/2.2 Inclusion-exclusion.md

#### **2.3 Search strategy / Query**

Upon establishing the inclusion and exclusion criteria, it is necessary to find the most relevant databases in which to search for research papers that meet the established criteria. At the same time, appropriate selection of the concepts is required in order to subsequently perform the queries in these databases.

The following databases have been selected for this work: 

- IEEE Xplore
- Web of Science
- SpringerLink
- Scopus

The main reasons for this decision are that they are databases in the scope of the research of this work and allow searches using search queries in a similar way to each other. The search concepts used were as follows:

- The term “llm” or “large language model” to search for large language models related works.
- The term “recommender”, “recsys”, to search for papers presenting recommendation algorithms.
- Consider alternative: Terms such as names of famous llms such as "gpt", "llama", "mistral", etc.
- Other terms such as “consumer hardware”, “limitations”, “issues”, “efficient”, “activity” that refer to the research questions proposed.


> **IA ASSESSMENT IN THIS STEP**

> In this step a LLM as ChatGPT could be used for brainstorming the search query in a collaborative way with the human assessors.
> Posible prompts are in the folder for this step in methodology/2. Develop a search strategy/2.3 Query Strings.md


#### **2.4 Query Strings**

Table with the query strings used in each database:

| Database | Query |
| -------- | -------- |
| IEEE Xplore | ("llm" OR "large language model") AND ("recommender" OR "recsys") |
| Web of Science | ("llm" AND "recommender") OR ("large language model" AND "recommender") |
| SpringerLink | ("llm" OR "large language model") AND ("recommender" OR "recsys") |
| Scopus | ("llm" AND "recommender") OR ("large language model" AND "recommender") |

#### **2.5 Quality criteria**

- Score 1: The article meets the established quality criterion.
- Score 0.75: The article meets most of the quality criterion.
- Score 0.5: The article partially meets the quality criterion.
- Score 0.25: The article meet only one or two of the quality criterion.
- Score 0: The article does not meet any of the quality criterion.

The quality criteria are as follows:

- The purpose of the work is the development of a recommender system employing LLMs.
- The paper applies the recommendation algorithm to datasets and presents a case study.
- The work includes the use of LLMs int the process of making recommendations.
- The paper describes how llms are employed in the recommender system.
- The paper presents used evaluation metrics for the proposed recommender system.
- The work uses publicly available datasets.
- The work uses open source LLMs.

### **3. Conduct the search**: Execute the search strategy across the required databases and gather a list of potentially relevant studies.

### **4. Eligibility criteria**: Define the eligibility criteria for the studies to be included in the SLR. This includes criteria such as study type, language, publication date, and authors.

### **5. Data collection**: Develop a data collection form to systematically gather the necessary data from the selected studies.

### **6. Data extraction**: Use the data collection form to extract the data from the selected studies.

### **7. Data cleaning**: Clean the data extracted from the studies to ensure its accuracy and consistency.

### **8. Data analysis**: Analyze the cleaned data using appropriate statistical or computational methods.

### **9. Results presentation**: Present the results of the SLR in a clear and informative manner.


## Repository Structure

The repository is organized as follows:

- `methodology/`: Contains the methodology used for the SLR, including the search strategy, the inclusion/exclusion criteria, and the data extraction form. This includes the use of IA in each step of the methodology and posible uses.
- `data/`: Contains the raw data used for the SLR, including the search results, the selected studies, and the data extraction forms.
- `csv/`: Contains the csv files with the results of the SLR, the data extraction forms and the human assessment of the IA.

## How to cite

If you use this repository in your work, please cite it as follows:

```
Pending to be defined
```

## Contact

If you have any questions, please contact the authors.
