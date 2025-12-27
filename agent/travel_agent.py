from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



def create_travel_agent():
    """
    Creates an agentic travel planner using LangChain Runnable pipeline.
    This avoids unstable AgentExecutor imports while preserving agent logic.
    """

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2
    )

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

    chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    return chain
