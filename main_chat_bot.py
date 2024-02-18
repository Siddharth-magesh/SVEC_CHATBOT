import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from functionalities import *
from talk import *
#nltk.download('punkt')  # Download NLTK tokenizer data
#nltk.download('wordnet')  # Download NLTK WordNet data

def get_related_words(keyword):
    synsets = wordnet.synsets(keyword)
    related_words = set()
    for synset in synsets:
        for lemma in synset.lemmas():
            related_words.add(lemma.name())
    return related_words

def is_keyword_present(string, keyword):
    tokens = word_tokenize(string.lower())
    lemmatizer = WordNetLemmatizer()
    keyword_variations = get_related_words(keyword)
    for token in tokens:
        token_lemma = lemmatizer.lemmatize(token)
        if token_lemma in keyword_variations:
            return True
    return False

def main_function(user_input):
    keywords = ["temperature", "budget"]
    for keyword in keywords:
        if is_keyword_present(user_input, keyword):
            if keyword == "budget":
                split_string = user_input.split()
                first_number = int(split_string[0])
                numbers = [int(num) for num in split_string[1:6]]
                m5 = budget_prediction(first_number, numbers)
                m5 = str(m5)
                return m5 + " is the minimum cost"
            elif keyword == "temperature":
                words = user_input.split()
                index_of_in = words.index("in")
                city_name = words[index_of_in + 1]
                m3 = temperature_prediction(city_name)
                return "Temperature in " + city_name + " is " + m3
    else:
        m6 = chatbot(user_input)
        return m6
