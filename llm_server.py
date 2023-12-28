from llms.llm import LLM
from llms.chatgpt import ChatGPT
from config.config import get_config

config = get_config()
model_name = config.get("openai", 'model_name')
model: LLM = ChatGPT(model_name)


def request_llm(sys_prompt: str, user_prompt: list, stream=False):
    return model.request(sys_prompt, user_prompt, stream)
