import asyncio
from fastmcp import Client

async def main():
    # Use async context manager
    async with Client("http://127.0.0.1:8002/mcp") as client:
        # List all registered tools
        tools = await client.list_tools()
        print("Tools available:")
        print(tools)

        # Call your Jira tool
        result = await client.call_tool(
            "get_jira_issue_tool",   # Name of the tool function
            {"issueKey": "SFBB-9418"}  # Arguments as a dict
        )
        print("\nTool result:")
        print(result)

# Run the async main
asyncio.run(main())