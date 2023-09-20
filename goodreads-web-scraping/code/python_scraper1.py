import requests
from bs4 import BeautifulSoup

url = "https://www.goodreads.com/search?q=python+programming"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}
response = requests.get(url, headers=HEADERS)

if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    first_book = soup.find("tr", itemtype="http://schema.org/Book")

    title = first_book.find("span", itemprop="name")
    author = first_book.find("span", itemprop="author")
    rating = first_book.find("span", class_="minirating")

    if title and author and rating:
        title_text = title.text.strip()
        author_text = author.text.strip()
        rating_text = rating.text.strip()
        print(f"Title: {title_text}")
        print(f"Author: {author_text}")
        print(f"Rating: {rating_text}")

    else:
        print("No books found on the page.")
else:
    print("Failed to retrieve the webpage.")
