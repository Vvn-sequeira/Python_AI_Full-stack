from deepagents import create_deep_agent

def get_My_Name():
    """this funtion tell the Name of the person who created this"""
    return "My name is VVN "

agent = create_deep_agent(
    tools=[get_My_Name],
    system_prompt="You are a helpfuull assistant to find out the Name Strictly use the given Tools for answering!!"
)

result = agent.invoke(
    {"message":
        [
          {
            "role":"user" ,
            "content":"What is his Name? "
           }
        ]
     }
)

print(result["messages"][-1].content)