# Research Assistant 

## Overview
Research Assistant application that leverages the power of large language models (LLMs), specifically LLAMA-3, to perform comprehensive web searches and generate detailed reports based on user queries. It integrates multiple components to facilitate automated research, including web scraping, search queries, and report generation, all within a Streamlit web application.

Research Assistant is deployed on **Streamlit Cloud**, utilizing streamlit community cloud servers and computing. For **LLAMA-3** computation and processing, I used **[GROQ](https://groq.com/)**, Fastest AI inference

## Features
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
To set up and run the project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Abhishekvidhate/Research-Assistant.git
   cd research-assistant
