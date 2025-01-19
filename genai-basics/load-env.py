import os
from dotenv import load_dotenv

load_dotenv(override=True)
openai_api_key = os.environ.get("OPENAI_API_KEY")
print(openai_api_key)