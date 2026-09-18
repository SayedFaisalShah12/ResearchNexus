import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

from prompts.writer import WRITER_PROMPT


load_dotenv()


def create_writer_chain():
    """Create the report-writing pipeline using Hugging Face InferenceClient."""

    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    if not token:
        raise ValueError(
            "HUGGINGFACEHUB_API_TOKEN is not set in the environment."
        )

    client = InferenceClient(
        api_key=token,
        provider="auto",
    )

    prompt = ChatPromptTemplate.from_template(WRITER_PROMPT)

    def generate_report(messages):
        hf_messages = []

        for message in messages:
            if hasattr(message, "type") and hasattr(message, "content"):
                role = message.type

                if role == "human":
                    role = "user"
                elif role == "ai":
                    role = "assistant"

                hf_messages.append(
                    {
                        "role": role,
                        "content": str(message.content),
                    }
                )

        response = client.chat.completions.create(
            model="Qwen/Qwen3-4B-Instruct-2507",
            messages=hf_messages,
            max_tokens=1500,
            temperature=0.3,
        )

        return response.choices[0].message.content

    llm = RunnableLambda(generate_report)

    return prompt | llm