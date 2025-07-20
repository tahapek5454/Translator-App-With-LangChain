from modelchain import get_chain
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(
    title="Translation API",
    description="An API for translating text using Azure OpenAI",
    version="1.0.0"
)
chain = get_chain()

add_routes(app, chain, path="/chain")

# for langchain playground http://localhost:8000/chain/playground
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
