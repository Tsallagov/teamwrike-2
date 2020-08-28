import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer

class Model_v1:

    def text_normalization(self, text):
        porter = PorterStemmer()

        res = []
        if (type(text) != str):
            text = str(text)
        text = text.lower()

        # Text cleaning
        trash_symbols = "!”#$%&’'()*+-,.:;<=>?@[]\|/^_`{}~]\"\'"
        for i in range(len(trash_symbols)):
            text = text.replace(trash_symbols[i], '')
        text = text.replace('  ', ' ')

        # Tokenizing
        text = text.split(' ')
        # Stamming and using only useful words
        trash_words = ['', 'a', 'an', 'the', 'or']
        for word in text:
            if (word not in trash_words):
                res.append(porter.stem(word))
        return res

    def fit_transform(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.corpus = []
        #self.corpus = list(map(' '.join, self.data['norm_title'].values))
        for sentence in self.data['norm_title'].values:
            sentence = sentence[2:-2].split("', '")
            sentence = " ".join(sentence)
            self.corpus.append(sentence.replace('\\xa0', ' '))

        to_delete = ['\n', '']
        for symb in to_delete:
            if symb in self.corpus:
                self.corpus.remove(symb)

        self.corpus = ['How to ' + s for s in self.corpus]

        self.vectorizer = TfidfVectorizer()
        self.trans_matrix = self.vectorizer.fit_transform(self.corpus)
        self.vocabulary = self.vectorizer.get_feature_names()

    def predict(self, request):
        norm_request = self.text_normalization(request)
        #print(' '.join(norm_request))
        request_vector = self.vectorizer.transform([' '.join(norm_request)])

        # Finding max dot product (max similarity of sentences)
        n = 0
        max_dot = 0
        pred_title = ''
        for title in self.trans_matrix:
            res = np.dot(request_vector.toarray(), title.toarray().T)
            if (res > max_dot):
                max_dot = res
                pred_title = self.corpus[n]
            n += 1
        #print(pred_title)
        pred_row = self.data['How to ' + self.data['norm_title'].map(lambda x: " ".join(x[2:-2].split("', '"))) == pred_title]
        pred_row.index = range(len(pred_row))
        if (len(pred_row) == 0):
            return 'Sorry', "Couldn\'t find answer"
        else:
            title = 'How to ' + pred_row['title'][0]
            answer = pred_row['answer'][0]
            return title, answer
