import requests
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver

def find_links_page_n(n):
    url = f"http://www.todayhumor.co.kr/board/list.php?table=humorbest&page={n}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("td", attrs={"class":"subject"})
    l_list = ['http://www.todayhumor.co.kr'+link.find('a')['href'] for link in links]
    return l_list

page = 1
# page = input("page number?: ")

# chrome_driver_path = "/users/chae/Developer/PycharmProjects/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
#     driver.get(link)

for link in find_links_page_n(page):
    webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open(link)