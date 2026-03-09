import asyncio
from jira_agent import run_agent

print("Jira AI Chatbot Ready")

while True:

    user = input("\nYou: ")

    if user == "exit":
        break

    response = asyncio.run(run_agent(user))

    print("\nAI:", response)