import requests
from bs4 import BeautifulSoup
import sys

def scrape_links(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all anchor tags
        links = soup.find_all('a')

        # Extract and print the href attribute of each link
        for link in links:
            href = link.get('href')
            if href:
                print(href)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scrape_links.py <URL>")
    else:
        url = sys.argv[1]
        scrape_links(url)
