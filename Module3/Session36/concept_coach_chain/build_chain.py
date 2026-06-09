# pip install langchain-ollama
# pip install langchain-core
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

OLLAMA_BASE_URL = "http://localhost:11434"
API_PATH = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen:1.8b"

def build_chain():
    
    """
    prompt template -> ChatOllama -> Output parser

    """

    # Build chat prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",
             """You are a beginner-friendly programming instructor.

             Rules:
            - Explain the concept clearly.
            - Use exactly 3 bullet points.
            - Each bullet point should be short.
            - Do not add an introduction.
            - Do not add a conclusion.
             """),
             (
                 "human",
                "Explain {topic} using a simple analogy from {analogy_domain}."
             )
        ]
    )

    # Build the model
    llm = ChatOllama(
        model=MODEL_NAME,
        base_url=OLLAMA_BASE_URL,
        temperature=1,
        num_predict=100
    )

    