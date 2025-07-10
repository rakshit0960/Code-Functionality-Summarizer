from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = str(os.getenv("GEMINI_API_KEY"))
openai_api_key = str(os.getenv("OPENAI_API_KEY"))

# model_client = OpenAIChatCompletionClient(
#     model="gemini-2.5-flash",
#     api_key=gemini_api_key,
# )

model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini",
    api_key=openai_api_key,
)