from fastmcp import FastMCP
import httpx
from services.jira_service import (
    get_jira_issue,
    search_high_priority_issues,
    create_jira_issue
)

mcp = FastMCP("Operations MCP")


# @mcp.tool()
# async def get_jira_issue_tool(issueKey: str) -> str:
#     """
#     Get Jira issue details by issue key
#     """
#     try:
#         result = get_jira_issue(issueKey)
#         return str(result)
#     except Exception as e:
#         return f"Error: {str(e)}"
@mcp.tool()
async def get_jira_issue_tool(issueKey: str):
    """
    Get Jira issue details by issue key
    """
    try:
        result = get_jira_issue(issueKey)
        return result   # ❗ NOT str(result)
    except Exception as e:
        return {"error": str(e)}
@mcp.tool()
async def search_high_priority_issues_tool(projectKey: str):
    try:
        result = search_high_priority_issues(projectKey)
        return result
    except Exception as e:
        return {"error": str(e)}
# @mcp.tool()
# async def search_high_priority_issues_tool(projectKey: str) -> str:
#     """
#     Search high priority Jira issues in a project
#     """
#     try:
#         result = search_high_priority_issues(projectKey)
#         return str(result)
#     except Exception as e:
#         return f"Error: {str(e)}"


# @mcp.tool()
# async def create_jira_issue_tool(
#     projectKey: str,
#     summary: str,
#     description: str
# ) -> str:
#     """
#     Create a new Jira issue
#     """
#     try:
#         result = create_jira_issue(projectKey, summary, description)
#         return str(result)
#     except Exception as e:
#         return f"Error: {str(e)}"


# if __name__ == "__main__":
#    mcp.run(transport="http", port=8002)
if __name__ == "__main__":
   mcp.run(transport="sse", port=3001, host="0.0.0.0")