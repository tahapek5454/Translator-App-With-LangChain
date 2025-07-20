from simple_message import get_chain

if __name__ == "__main__":
    chain = get_chain()
    response = chain.invoke({
        "language": "English",
        "text": "Ben yapay zeka ile çalışıyorum."
    })
    print(response)
