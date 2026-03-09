from fastapi import FastAPI
from fastmcp import Client
from pydantic import BaseModel

# IMPORTANT: This line must exist
app = FastAPI()

MCP_URL = "http://127.0.0.1:8002/mcp"


class ToolRequest(BaseModel):
    tool: str
    arguments: dict


@app.get("/tools")
async def list_tools():

    async with Client(MCP_URL) as client:
        tools = await client.list_tools()

        return {
            "tools": [
                {
                    "name": t.name,
                    "description": t.description
                }
                for t in tools
            ]
        }


@app.post("/tools")
async def call_tool(req: ToolRequest):

    async with Client(MCP_URL) as client:

        result = await client.call_tool(req.tool, req.arguments)

        return result.data