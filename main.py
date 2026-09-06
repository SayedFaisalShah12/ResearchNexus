import os

from dotenv import load_dotenv


load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print("Hugging Face token loaded:", bool(hf_token))