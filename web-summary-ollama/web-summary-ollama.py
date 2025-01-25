import requests

from webscrapper.website import Website

site = Website("https://biryanibykilo.com/")
HEADERS = {
    "Content-Type": "application/json"}
OLLAMA_API = "http://localhost:11434/api/chat"
MODEL = "llama3.2"
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

payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt_generator(site)}
        ],
        "stream": False
    }

# Example usage

response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
print(response.json()['message']['content'])


