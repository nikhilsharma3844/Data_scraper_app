import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch the webpage
url = "http://books.toscrape.com/"
response = requests.get(url)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract book titles and prices
books = soup.find_all("article", class_="product_pod")

data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").get_text()
    data.append([title, price])

# Step 4: Save to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])  # Header
    writer.writerows(data)

print("✅ Data saved into books.csv")
