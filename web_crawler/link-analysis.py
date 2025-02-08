from web_crawler import get_unique_links
from webscrapper.website import Website
import requests
#import openai

OLLAMA_API = "http://localhost:11434/api/chat"
MODEL = "llama3.2"

link_system_prompt = "You are provided with a list of links found on a webpage. \
You are able to decide which of the links would be most relevant to include in a brochure about the company, \
such as links to an About page, or a Company page, or Careers/Jobs pages.\n"
link_system_prompt += "You should respond in JSON as in this example:"
link_system_prompt += """
{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page": "url": "https://another.full.url/careers"}
    ]
}
"""

def get_links_user_prompt(website):
    user_prompt = f"Here is the list of links on the website of {website} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += '\n'.join(get_all_details(website))
    return user_prompt


def get_all_details(website):
    unique_links = get_unique_links(website)
    return unique_links


def get_links_response(website):
    user_prompt = get_links_user_prompt(website)
    # response = openai.chat.completions.create(
    #     model = "gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": link_system_prompt},
    #         {"role": "user", "content": user_prompt}
    #     ]
    # )

    response = requests.post(OLLAMA_API, json={
        "model": MODEL,
        "messages": [
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "stream": False
    })
    #return response.choices[0].message.content
    return response.json()['message']['content']



website = "https://globe24news.com/"
#print(website.links)
print(get_links_response(website))