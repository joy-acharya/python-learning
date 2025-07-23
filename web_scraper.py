#What it does:
#Sends HTTP requests to each page (page 1, 2, 3...).
#Parses the HTML to extract:

#Quote text

#Author name

#Tags related to the quote

#Writes this data into a CSV file with 3 columns: Quotes, Author, Tags.

#Stops when there are no more pages or no more quotes.





import csv
from bs4 import BeautifulSoup
import requests


base_url = "http://quotes.toscrape.com/page/{}/"


with open("csvwritter", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Quotes", "Author", "Tags"])

    page = 1

    while True:

        print(f"scraping page {page}")
        response = requests.get(base_url.format(page))

        if response.status_code != 200:
            print('No more pages')
            break

        soup = BeautifulSoup(response.text,"html.parser")
        quotes = soup.find_all('div', class_='quote')

        if not quotes:
            print('No more quotes')
            break;

        for quote in quotes:
            text = quote.find('span', class_="text").get_text(strip=True)
            author = quote.find('small', class_="author").get_text(strip=True)

            tags = [ tag.get_text(strip=True) for tag in quote.find_all('a', class_="tag")]

            writer.writerow([text, author, "".join(tags)])
        page += 1
