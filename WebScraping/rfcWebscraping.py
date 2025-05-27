from bs4 import BeautifulSoup
import requests

url = "https://www.ietf.org/rfc/"


def fetchContent(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(len(soup.contents[0]))


fetchContent(url)