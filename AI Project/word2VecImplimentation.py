# Code taken and modified from
# https://medium.freecodecamp.org/how-to-get-started-with-word2vec-and-then-how-to-make-it-work-d0a2fca9dad3
# for purpose of reading files and training word2vec

import numpy as np
import gensim
import logging

from keras.callbacks import LambdaCallback
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
from keras.layers import Dense, Activation
from keras.models import Sequential

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def print_input(input_file):
    f = open(input_file, "r")
    for i, line in enumerate(f):
        print(line)


def read_input(input_file):
    f = open(input_file, "r")
    for i, line in enumerate(f):
        yield gensim.utils.simple_preprocess(line)


def word2idx(words):
    return model.wv.vocab[words].index


def idx2word(idx):
    return model.wv.index2word[idx]


# code taken from
# https://gist.github.com/maxim5/c35ef2238ae708ccb0e55624e9e0252b
# for purpose of creating text generation
def sample(preds, temperature=1.0):
    if temperature <= 0:
        return np.argmax(preds)

    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def generate_next(text, num_generated=10):
    word_idxs = [word2idx(words) for words in text.lower().split()]
    for i in range(num_generated):
        prediction = model.predict(x=np.array(word_idxs))
        idx = sample(prediction[-1], temperature=0.7)
        word_idxs.append(idx)
    return ' '.join(idx2word(idx) for idx in word_idxs)

def on_epoch_end(epoch, _):
    print('\nGenerating text after epoch: %d' % epoch)
    texts = [
        'the universe',
        '42',
        'arthur dent',
        'zaphod',
    ]
    for text in texts:
        sample = generate_next(text)
        print('%s... -> %s' % (text, sample))

max_quote_len = 40

quotes = list(read_input("Hitchhikers_Quotes.txt"))
model = gensim.models.Word2Vec(quotes, size=45, window=10, min_count=2, workers=10)
model.train(quotes, total_examples=len(quotes), epochs=100)

# code taken and modified from
# https://gist.github.com/maxim5/c35ef2238ae708ccb0e55624e9e0252b

pretrained_weights = model.wv.syn0
vocab_size, embedding_size = pretrained_weights.shape

train_x = np.zeros([len(quotes), max_quote_len], dtype=np.int32)
train_y = np.zeros([len(quotes)], dtype=np.int32)
for i, sentence in enumerate(quotes):
    for t, word in enumerate(sentence[:-1]):
        train_x[i, t] = word2idx(word)
    train_y[i] = word2idx(sentence[-1])
print('train_x shape:', train_x.shape)

sentence_model = Sequential()
sentence_model.add(Embedding(input_dim=vocab_size, output_dim=embedding_size, weights=[pretrained_weights]))
sentence_model.add(LSTM(units=embedding_size))
sentence_model.add(Dense(units=vocab_size))
sentence_model.add(Activation('softmax'))
sentence_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')


model.fit(train_x, train_y,
          batch_size=128,
          epochs=20,
          callbacks=[LambdaCallback(on_epoch_end=on_epoch_end)])

# w1 = "heart"
# print(model.wv.most_similar(positive=w1))
#
# #print_input("Hitchhikers_Quotes.txt")
