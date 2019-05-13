#code taken from http://www.albertauyeung.com/post/generating-ngrams-python/
import random, re
import nltk
nltk.download('punkt')

#open filestream to read the quote corpus
f = open("Hitchhikers_quotes.txt", "r")
contents = f.read()

#test string
#string = "Natural-language processing (NLP) is an area of computer science " \
#    "and artificial intelligence concerned with the interactions " \
#    "between computers and human (natural) languages."

def generate_ngrams(s, n):
	#convert to lowercases
	s = s.lower()

	#replace non alphanumeric characters with spaces
	s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)

	#break sentence in token, remove empty token
	tokens = [token for token in s.split(" ") if token != ""]

	#Use the zip function to generate n-grams
	#Concatnate tokens into ngrams and return
	ngrams = zip(*[tokens[i:] for i in range(n)])
	return [" ".join(ngram) for ngram in ngrams]




print(generate_ngrams(contents, 20))