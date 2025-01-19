import openai
import os
from dotenv import load_dotenv

load_dotenv(override=True)
# Set up OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define system and user prompts
system_prompt = "You are a helpful assistant."
user_prompt = "What is the weather today in New York?"

# Send a request to OpenAI's GPT model

response = openai.chat.completions.create(
        model = "gpt-4-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
)

# Print the model's response
print(response.choices[0].message.content)