from dotenv import load_dotenv
from langchain_core.tools import Tool, render_text_description, tool
from langchain_core.prompts import PromptTemplate
from langchain_core.agents import AgentAction, AgentFinish
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.output_parsers.react_single_input import ReActSingleInputOutputParser

load_dotenv()

@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    return len(text)

def main():
    print("Hello from react-langchain!")
    
    tools = [get_text_length]

    template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought:
    """

    prompt = PromptTemplate.from_template(template=template).partial(
        tools=render_text_description(tools),
        tool_names=", ".join([t.name for t in tools]),
    )

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash").bind(stop=["\nObservation", "Observation"])
    agent = { "input": lambda x: x["input"]} | prompt | llm | ReActSingleInputOutputParser() 

    res = agent.invoke({"input": "What is the length of 'DOG' in characters?"})
    print(res)
if __name__ == "__main__":
    main()
