import requests
def get_html_from_url(url):
    r = requests.get(url)
    return r.text