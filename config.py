import os
from dotenv import load_dotenv

load_dotenv()

JIRA_BASE = os.getenv("JIRA_BASE")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")