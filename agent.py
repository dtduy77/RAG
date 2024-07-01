from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-functions-agent")
# prompt.messages

agent = create_tool_calling_agent(llm, tools, prompt)



agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)