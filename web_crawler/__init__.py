import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def get_unique_links(url):
    visited_links = set()  # Store visited links to avoid duplication
    links_to_visit = set([url])  # Initialize with the main URL

    while links_to_visit:
        current_url = links_to_visit.pop()  # Get a URL to process

        if current_url in visited_links:  # Skip if we already visited this URL
            continue

        visited_links.add(current_url)  # Mark this URL as visited

        try:
            # Send a GET request to the current URL
            response = requests.get(current_url)

            # Only process HTML content
           # if 'text/html' not in response.headers.get('Content-Type', ''):
            #    continue

            # Parse the response using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract all the links on the page (using the `href` attribute from <a> tags)
            links = [link.get("href") for link in soup.find_all("a")]

            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                # Resolve relative URLs to absolute ones
                full_url = urljoin(current_url, href)

                # Only include links from the same domain (optional, depending on use case)
                if urlparse(full_url).netloc == urlparse(url).netloc:
                    if full_url not in visited_links:  # If not already added
                        links_to_visit.add(full_url)
        except Exception as e:
            print(f"Error accessing {current_url}: {e}")

    return visited_links

