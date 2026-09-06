import os

from dotenv import load_dotenv
from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint,
)


load_dotenv()


HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not HF_TOKEN:
    raise ValueError(
        "HUGGINGFACEHUB_API_TOKEN is missing from .env"
    )


llm = HuggingFaceEndpoint(
    repo_id="YOUR_MODEL_ID",
    huggingfacehub_api_token=HF_TOKEN,
    temperature=0.2,
    max_new_tokens=512,
)

model = ChatHuggingFace(llm=llm)