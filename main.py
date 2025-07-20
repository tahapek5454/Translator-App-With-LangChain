from simple_message import get_chain
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
        SystemMessage(content="Translate to following from Turkish to English:"),
        HumanMessage(content="Fransa'nın başkenti neresidir?")
]

if __name__ == "__main__":
    chain = get_chain()
    response = chain.invoke(messages)
    print(response)
