from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnablePassthrough
from search.web import chain as search_chain
from search.writer import chain as writer_chain
import os

# # Access environment variables
# LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
# GROQ_API_KEY = os.getenv('GROQ_API_KEY')
# LANGCHAIN_PROJECT = os.getenv('LANGCHAIN_PROJECT')
# TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
# os.environ["LANGCHAIN_TRACING_V2"] = "true"

chain_notypes = (
        RunnablePassthrough().assign(research_summary=search_chain) | writer_chain
)


class InputType(BaseModel):
    question: str


chains = chain_notypes.with_types(input_type=InputType)

