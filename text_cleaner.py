import pandas as pd
import numpy as np
import csv
#for text pre-processing
import re, string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
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

text = read_csv('./transcriptions/Chris_Evans_OPENS_UP_About_His_‘Deadpool_&_Wolverine’_Cameo_(Exclusive)__E!_News.csv')

def clean_text(text: pd.DataFrame) -> pd.DataFrame:
	#lambda function to transform the text to lowercase
	text['testo'] = text['testo'].apply(lambda x: str.lower(x) if pd.isna(x) != True else x)

	#lambda function to remove the punctuation
	text['clean_text'].apply(lambda x: re.sub(r'[^\w\s]', ' ', x) if pd.notna(x) else x)
	text['clean_text'] = text['clean_text'].apply(lambda x: re.sub(r'[\n\t]', ' ', x) if pd.notna(x) else x)

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
	return text['clean_text'].apply(lambda x: lemmatizer(x) if pd.isna(x) != True else x)

def stopword(string):
	a = [i for i in string.split() if i not in stopwords.words('english')]
	return ' '.join(a)

def remove_empty_rows(text: pd.DataFrame) -> pd.DataFrame:
	text['clean_text'].replace('', np.nan,inplace=True)
	return text.dropna(subset=['clean_text'], inplace=True)

if __name__ == "__main__":
	clean_text(text)
	text['clean_text'] = lemmatize_text(text)
	text['clean_text'] = text['clean_text'].apply(lambda x: stopword(x) if pd.isna(x) != True else x)
	remove_empty_rows(text)
	text.to_csv('./transcriptions/Chris_Evans_OPENS_UP_About_His_‘Deadpool_&_Wolverine’_Cameo_(Exclusive)__E!_News_clean.csv', index=False)
	print(text)