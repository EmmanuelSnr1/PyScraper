# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_site(url):
    # Use requests to retrieve data from the given URL
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Create a list to store the scraped content
    content = []

    # Find all header tags (h1, h2, h3, etc.) and their associated contents
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for header in headers:
        header_text = header.get_text().strip()
        data = []
        siblings = header.find_next_siblings()
        for sibling in siblings:
            if sibling.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                break
            if sibling.name in ['a', 'p']:
                data.append(sibling.get_text().strip())

            # Find all the child tags of the siblings
            children = sibling.find_all(['a', 'p'])
            for child in children:
                data.append(child.get_text().strip())

        content.append({'tag': header.name, 'text': header_text, 'data': data})

    return content



def scrape_site_with_content_categories(url):
    # Use requests to retrieve data from the given URL
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Create a dictionary to store the scraped content
    content = {
        'paragraphs': [],
        'links': [],
        'headings': []
    }

    # Find all paragraphs and store their text content
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        content['paragraphs'].append(paragraph.get_text().strip())

    # Find all anchor tags and store their href attribute values and text content
    anchor_tags = soup.find_all('a')
    for anchor in anchor_tags:
        href = anchor.get('href')
        text = anchor.get_text().strip()
        content['links'].append({'href': href, 'text': text})

    # Find all header tags (h1, h2, h3, etc.) and store their text content
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for header in headers:
        content['headings'].append(header.get_text().strip())

    return content



def scrape_website(url, element, attr_type=None, attr_value=None):
    # Use requests to retrieve data from a given URL
    response = requests.get(url)
    # Parse the whole HTML page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements with the specified tags and classes
    if attr_type and attr_value:
        articles = soup.find_all(element, {attr_type: attr_value})
    else:
        articles = soup.find_all(element)

    # Extract the titles and organize them into a dictionary where the key is the title and the value is the URL
    news = {article.text: url + article['href'] for article in articles if article['href'].startswith('/')}

    return news
