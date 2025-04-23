import os
import json
import logging
import time

import requests
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)


def scrape_dictionary(word, session):
    # Replace spaces and single quotes with dashes for the URL
    word = word.replace(" ", "-").replace("'", "-")
    url = f"https://www.wordreference.com/fren/{word}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0",
        "Accept": "text/html",
    }
    try:
        # Fetch the webpage
        response = session.get(url, headers=headers)
        response.raise_for_status()
        print(response.status_code)  # Debugging line to check status code

        # Decode the response content to handle raw byte data
        decoded_content = response.content.decode(response.apparent_encoding or "utf-8")

        # Parse the HTML
        soup = BeautifulSoup(decoded_content, "html.parser")

        # Find the first relevant table
        table = soup.find(
            "table",
            class_="WRD",
            attrs={"data-dict": "fren"},
        )
        if not table:
            logging.error(f"No relevant table found for word '{word}'")
            return {"word": word, "html": []}

        # Extract definitions
        combined_html = []

        for row in table.find_all("tr"):
            try:
                # Skip rows with class 'wrtopsection' or 'langHeader'
                if "class" in row.attrs and (
                    "wrtopsection" in row["class"] or "langHeader" in row["class"]
                ):
                    continue

                if "id" in row.attrs:  # New definition starts
                    combined_html.append(str(row))
                elif combined_html:  # Part of the current definition
                    combined_html.append(str(row))
            except Exception as e:
                logging.error(f"Error processing row for word '{word}': {e}")
                continue

        return {"word": word, "html": combined_html}

    except requests.RequestException as e:
        logging.error(f"HTTP error occurred for word '{word}': {e}")
        return {"word": word, "html": []}
    except Exception as e:
        logging.error(f"An error occurred for word '{word}': {e}")
        return {"word": word, "html": []}


def read_words_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            words = [word.strip() for word in content.split(",")]
            return words
    except Exception as e:
        logging.error(f"Error reading words from file: {e}")
        raise


if __name__ == "__main__":
    # Delete the definitions.json file if it exists
    definitions_file = "definitions.json"
    if os.path.exists(definitions_file):
        os.remove(definitions_file)
        print(f"Deleted existing {definitions_file}")

    words_file = "words.txt"  # Path to the file containing words
    words_to_lookup = read_words_from_file(words_file)

    # Use a session to persist headers and cookies
    all_definitions = []
    with requests.Session() as session:
        for word in words_to_lookup:
            definition = scrape_dictionary(word, session)
            all_definitions.append(definition)
            time.sleep(2)  # Add a delay between requests

    # Save all definitions to a single JSON file
    with open(definitions_file, "w", encoding="utf-8") as json_file:
        json.dump(all_definitions, json_file, ensure_ascii=False, indent=4)

    print(f"All definitions saved to {definitions_file}")
