import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
URL = "https://www.audible.com/adblbestsellers"

# Adding headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def scrape_audible():
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Locate the container for all book items
    book_list = soup.find_all("li", class_="productListItem")

    data = []

    for book in book_list:
        try:
            # Extracting specific data points
            title = book.find("h3").get_text(strip=True)
            author = book.find("li", class_="authorLabel").get_text(strip=True).replace("By:", "")
            runtime = book.find("li", class_="runtimeLabel").get_text(strip=True).replace("Length:", "")
            
            data.append({
                "Title": title,
                "Author": author,
                "Runtime": runtime
            })
        except AttributeError:
            # Skip items that don't match the expected format
            continue

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(data)
    df.to_csv("audible_bestsellers.csv", index=False)
    print(f"Success! {len(data)} books scraped and saved to audible_bestsellers.csv")

if __name__ == "__main__":
    scrape_audible()