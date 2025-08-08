from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model=gemini-2.5-flash,
    tools=[],
    prompt="",
)

agent.invoke