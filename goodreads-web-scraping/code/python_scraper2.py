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

    # Locate all book entries on the page
    book_entries = soup.find_all("tr", itemtype="http://schema.org/Book")

    for i, book_entry in enumerate(book_entries, start=1):
        title = book_entry.find("span", itemprop="name")
        author = book_entry.find("span", itemprop="author")
        rating = book_entry.find("span", class_="minirating")

        if title and author and rating:
            title_text = title.text.strip()
            author_text = author.text.strip()
            rating_text = rating.text.strip()
            print(f"Book {i}:")
            print(f"Title: {title_text}")
            print(f"Author: {author_text}")
            print(f"Rating: {rating_text}")
            print()

else:
    print("Failed to retrieve the webpage.")
