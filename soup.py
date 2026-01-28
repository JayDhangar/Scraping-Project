import requests
from bs4 import BeautifulSoup

url="https://stxaviersbhopal.org/"

r=requests.get(url)
soup =BeautifulSoup(r.text,"html")


testimonials = soup.find_all("div", class_="testimonial")

for t in testimonials:
    title=t.find("h3",class_="title")
    desc=t.find("p",class_="description")

    if title and desc:
        print(title.get_text())
        print(desc.get_text())
