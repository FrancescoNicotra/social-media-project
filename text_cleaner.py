import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

WL = WordNetLemmatizer()

def read_csv(path: str) -> pd.DataFrame:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    nltk.download('vader_lexicon')
    nltk.download('stopwords')

    # Read the CSV file
    return pd.read_csv(path)

def clean_text(text: pd.DataFrame) -> pd.DataFrame:
    # Create 'clean_text' column by copying 'testo' column
    text['clean_text'] = text['testo'].apply(lambda x: str.lower(x) if pd.notna(x) else x)

    # Remove punctuation and replace newlines/tabs
    text['clean_text'] = text['clean_text'].apply(lambda x: re.sub(r'[^\w\s]', ' ', x) if pd.notna(x) else x)
    text['clean_text'] = text['clean_text'].apply(lambda x: re.sub(r'[\n\t]', ' ', x) if pd.notna(x) else x)
    return text

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def lemmatizer(string):
    word_pos_tags = nltk.pos_tag(word_tokenize(string))
    a = [WL.lemmatize(tag[0], get_wordnet_pos(tag[1])) for idx, tag in enumerate(word_pos_tags)]
    return " ".join(a)

def lemmatize_text(text: pd.DataFrame) -> pd.DataFrame:
    return text['clean_text'].apply(lambda x: lemmatizer(x) if pd.notna(x) else x)

def stopword(string):
    a = [i for i in string.split() if i not in stopwords.words('english')]
    return ' '.join(a)

def remove_empty_rows(text: pd.DataFrame) -> pd.DataFrame:
    text['clean_text'].replace('', np.nan, inplace=True)
    text.dropna(subset=['clean_text'], inplace=True)
    return text

if __name__ == "__main__":
    path = './transcriptions/Chris_Evans_OPENS_UP_About_His_‘Deadpool_&_Wolverine’_Cameo_(Exclusive)__E!_News.csv'
    text = read_csv(path)
    text = clean_text(text)
    text['clean_text'] = lemmatize_text(text)
    text['clean_text'] = text['clean_text'].apply(lambda x: stopword(x) if pd.notna(x) else x)
    text = remove_empty_rows(text)

    # Sovrascrivi il file CSV originale
    text.to_csv(path, index=False, encoding='utf-8')

    print(text)
