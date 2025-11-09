pip install requests beautifulsoup4


import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    Scrapes the title and all paragraph texts from a given URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        dict: A dictionary containing the title and a list of paragraph texts,
              or None if an error occurs.
    """
    try:
        # Fetch the HTML content of the page
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title
        title = soup.find('title').text if soup.find('title') else "No Title Found"

        # Extract all paragraph texts
        paragraphs = [p.text for p in soup.find_all('p')]

        return {"title": title, "paragraphs": paragraphs}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return None

if __name__ == "__main__":
    target_url = "https://en.wikipedia.org/wiki/Web_scraping"
    scraped_data = scrape_website(target_url)

    if scraped_data:
        print(f"Title: {scraped_data['title']}")
        print("\nParagraphs:")
        for i, p in enumerate(scraped_data['paragraphs'][:5]):  # Print first 5 paragraphs
            print(f"{i+1}. {p[:100]}...") # Print first 100 characters of each paragraph
