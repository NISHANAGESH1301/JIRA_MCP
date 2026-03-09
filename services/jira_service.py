import requests
from config import JIRA_BASE, JIRA_TOKEN
from models.incident_model import map_jira_to_incident

headers = {
    "Authorization": f"Bearer {JIRA_TOKEN}",
    "Accept": "application/json"
}

def get_jira_issue(issue_key: str):
    url = f"{JIRA_BASE}/rest/api/2/issue/{issue_key}"
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return map_jira_to_incident(response.json())


def search_high_priority_issues(project_key: str):
    jql = f'project = "{project_key}" AND priority = High AND status != Done'
    url = f"{JIRA_BASE}/rest/api/2/search"
    response = requests.post(url, json={"jql": jql}, headers=headers, timeout=10)
    response.raise_for_status()

    issues = response.json()["issues"]
    return [map_jira_to_incident(issue) for issue in issues]


def create_jira_issue(project_key: str, summary: str, description: str):
    url = f"{JIRA_BASE}/rest/api/2/issue"

    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Task"}
        }
    }

    response = requests.post(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()

    return {
        "id": response.json()["key"],
        "message": "Issue created successfully"
    }