import requests
from bs4 import BeautifulSoup

url = "https://example.com"  # Replace this with the target website URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n", strip=True)
    print(text)
else:
    print(f"Failed to fetch the site. Status code: {response.status_code}")
    