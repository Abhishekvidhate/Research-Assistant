# Research Assistant 

## Overview
Research Assistant application that leverages the power of large language models (LLMs), specifically LLAMA-3, to perform comprehensive web searches and generate detailed reports based on user queries. It integrates multiple components to facilitate automated research, including web scraping, search queries, and report generation, all within a Streamlit web application.

Research Assistant is deployed on **Streamlit Cloud**, utilizing streamlit community cloud servers and computing. For **LLAMA-3** computation and processing, I used **[GROQ](https://groq.com/)**, Fastest AI inference

## APP

[Research Assistant hosted on Streamlit Cloud Application's working link](https://research-assistant-aves.streamlit.app/) 
![image](https://github.com/Abhishekvidhate/Research-Assistant/assets/120262589/1370f851-8b01-4e3e-a0a5-43548f7cf4c8)

### Demon video :

[Google Drive video link](https://drive.google.com/file/d/1TuMz2GVPJFLGkmI28bMIIYaJP3zC8Gql/view?usp=drive_link)

## Features
- **LangSmith Tracing:** Uses Langsmith for tracing, monitoring and etc LLMOps tasks
![image](https://github.com/Abhishekvidhate/Research-Assistant/assets/120262589/29c4561c-7b25-4411-aa29-d1b877f8815e)

- **Real-time Web Search:** Performs web searches using DuckDuckGo and Tavily APIs to retrieve relevant information.
- **Web Scraping:** Extracts text from web pages using BeautifulSoup.
- **Search Query Generation:** Utilized LANGCHAIN Ecosystem to create optimized search queries 
- **Report Generation:** Generates detailed research reports, bibliographies, and outlines using templates.

## Components
The project consists of three main components: `web.py`, `writer.py`, and `chain.py`.

### 1. `web.py`
Handles web searches and text extraction.

#### Key Functions:
- **scrape_text(url: str):** Extracts text from the given URL.
- **web_search(query: str, num_results: int):** Performs a web search and returns a list of URLs.
- **get_links:** Retrieves links based on the search query.
- **scrape_and_summarize:** Scrapes text from URLs and summarizes the content.

### 2. `writer.py`
Generates reports based on the summarized research data.

#### Key Templates:
- **RESEARCH_REPORT_TEMPLATE:** Template for generating detailed research reports.
- **RESOURCE_REPORT_TEMPLATE:** Template for generating bibliography recommendations.
- **OUTLINE_REPORT_TEMPLATE:** Template for generating report outlines.

### 3. `chain.py`
Combines `web.py` and `writer.py` into a cohesive chain for end-to-end functionality.

#### Key Classes:
- **InputType:** Defines the input type for the chain.
- **chain:** The main chain combining search and writing functionalities.

### 4. `app.py`
The Streamlit web application that provides a user interface for interacting with the research assistant.

#### Key Elements:
- **Streamlit UI:** Accepts user input and displays the generated reports.
- **Integration with `chain.py`:** Uses the combined chain to process user queries and generate results.

## Installation
To set up and run the project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Abhishekvidhate/Research-Assistant.git
   cd research-assistant

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Set Environment Variables(for windows command prompt):**
   ```bash
   set LANGCHAIN_API_KEY=your_langchain_api_key
   set GROQ_API_KEY=your_groq_api_key
   set LANGCHAIN_PROJECT=your_langchain_project
   set TAVILY_API_KEY=your_tavily_api_key

5. **Run the Streamlit Application:**
   ```bash
   streamlit run app.py

The App will run on local host


## Acknowledgements
- [LangChain](https://www.langchain.com/) for the APIs and tools.
- [LangSmith](https://www.langchain.com/langsmith) for all response and workflow tracing & monitoring of LLM/LLAMA-3 & project
- [Streamlit](https://www.streamlit.io/) for the web application framework.

