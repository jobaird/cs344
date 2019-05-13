# Code taken and modified from
# https://medium.freecodecamp.org/how-to-get-started-with-word2vec-and-then-how-to-make-it-work-d0a2fca9dad3
# for purpose of reading files and training word2vec

import keras
import numpy as np
import gensim
import logging
import string
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from keras.callbacks import LambdaCallback
from keras.layers.recurrent import LSTM

from keras.layers.embeddings import Embedding
from keras.layers import Dense, Activation
from keras.models import Sequential
from keras.utils.data_utils import get_file

url = 'https://github.com/jobaird/cs344/blob/master/AI%20Project/Hitchhikers_quotes.txt'
path = get_file('hitch.txt', origin=url)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def print_input(input_file):
    f = open(input_file, "r")
    for i, line in enumerate(f):
        print(line)


def read_input(input_file):
    f = open(input_file, "r")
    for i, line in enumerate(f):

        yield gensim.utils.simple_preprocess(line)


def word2idx(word):
  return word_model.wv.vocab[word].index

def idx2word(idx):
  return word_model.wv.index2word[idx]


# code taken from
# https://gist.github.com/maxim5/c35ef2238ae708ccb0e55624e9e0252b
# for purpose of creating text generation
#edits done to values in attempts to get better output.
def sample(preds, temperature=1.0):
  if temperature <= 0:
    return np.argmax(preds)
  preds = np.asarray(preds).astype('float64')
  preds = np.log(preds) / temperature
  exp_preds = np.exp(preds)
  preds = exp_preds / np.sum(exp_preds)
  probas = np.random.multinomial(1, preds, 1)
  return np.argmax(probas)


def generate_next(text, num_generated=20):
  word_idxs = [word2idx(word) for word in text.lower().split()]
  for i in range(num_generated):
    prediction = model.predict(x=np.array(word_idxs))
    idx = sample(prediction[-1], temperature=0.7)
    word_idxs.append(idx)
  return ' '.join(idx2word(idx) for idx in word_idxs)

def on_epoch_end(epoch, _):
  print('\nGenerating text after epoch: %d' % epoch)
  texts = [
      'the universe',
      'the guide',
      'arthur dent',
      'zaphod',
      'the answer',
  ]
  for text in texts:
    sample = generate_next(text)
    print('%s... -> %s' % (text, sample))

max_sentence_len = 40
with open(path) as file_:
  docs = file_.readlines()
sentences = [[word for word in doc.lower().translate(string.punctuation).split()[:max_sentence_len]] for doc in docs]
print('\nTraining word2vec...')
word_model = gensim.models.Word2Vec(sentences, size=40, min_count=1, window=5, iter=200)
pretrained_weights = word_model.wv.syn0
vocab_size, emdedding_size = pretrained_weights.shape
print('Result embedding shape:', pretrained_weights.shape)
print('Checking similar words:')
for word in ['universe', 'guide', 'arthur', 'zaphod', 'answer']:
  most_similar = ', '.join('%s (%.2f)' % (similar, dist) for similar, dist in word_model.most_similar(word)[:8])
  print('  %s -> %s' % (word, most_similar))

# code taken and modified from
# https://gist.github.com/maxim5/c35ef2238ae708ccb0e55624e9e0252b

print('\nPreparing the data for LSTM...')
train_x = np.zeros([len(sentences), max_sentence_len], dtype=np.int32)
train_y = np.zeros([len(sentences)], dtype=np.int32)
for i, sentence in enumerate(sentences):
  for t, word in enumerate(sentence[:-1]):
    train_x[i, t] = word2idx(word)
  train_y[i] = word2idx(sentence[-1])
print('train_x shape:', train_x.shape)
print('train_y shape:', train_y.shape)


print('\nTraining LSTM...')
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=emdedding_size, weights=[pretrained_weights]))
model.add(LSTM(units=emdedding_size))
model.add(Dense(units=vocab_size))
model.add(Activation('softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')


model.fit(train_x, train_y,
          batch_size=256,
          epochs=50,
          callbacks=[LambdaCallback(on_epoch_end=on_epoch_end)])

