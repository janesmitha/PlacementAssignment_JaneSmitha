'''Write a program to count the number of verbs, nouns, pronouns, and adjectives in a given particular phrase or
paragraph, and return their respective count as a dictionary.
Note -
1. Write code comments wherever required for code
2. You have to write at least 2 additional test cases in which your program will run successfully and provide
an explanation for the same.

Example Output -'''
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
'''nltk.download('punkt')'''
nltk.download('averaged_perceptron_tagger')

def count_pos_tags(text):
    """
    Count the number of verbs, nouns, pronouns, and adjectives in a given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary containing the count of verbs, nouns, pronouns, and adjectives.
    """
    # Tokenize the text into sentences and words
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]

    # Perform part-of-speech tagging on the words
    tagged_words = [pos_tag(sentence) for sentence in words]

    # Initialize counters for verbs, nouns, pronouns, and adjectives
    verb_count = 0
    noun_count = 0
    pronoun_count = 0
    adjective_count = 0

    # Iterate over tagged words and count the respective part-of-speech tags
    for sentence in tagged_words:
        for word, tag in sentence:
            if tag.startswith('V'):
                verb_count += 1
            elif tag.startswith('N'):
                noun_count += 1
            elif tag.startswith('PRP'):
                pronoun_count += 1
            elif tag.startswith('JJ'):
                adjective_count += 1

    # Create a dictionary to store the counts
    pos_counts = {
        'Verbs': verb_count,
        'Nouns': noun_count,
        'Pronouns': pronoun_count,
        'Adjectives': adjective_count
    }

    return pos_counts

# Example usage
text = "I love eating delicious food. It makes me happy."
counts = count_pos_tags(text)
print(counts)

