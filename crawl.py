from urllib.parse import urlparse
from bs4 import BeautifulSoup

def normalize_url(url: str) -> str:
    if not url:
        raise ValueError("URL cannot be empty")
    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        raise ValueError("Invalid URL")
    netloc = parsed_url.netloc
    netloc = netloc.split(":")[0]
    parsed_url = f"{netloc}{parsed_url.path}"
    return parsed_url.rstrip("/")

def get_h1_from_html(html: str) -> list:
    if not html:
        raise ValueError("HTML content cannot be empty")
    soup = BeautifulSoup(html, 'html.parser')
    headers = soup.find_all('h1') 
    if len(headers) < 1:
        return ''
    return headers[0].get_text(strip=True)

def get_first_paragraph_from_html(html: str) -> str:
    if not html:
        raise ValueError("HTML content cannot be empty")
    soup = BeautifulSoup(html, 'html.parser')
    if (main := soup.find('main')) is not None:
        paragraphs = main.find_all('p')
    else:
        paragraphs = soup.find_all('p')
    if len(paragraphs) < 1:
        return ''
    return paragraphs[0].get_text(strip=True)

