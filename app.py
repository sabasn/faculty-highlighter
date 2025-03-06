
import re
from bs4 import BeautifulSoup

def highlight_words_in_html(file_path, output_path):
    """Highlight only specific words in an HTML file without affecting full sentences."""
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # List of words to highlight
    WORDS_TO_HIGHLIGHT = ["research", "proposal", "faculty", "grant", "funding", "innovation"]

    # Define a regex pattern that ensures we only replace the whole word, not substrings
    for word in WORDS_TO_HIGHLIGHT:
        pattern = r'\b' + re.escape(word) + r'\b'  # Match the exact word only
        replacement = rf'<span style="background-color: yellow;">{word}</span>'

        # Replace only the exact word occurrences
        for element in soup.find_all(string=True):
            new_text = re.sub(pattern, replacement, element, flags=re.IGNORECASE)
            if new_text != element:
                element.replace_with(BeautifulSoup(new_text, "html.parser"))

    # Save the modified HTML file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(str(soup))
