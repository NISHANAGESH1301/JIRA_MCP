def map_jira_to_incident(issue):
    return {
        "id": issue["key"],
        "source": "JIRA",
        "summary": issue["fields"]["summary"],
        "status": issue["fields"]["status"]["name"],
        "priority": issue["fields"].get("priority", {}).get("name"),
        "assignee": (
            issue["fields"]["assignee"]["displayName"]
            if issue["fields"].get("assignee")
            else None
        ),
        "createdAt": issue["fields"]["created"]
    }