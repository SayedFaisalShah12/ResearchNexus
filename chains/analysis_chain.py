import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

from prompts.analyst import ANALYST_PROMPT

load_dotenv()


def create_analysis_chain():
    """Create the analysis pipeline using Hugging Face InferenceClient."""

    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    if not token:
        raise ValueError(
            "HUGGINGFACEHUB_API_TOKEN is not set in the environment."
        )

    client = InferenceClient(
        api_key=token,
        provider="auto",
    )

    prompt = ChatPromptTemplate.from_template(ANALYST_PROMPT)

    def generate_analysis(messages):
        response = client.chat.completions.create(
            model="Qwen/Qwen3-4B-Instruct-2507",
            messages=[
                {
                    "role": role,
                    "content": content,
                }
                for role, content in messages
            ],
            max_tokens=1000,
            temperature=0.2,
        )

        return response.choices[0].message.content

    llm = RunnableLambda(generate_analysis)

    return prompt | llm