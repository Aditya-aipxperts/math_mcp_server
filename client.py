from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

async def main():
    client = MultiServerMCPClient({
        "math": {
            "url": "https://your-math-mcp.onrender.com/mcp",  # Replace with actual URL
            "transport": "streamable_http"
        }
    })

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(model, tools)

    # Math call
    math_response = agent.invoke({
        "messages": [{"role": "user", "content": "what is (3 * 5) + 15?"}]
    })
    print("Math-RESPONSE:", math_response["messages"][-1].content)

asyncio.run(main())





# from langchain_mcp_adapters.client import MultiServerMCPClient
# from langgraph.prebuilt import create_react_agent
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# import os

# load_dotenv()

# import asyncio

# async def main():
#     client = MultiServerMCPClient({
#         "math": {
#             "url": "https://your-math-mcp.onrender.com/mcp",
#             "transport": "streamable_http"
#             },
#         "weather": {
#                 "url": "http://localhost:8000/mcp",  # Ensure server is running here
#                 "transport": "streamable_http",
#             }
#     })

#     os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
#     tools = await client.get_tools()
#     model = ChatGroq(model="qwen-qwq-32b")
#     agent = create_react_agent(model, tools)

#     # Math call (synchronous)
#     math_response = agent.invoke({
#         "messages": [{"role": "user", "content": "what is (3 * 5) + 15?"}]
#     })
#     print("Math-RESPONSE:", math_response["messages"][-1].content)

#     # Weather call (also synchronous)
#     weather_response = await agent.ainvoke(
#         {"messages": [{"role": "user", "content": "what is the weather in California?"}]}
#     )
#     print("Weather response:", weather_response['messages'][-1].content)

# asyncio.run(main())