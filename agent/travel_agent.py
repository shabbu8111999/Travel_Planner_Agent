# Import ChatOpenAI to connect LangChain with OpenAI chat models
from langchain_openai import ChatOpenAI

# Import ChatPromptTemplate to create structured prompts
from langchain_core.prompts import ChatPromptTemplate

# Import StrOutputParser to convert model output into plain text
from langchain_core.output_parsers import StrOutputParser


# Function that builds and returns an AI travel planning chain
def create_travel_agent():
    """
    Creates an agentic travel planner using LangChain Runnable pipeline.
    This avoids unstable AgentExecutor imports while preserving agent logic.
    """

    # Initialize the OpenAI chat model
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2 # Low temperature for more deterministic output
    )

    # Defining the prompt template for the travel agent
    prompt = ChatPromptTemplate.from_template(
        """
        You are an intelligent AI travel agent.

        User request:
        {query}

        Use the following available data:
        - Flights
        - Hotels
        - Places
        - Weather
        - Budget

        Reason step by step and produce:
        1. Flight selection
        2. Hotel recommendation
        3. Day-wise itinerary
        4. Weather summary
        5. Budget breakdown

        Provide a clear, structured answer.
        """
    )

    # Create a runnable chain:
    # 1. Pass input to prompt
    # 2. Send prompt to LLM
    # 3. Parse output as string
    chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    return chain
