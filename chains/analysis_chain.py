from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from prompts.analyst import ANALYST_PROMPT


def create_analysis_chain():
    """
    Create the LangChain pipeline used by the Analyst Agent.
    """

    llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen3-4B",
        task="text-generation",
        max_new_tokens=1000,
        temperature=0.2,
    )

    chat_model = ChatHuggingFace(llm=llm)

    prompt = ChatPromptTemplate.from_template(ANALYST_PROMPT)

    return prompt | chat_model