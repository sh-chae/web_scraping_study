import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text
# print(html_src)
soup = BeautifulSoup(html_src,'html.parser')

target_img = soup.find(name = 'img', attrs = {'alt':'Seoul-Metro-2004-20070722.jpg'})
print('HTML 요소: ',target_img)
print("\n")

target_img_src = target_img.get('src')
print('이미지 파일 경로: ', target_img_src)
print("\n")
target_img_resp = requests.get('http:'+target_img_src)
out_file_path = "./output/download_image.jpg"

with open(out_file_path, 'wb') as out_file:
    out_file.write(target_img_resp.content)
    print("이미지 파일로 저장하였습니다.")



# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/sh-chae/web_scraping_study.git
# git push -u origin main