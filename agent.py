from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import Tool
from langchain.prompts import PromptTemplate
from tools.vector import kg_qa
from tools.cypher import cypher_qa

# Include the LLM from a previous lesson
from llm import llm

tools = [
    Tool.from_function(
        name="General Chat",
        description="For general chat not covered by other tools",
        func=llm.invoke,
        return_direct=True
    ),
    Tool.from_function(
        name="Vector Search Index",  # (1)
        description="Provides information about movie plots using Vector Search", # (2)
        func = kg_qa, # (3)
        return_direct=True
    ),
    Tool.from_function(
        name="Graph Cypher QA Chain",  # (1)
        description="Provides information about Movies including their Actors, Directors and User reviews", # (2)
        func = cypher_qa, # (3)
        return_direct=True
    ),
]

from langchain.chains.conversation.memory import ConversationBufferWindowMemory
memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True,
)



# agent_prompt = hub.pull("hwchase17/react-chat")

agent_prompt = PromptTemplate.from_template("""
You are a movie expert providing information about movies.
Be as helpful as possible and return as much information as possible.
Do not answer any questions that do not relate to movies, actors or directors.

Do not answer any questions using your pre-trained knowledge, only use the information provided in the context.

TOOLS:
------

You have access to the following tools:

{tools}

To use a tool, please use the following format:

```
Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

```
Thought: Do I need to use a tool? No
Final Answer: [your response here]
```

Begin!

Previous conversation history:
{chat_history}

New input: {input}
{agent_scratchpad}
""")

agent = create_react_agent(llm, tools, agent_prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    # handle_parsing_errors=True
    )

####################################################################################################
# These are from solutions/tools/vector.py and solutions/tools/cypher.py
# Take only the last one from cypher.py because it work backwards
####################################################################################################

# def generate_response(prompt):
#     """
#     Create a handler that calls the Conversational agent
#     and returns a response to be rendered in the UI
#     """
#     response = agent_executor.invoke({"input": prompt})
#     return response['output']

# def generate_response(prompt):
#     """
#     Use the Neo4j Vector Search Index
#     to augment the response from the LLM
#     """
#     # Handle the response
#     response = kg_qa({"query": prompt})
#     return response['result']

def generate_response(prompt):
    """
    Use the Neo4j recommendations dataset to provide
    context to the LLM when answering a question
    """

    try:
        # Handle the response
        response = cypher_qa.run(prompt)
        return response
    except Exception as e:
        # Handle the exception
        print(f"An error occurred: {str(e)}")
        return "Sorry, I don't know the answer to that."
