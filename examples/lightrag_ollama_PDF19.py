import asyncio
import os
import inspect
import logging
from lightrag import LightRAG, QueryParam
from lightrag.llm.ollama import ollama_model_complete, ollama_embed
from lightrag.utils import EmbeddingFunc

WORKING_DIR = "./PDF19"

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=ollama_model_complete,
    llm_model_name="qwen2.5:7b",
    llm_model_max_async=4,
    llm_model_max_token_size=32000,
    llm_model_kwargs={"host": "http://localhost:11434", "options": {"num_ctx": 32000}},
    embedding_func=EmbeddingFunc(
        embedding_dim=768,
        max_token_size=2048,
        func=lambda texts: ollama_embed(
            texts, embed_model="nomic-embed-text", host="http://localhost:11434"
        ),
    ),
)

with open("./pdfs/pdf_19.txt", "r", encoding="utf-8") as f:
    rag.insert(f.read())

# Perform naive search
print(
    rag.query("What are the top topics of the article?", param=QueryParam(mode="naive"))
)

# Perform local search
print(
    rag.query("What are the top topics in this article?", param=QueryParam(mode="local"))
)

# Perform global search
print(
    rag.query("What are the top topics in this article?", param=QueryParam(mode="global"))
)

# Perform hybrid search
print(
    rag.query("What are the top topics in this article?", param=QueryParam(mode="hybrid"))
)

# stream response
resp = rag.query(
    "What are the top topics in this article?",
    param=QueryParam(mode="hybrid", stream=True),
)


async def print_stream(stream):
    async for chunk in stream:
        print(chunk, end="", flush=True)


if inspect.isasyncgen(resp):
    asyncio.run(print_stream(resp))
else:
    print(resp)
