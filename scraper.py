import re
from urllib.parse import urlparse
from lxml import html
import requests
from lxml import etree, objectify


def scraper(url, resp):
    result = []
    page = requests.get(url)
    if page.status_code != 200:
        return result
    links = extract_next_links(url, resp)
    result = [link for link in links if is_valid(link)]
    return result

def getURL(page):
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

def extract_next_links(url, resp):
    # Implementation requred.
    result = []
    page = requests.get(url)
    if page.status_code != 200:
        return result
    page = str(page.content)
    while True:
        url, n = getURL(page)
        page = page[n:]
        if url:
            if '#' not in url:
                p = requests.get(url)
                if p.status_code != 200:
                    return result
            result.append(url)
        else:
            break
    return result

def is_valid(url):
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        domains = set(["ics.uci.edu", "cs.uci.edu", "informatics.uci.edu", "stat.uci.edu", "today.uci.edu/department/information_computer_sciences"])
        if not any(d in url for d in domains):
            return False
        if "http://http://" in url:
            return False
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise