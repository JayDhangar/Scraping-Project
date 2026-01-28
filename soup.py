from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/testimonials")
def get_testimonials():
    url = "https://stxaviersbhopal.org/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    data = []
    for t in soup.find_all("div", class_="testimonial"):
        title = t.find("h3", class_="title")
        desc = t.find("p", class_="description")
        if title and desc:
            data.append({
                "title": title.get_text(strip=True),
                "description": desc.get_text(strip=True)
            })

    return jsonify(data)

if __name__ == "__main__":
    app.run()

