# JIRA_MCP

JIRA_MCP
Overview

JIRA_MCP is a Python-based Model Context Protocol (MCP) server that enables AI assistants such as LibreChat to securely interact with Atlassian Jira.

Using MCP, AI models can communicate with external systems through a standardized interface instead of relying on custom integrations. This makes it easier to expose Jira functionality (such as creating issues, searching tickets, updating issues, or retrieving project information) to AI applications.

# What is MCP?
Model Context Protocol (MCP) is an open protocol that standardizes how AI applications connect with external tools, APIs, databases, and services.

Rather than building separate integrations for every AI application, MCP provides a common interface between:

AI Clients (LibreChat, Claude Desktop, etc.)
MCP Servers (such as this Jira MCP Server)
External Services (Jira, GitHub, Databases, Slack, etc.)

# Without MCP:

Every AI application requires its own Jira integration.
Different authentication methods must be implemented repeatedly.
Tool definitions differ between applications.
Maintenance becomes difficult.

# With MCP:

One standardized integration works across multiple AI clients.
Easier maintenance.
Reusable tools.
Better security.
Consistent communication protocol.
Why JIRA_MCP?

This project provides an MCP server that exposes Jira functionality to AI assistants.

The exact capabilities depend on the tools implemented in the project.

Features
Python-based MCP Server
Jira REST API integration
Easy integration with LibreChat
Extensible tool architecture
Environment-based configuration
Secure authentication
Lightweight and easy to deploy

# Prerequisites

Before running the server, ensure you have:

Python 3.10 or later
Jira Cloud account
Jira API Token
Internet access
Virtual environment 

Clone the repository:
git clone <repository-url>
cd JIRA_MCP

Create a virtual environment:

python -m venv venv

Activate it.

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Configuration

Create a .env file.

Example:

JIRA_BASE=https://your-domain.atlassian.net

JIRA_API_TOKEN=your-api-token

Do not commit your .env file to source control.

Running the MCP Server

Start the server using Python:

python jira_mcp_server.py


# Connecting to LibreChat

LibreChat supports MCP servers, allowing AI models to call external tools.

Configure your MCP server inside LibreChat by adding the server configuration.


Restart LibreChat after updating the MCP configuration.

Once connected, the AI assistant can invoke the Jira tools exposed by this MCP server.

# How It Works
User asks LibreChat a Jira-related question.
LibreChat identifies the required MCP tool.
The request is sent to the JIRA_MCP server.
The MCP server calls the Jira REST API.
Jira returns the requested information.
The MCP server formats the response.
LibreChat presents the result to the user.


The MCP server securely authenticates with Jira using these credentials.Make sure gudrails in place where ever required.


New tools can be added easily by implementing additional MCP tool functions.

# Examples:

Create Sprint
Close Issue
Transition Issue
Search Projects
Get Boards
Get Sprints
Add Attachments
Manage Users
Example Workflow

