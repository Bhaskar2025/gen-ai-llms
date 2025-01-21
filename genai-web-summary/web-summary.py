import openai
import os
from dotenv import load_dotenv

from webscrapper import website
from webscrapper.website import Website

load_dotenv(override=True)
# Set up OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

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



# Send a request to OpenAI's GPT model
site = Website("https://biryanibykilo.com/")

response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt_generator(site)}
        ]
)

# Print the model's response
print(response.choices[0].message.content)