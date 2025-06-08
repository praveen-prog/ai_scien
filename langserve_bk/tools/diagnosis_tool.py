from langchain_core.tools import tool
from utils.euri_client import euri_chat_completion


@tool
def ai_sci_diagnosis(topic_description):
    """ Check the links and provide latest advancements"""

    message = [
        {
            "role" : "user",
            "content" : f"based on the topic {topic_description} give relevant latest topics from arxiv org website`"    
        }
    ]


    return euri_chat_completion(messages=message)


