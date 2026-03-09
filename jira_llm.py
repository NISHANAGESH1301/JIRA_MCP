from langchain_community.chat_models import ChatOllama

llm = ChatOllama(
    base_url="http://10.247.79.122:8080",
    model="gpt-oss:20b",
    temperature=0
)