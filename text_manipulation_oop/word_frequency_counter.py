import re
from collections import Counter

class WordFrequencyCounter:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_and_process_file(self):
        """Read the file, clean the text, and return a list of words."""
        try:
            with open(self.file_path, 'r') as file:
                text = file.read()

            # Remove non-alphabetical characters and convert to lowercase
            text = re.sub(r'[^a-zA-Z\s]', '', text).lower()

            # Split the text into words
            words = text.split()
            return words
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return []
        except Exception as e:
            print(f"Error: {e}")
            return []

    def count_and_display(self):
        """Count word frequencies and display them."""
        words = self.read_and_process_file()
        if words:
            word_count = Counter(words)
            # Sort by frequency and then alphabetically
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

            print("Word frequency:")
            for word, count in sorted_word_count:
                print(f"{word:<15} {count} requests")

if __name__ == '__main__':
    file_path = 'input.txt'  # Path to your text file
    counter = WordFrequencyCounter(file_path)
    counter.count_and_display()
