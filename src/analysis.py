import csv
import re
from collections import Counter
from pathlib import Path


def load_talk_text(file_path):
    """
    Load the text from the first talk in the CSV file.

    Parameters:
        file_path: The path to the CSV file.

    Returns:
        The text from the first talk in the dataset.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        first_talk = next(reader)
        return first_talk["text"]


def clean_text(text):
    """
    Clean the provided text for word counting.

    This function converts the text to lowercase and removes
    punctuation and other non-letter characters.

    Parameters:
        text: The text to clean.

    Returns:
        The cleaned text.
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text


def get_word_counts(text):
    """
    Count word frequencies in the provided text.

    TODO:
    Modify this function to ignore the words
    "the", "a", "and", "of", and "to" when counting.

    Keep all other words, count how many times each one appears,
    and return the results as a Counter object.
    """
    words = text.split()

    # Write your code here.

    return Counter(words)


def main():
    """
    Run the text analysis.

    This function loads the first talk from the dataset,
    cleans the text, counts the words, and prints the
    ten most common words.
    """
    data_path = Path(__file__).resolve().parent.parent / "data" / "talks.csv"

    talk = load_talk_text(data_path)
    cleaned_talk = clean_text(talk)
    word_counts = get_word_counts(cleaned_talk)

    print(word_counts.most_common(10))


if __name__ == "__main__":
    main()
