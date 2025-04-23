import subprocess


def run_scraper():
    try:
        print("Running scraper.py...")
        subprocess.run(["python", "scraper.py"], check=True)
        print("scraper.py completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running scraper.py: {e}")
        exit(1)


def run_generate_anki_cards():
    try:
        print("Running generate_anki_cards.py...")
        subprocess.run(["python", "generate_anki_cards.py"], check=True)
        print("generate_anki_cards.py completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running generate_anki_cards.py: {e}")
        exit(1)


if __name__ == "__main__":
    # Run scraper.py
    run_scraper()

    # Run generate_anki_cards.py
    run_generate_anki_cards()

    print("All tasks completed successfully.")
