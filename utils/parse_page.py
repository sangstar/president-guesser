from bs4 import BeautifulSoup
from utils.html_from_url import get_html_from_url

BASE_PATH = "https://www.presidency.ucsb.edu"

def view_page(url):
    html = get_html_from_url(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def retrieve_search_page(page_number):
    to_parse = "https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks?page=" + str(page_number)
    html = get_html_from_url(to_parse)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_author_and_transcript_urls(soup, result_no):
    results = soup.find_all('div', {"class":"node node-documents node-teaser view-mode-teaser"})[result_no].find_all('a')
    link = BASE_PATH + results[0]['href']
    author = results[1].text
    return link, author


def retrieve_transcript(transcript_url):
    soup = view_page(transcript_url)
    return soup.find_all('div', {"class":"field-docs-content"})[0].find_all('p')


