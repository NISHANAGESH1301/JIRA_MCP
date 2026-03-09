from jira_llm import llm
from fastmcp import Client

SYSTEM_PROMPT = """
You are a Jira assistant.

Available tools:
1. get_jira_issue_tool(issueKey)
2. search_high_priority_issues_tool(projectKey)

If the user asks about a Jira ticket like ABC-123,
use get_jira_issue_tool.

If the user asks about urgent issues in a project,
use search_high_priority_issues_tool.
"""

async def run_agent(user_input):

    # Ask LLM what to do
    response = llm.invoke([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ])

    print("FULL RESPONSE:", response)

    tool_calls = response.response_metadata.get("message", {}).get("tool_calls", [])

    if tool_calls:

        tool_name = tool_calls[0]["function"]["name"]
        arguments = tool_calls[0]["function"]["arguments"]

        print("TOOL:", tool_name)
        print("ARGS:", arguments)

        # Use FastMCP Client
        async with Client("http://127.0.0.1:8002/mcp") as client:

            result = await client.call_tool(tool_name, arguments)

            data = result.data
            final_response = llm.invoke([
            {"role": "system", "content": "You are a Jira assistant. Answer the user's question using the Jira data."},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": f"Tool returned this Jira data: {data}"}
             ])

            return final_response.content

    return response.content