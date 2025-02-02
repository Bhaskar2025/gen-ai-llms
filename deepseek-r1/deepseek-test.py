import openai
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "Write web scraping code with error handling"}],
    max_tokens=1000  # Limit costs for long responses
)