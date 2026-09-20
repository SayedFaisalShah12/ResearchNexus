import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

from prompts.critic import CRITIC_PROMPT


load_dotenv()


def create_critic_chain():
    """Create the critic pipeline using Hugging Face InferenceClient."""

    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    if not token:
        raise ValueError(
            "HUGGINGFACEHUB_API_TOKEN is not set in the environment."
        )

    client = InferenceClient(
        api_key=token,
        provider="auto",
    )

    prompt = ChatPromptTemplate.from_template(CRITIC_PROMPT)

    def generate_critique(prompt_value):
        """Generate a critique from the formatted LangChain prompt."""

        messages = prompt_value.to_messages()

        hf_messages = []

        for message in messages:
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

        if not hf_messages:
            raise ValueError(
                "Critic chain produced no messages for Hugging Face."
            )

        response = client.chat.completions.create(
            model="Qwen/Qwen3-4B-Instruct-2507",
            messages=hf_messages,
            max_tokens=1200,
            temperature=0.2,
        )

        return response.choices[0].message.content

    llm = RunnableLambda(generate_critique)

    return prompt | llm