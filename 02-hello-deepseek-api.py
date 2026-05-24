# 老版写法
# from langchain_deepseek import ChatDeepSeek
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatDeepSeek(
#     model="deepseek-chat",
#     temperature=0.1,
#     max_tokens=2000,
#     timeout=None,
#     max_retries=2,
# )

# for chunk in model.stream("来一段毛泽东的诗词"):
#     print(chunk.content, end='', flush=True)

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# model = init_chat_model(
#     model="deepseek:deepseek-chat",
#     model_provider="deepseek",
#     temperature=0.1,
# )
# 或
model = init_chat_model(
    model="deepseek:deepseek-chat",
    temperature=0.1,
)
for chunk in model.stream("来一段毛泽东的诗词"):
    print(chunk.content, end='', flush=True)