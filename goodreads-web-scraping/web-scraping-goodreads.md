# Web Scraping Goodreads for Python Programming Books

In this tutorial, we will walk through the process of web scraping Python programming book information from the Goodreads website. We will use Python, the `requests` library for making HTTP requests, and `BeautifulSoup` for parsing HTML content.

## Setting up the environment

Before we start, let's set up our development environment. Assuming we are working in an existing directory named `coding`, create a new subdirectory named `python_scraper` and set up a virtual environment:

```console
user@host:~$ cd coding
user@host:~/coding$ mkdir python_scraper
user@host:~/coding$ cd python_scraper
user@host:~/coding/python_scraper$ python3 -m venv .venv
user@host:~/coding/python_scraper$ source .venv/bin/activate
(.venv) user@host:~/coding/python_scraper$
```

Next, install the required Python libraries:

```console
(.venv) user@host:~/coding/python_scraper$ pip install requests beautifulsoup4
```

Open VS Code in the current directory:

```console
(.venv) user@host:~/coding/python_scraper$ code .
```

In VS Code, create a new Python file named `python_scraper.py`.

![File Explorer New File button](https://code.visualstudio.com/assets/docs/languages/cpp/new-file.png)

## Initial Version: Web Scraping Goodreads Python Books

### Step 1: Importing Libraries

In our `python_scraper.py` file, start by importing the necessary libraries for web scraping.

```python
import requests
from bs4 import BeautifulSoup
```

### Step 2: Setting the URL and Headers

Define the URL of the Goodreads Python programming books section and set custom headers for the HTTP request.

```python
url = 'https://www.goodreads.com/search?q=python+programming'

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}
response = requests.get(url, headers=HEADERS)
```

### Step 3: Checking the Request Status

Check if the HTTP request was successful by examining the status code.

```python
if response.status_code == 200:
```

### Step 4: Parsing HTML with BeautifulSoup

Parse the HTML content of the web page using BeautifulSoup. (Notice the indentation starting here.)

```python
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
```

### Step 5: Extracting Book Data

Locate the HTML element representing the first book on the page using specific attributes and schema information.

```python
    first_book = soup.find('tr', itemtype="http://schema.org/Book")
```

### Step 6: Extracting Title, Author, and Rating

Within the book's HTML element, use specific selectors to locate and extract the title, author, and rating of the book.

```python
    title = first_book.find('span', itemprop="name")
    author = first_book.find('span', itemprop="author")
    rating = first_book.find('span', class_="minirating")
```

### Step 7: Displaying Book Information

Extract the text content of the title, author, and rating elements and print out this information. (More indenting.)

```python
    if title and author and rating:
        title_text = title.text.strip()
        author_text = author.text.strip()
        rating_text = rating.text.strip()
        print(f"Title: {title_text}")
        print(f"Author: {author_text}")
        print(f"Rating: {rating_text}")
```

### Step 8: Error handling and Completion

Handle two scenarios: one for when no books are found on the page and another for when the initial HTTP request fails.

```python
    else:
        print('No books found on the page.')
else:
    print('Failed to retrieve the webpage.')
```



## Version 2: Scraping Multiple Python Books

Before we dive into the code changes for this version, let's start by identifying the code that needs to be removed from the previous version. We'll remove the code responsible for extracting and displaying information about a single book entry since we'll be transitioning to extracting multiple book entries.

#### Code to Remove (From Previous Version)

Please remove the following code block, as it's no longer needed:

```python
-     # Extract Title, Author, and Rating for the first book
-     title = first_book.find('span', itemprop="name")
-     author = first_book.find('span', itemprop="author")
-     rating = first_book.find('span', class_="minirating")
- 
-     # Display Book Information for the first book
-     if title and author and rating:
-         title_text = title.text.strip()
-         author_text = author.text.strip()
-         rating_text = rating.text.strip()
-         print("Title:", title_text)
-         print("Author:", author_text)
-         print("Rating:", rating_text)
-     else:
-         print("No books found on the page.")
```

Now that we've removed the unnecessary code, let's proceed to the last steps of Version 2 with more detail.

### Step 1: Extracting Multiple Book Entries

We've modified the code to locate all the HTML elements representing book entries on the page. Here's the updated code:

```python
-    first_book = soup.find('tr', itemtype="http://schema.org/Book")
+    # Locate all book entries on the page
+    book_entries = soup.find_all('tr', itemtype="http://schema.org/Book")
```

### Step 2: Loop Through Book Entries

We're now looping through each book entry, extracting book details, and printing them. This allows us to gather information for multiple books. Here's the code for this step:

```python
+     # Loop through each book entry and extract details
+     for i, book_entry in enumerate(book_entries, start=1):
+         title = book_entry.find('span', itemprop="name")
+         author = book_entry.find('span', itemprop="author")
+         rating = book_entry.find('span', class_="minirating")
+  
+         if title and author and rating:
+             title_text = title.text.strip()
+             author_text = author.text.strip()
+             rating_text = rating.text.strip()
+             print(f"Book {i}:")
+             print(f"Title: {title_text}")
+             print(f"Author: {author_text}")
+             print(f"Rating: {rating_text}")
```

These code changes enable us to scrape and display information about multiple Python programming books from Goodreads. If you have any further questions or are ready to proceed, please let me know.
