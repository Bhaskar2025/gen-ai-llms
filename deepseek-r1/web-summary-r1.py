import os

import openai
from dotenv import load_dotenv

from webscrapper.website import Website

load_dotenv(override=True)

base_url = "https://api.deepseek.com"

API_KEY = os.environ.get("DEEPSEEK_API_KEY")
client = openai.OpenAI(api_key=API_KEY, base_url=base_url)

# Define system and user prompts
system_prompt = ("You are an assistant that analyzes the contents of a website "
                 "and provides a detailed summary, ignoring text that might be navigation related."
                 "Respond in markdown.")

def user_prompt_generator(website):
    user_prompt = "The contents of this website is as follows; \
    please provide a detailed summary of this website in markdown. \
    If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt


site = Website("https://globe24news.com/")

response = client.chat.completions.create(
        model = "deepseek-reasoner",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt_generator(site)}
        ],
        max_tokens=1000
)

# Print the model's response
print(response.choices[0].message.content)