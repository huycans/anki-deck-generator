import json
import os


def generate_anki_cards(definitions_file, output_file):
    try:
        # Load definitions from definitions.json
        with open(definitions_file, "r", encoding="utf-8") as file:
            definitions = json.load(file)

        # Check if the output file already exists
        file_exists = os.path.exists(output_file)

        # Open the output file for writing (overwrite any existing content)
        with open(output_file, "w", encoding="utf-8") as file:
            # If the file doesn't exist, write the Anki format header
            if not file_exists:
                file.write("#separator:tab\n")
                file.write("#html:true\n")

            # Process each word and its definitions
            for entry in definitions:
                word = entry.get("word", "").replace("%20", " ")
                # Combine all HTML definitions and wrap in <table><tbody>...</tbody></table>
                html_content = (
                    f"<table><tbody>{''.join(entry.get('html', []))}</tbody></table>"
                )

                # Write the Anki card in the specified format
                file.write(f'<h2>{word}</h2>\t"{html_content}"\n\n')

        print(f"Anki flashcards saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Input and output file paths
    definitions_file = "definitions.json"
    output_file = "my_deck.txt"

    # Generate Anki flashcards
    generate_anki_cards(definitions_file, output_file)
