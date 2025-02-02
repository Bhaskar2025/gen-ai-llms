from bs4 import BeautifulSoup
import requests

class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        self.soup = BeautifulSoup(response.text, "html.parser")
        self.title = self.soup.title.text if self.soup.title else "No Title"
        for tagscript in self.soup(["script", "style", "input", "image","meta", "iframe", "form"]):
            tagscript.decompose()
        self.text = self.soup.body.get_text(separator="\n", strip=True)

        links = [link.get("href") for link in self.soup.find_all("a")]
        self.links = [link for link in links if link]
        self.links = list(set(self.links))

#bhaskar = Website("https://globe24news.com/")
#print(bhaskar.links)




