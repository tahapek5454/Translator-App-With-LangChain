from dotenv import load_dotenv, get_key
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model = get_key(".env", "AZURE_OPENAI_MODEL_NAME")
deployment = get_key(".env", "AZURE_OPENAI_DEPLOYMENT")

# Key, Endpoint, Version infos get automatically loaded from the environment variables
llm = AzureChatOpenAI(
    model=model,
    deployment_name=deployment,
    temperature=0.1 # between 0 and 1, lower is more deterministic, higher is more creative
)

messages = [
        SystemMessage(content="Translate to following from Turkish to English:"),
        HumanMessage(content="Fransa'nın başkenti neresidir?")
]

if __name__ == "__main__":
    response = llm.invoke(messages)
    print(response.content)