import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Web Scraper", layout="centered")

st.title("Web Scraper")

url = st.text_input("Enter website URL",placeholder="https://stxaviersbhopal.org/")

if st.button("Scrape"):
    if not url:
        st.warning("Please enter a URL")
    else:
        try:
            with st.spinner("Scraping website..."):
                r = requests.get(url, timeout=20)
                r.raise_for_status()

                soup = BeautifulSoup(r.text, "html.parser")
                testimonials = soup.find_all("div", class_="testimonial")

                if not testimonials:
                    st.info("Data not found")
                else:
                    st.success(f"Found {len(testimonials)} testimonials")

                    for i, t in enumerate(testimonials, start=1):
                        title = t.find("h3", class_="title")
                        desc = t.find("p", class_="description")

                        if title and desc:
                            st.subheader(f"{i}. {title.get_text(strip=True)}")
                            st.write(desc.get_text(strip=True))
                            st.divider()

        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching the URL: {e}")


