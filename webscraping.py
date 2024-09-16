import requests
from bs4 import BeautifulSoup
import pandas as pd

current_page = 1
proceed = True
data = []

base_url = "https://books.toscrape.com/catalogue/"

while proceed:
    print("Page that is being scraped currently: " + str(current_page))
    url = f"https://books.toscrape.com/catalogue/page-{current_page}.html"
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    if not all_books:  # Stop when no books are found on the page
        print(f"No books found on page {current_page}. Stopping.")
        proceed = False
    else:
        for book in all_books:
            item = {}
            item['Title'] = book.find("img").attrs["alt"]
            item["Link"] = base_url + book.find("a").attrs["href"]
            item["Price"] = book.find("p", class_="price_color").text[1:]  # Remove £ symbol
            item['Stock'] = book.find("p", class_="instock availability").text.strip()

            data.append(item)
    
    current_page += 1

# Save the data
df = pd.DataFrame(data)
df.to_excel("books.xlsx", index=False)
df.to_csv("books.csv", index=False)
print("Done!")
