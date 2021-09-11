import requests
from bs4 import BeautifulSoup
import webbrowser

url = "https://bbs.ruliweb.com/best/humor"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("li", attrs={"class": "item"})
# print(links)
l_list = [link.find('a')['href'] for link in links][:24]
# print(l_list)

for link in l_list:
    webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open(link)