# Anki Agent

Anki Agent is a Python-based program that scrapes word definitions from WordReference, formats them into Anki-compatible flashcards, and saves them to a text file. The program consists of three main components:

1. **`scraper.py`**: Scrapes word definitions from WordReference and saves them to a JSON file.
2. **`generate_anki_cards.py`**: Converts the scraped definitions into Anki-compatible flashcards and saves them to a text file.
3. **`run.py`**: Orchestrates the execution of the above scripts in sequence.

## Features

- Scrapes word definitions from WordReference.
- Formats definitions into Anki-compatible flashcards.
- Saves flashcards in a tab-separated format for easy import into Anki.

---

## Setup Instructions

### Prerequisites

1. **Python**: Ensure you have Python 3.7 or higher installed. You can download it from [python.org](https://www.python.org/).
2. **Pip**: Ensure `pip` is installed for managing Python packages.
3. **Virtual Environment (Optional)**: It's recommended to use a virtual environment to isolate dependencies.

### Installation Steps

1. Clone or download this repository to your local machine.
2. Navigate to the project directory:
   ```bash
   cd anki-agent
3. pip install -r requirements.txt

## How to Use
### Using Conversion Strings
The scraper.py script uses a conversion string to determine the language pair for translation. By default, the conversion string is set to fren (French to English). You can modify this to scrape definitions for other language pairs.

Examples of Conversion Strings:
fren: French to English
enfr: English to French

### How to Find Conversion Strings:
1. Go to WordReference.
1. Look up a word in your desired language pair.
1. Check the URL of the results page. The conversion string is the part of the URL after the domain and before the word. For example:
```https://www.wordreference.com/fren/avoir```
1. Here, fren is the conversion string for French to English.
1. Changing the Conversion String:
1. To change the conversion string, edit the conversion variable in scraper.py:
```conversion = "enfr"  # Example: English to French```

### Input File
words.txt: This file should contain a comma-separated list of words you want to scrape definitions for. Example:
### Running the Program
Run the run.py script to execute the entire workflow:

The program will:

- Scrape definitions for the words in words.txt and save them to definitions.json.
- Convert the definitions into Anki-compatible flashcards and save them to my_deck.txt.

Output Files
- definitions.json: Contains the scraped definitions in JSON format.
- my_deck.txt: Contains the Anki-compatible flashcards in a tab-separated format.
