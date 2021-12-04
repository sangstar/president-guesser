from bs4 import BeautifulSoup
from utils.html_from_url import get_html_from_url
import numpy as np
import csv

BASE_PATH = "https://www.presidency.ucsb.edu"

def view_page(url):
    html = get_html_from_url(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def retrieve_search_page(page_number):
    to_parse = "https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks?page=" + str(page_number)
    html = get_html_from_url(to_parse)
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all('div', {"class":"node node-documents node-teaser view-mode-teaser"})

def get_author_and_transcript_urls(soup, result_no):
    results = soup[result_no].find_all('a')
    transcript_title = results[0].text
    link = BASE_PATH + results[0]['href']
    author = results[1].text
    return link, author, transcript_title


def retrieve_transcript(transcript_url):
    soup = view_page(transcript_url)
    return soup.find_all('div', {"class":"field-docs-content"})[0].find_all('p')


def retrieve_data(max_pages, start_page):
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for i in np.arange(start_page, max_pages, 1):
            search_page = retrieve_search_page(i)
            for j in range(len(search_page)):
                link, author, transcript_title = get_author_and_transcript_urls(search_page, j)
                transcript = retrieve_transcript(link)
                writer.writerow([i,j, author, transcript_title, link, transcript])
        return 0


