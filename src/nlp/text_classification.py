import csv

import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocessing(text):
    text = text.decode('utf-8')
    # tokenize into words
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    # remove stopwords
    stop = stopwords.words('english')
    tokens = [token for token in tokens if token not in stop]
    # remove words less than three letters
    tokens = [word for word in tokens if len(word) >= 3]
    # lower capitalization
    tokens = [word.lower() for word in tokens]
    # lemmatize
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(word) for word in tokens]
    preprecessed_text = ''.join(tokens)
    return preprecessed_text


sms = open('SMSSpamCollection')
sms_data = []
sms_labels = []
csv_reader = csv.reader(sms, delimiter='\t')

for line in csv_reader:
    # adding the sms_id
    sms_labels.append(line[0])
    # adding the cleaned text
    sms_data.append(preprocessing(line[1]))

sms.close()

trainset_size = int(round(len(sms_data) * 0.70))
print 'Training Set size: ' + str(trainset_size)

x_train = np.array([''.join(el) for el in sms_data[0:trainset_size]])
y_train = np.array([el for el in sms_labels[0:trainset_size]])
x_test = np.array([''.join(el) for el in sms_data[trainset_size + 1:len(sms_data)]])
y_test = np.array([el for el in sms_labels[trainset_size + 1:len(sms_labels)]]) or el in sms_labels[
                                                                                         trainset_size + 1:len(
                                                                                             sms_labels)]

print x_train
print y_train

sms_exp = []

for line in sms_data:
    sms_exp.append(preprocessing(line[1]))
    vectorizer = CountVectorizer(min_df=1)
    X_exp = vectorizer.fit_transform(sms_exp)
    print '||'.join(vectorizer.get_feature_names())
    print X_exp.toarray()

vectorizer = TfidfVectorizer(min_df=2, ngram_range=(1,2), stop_words='english', strip_accents='unicode', norm='l2')
X_train = vectorizer.fit_transform(x_train)
X_test = vectorizer.transform(x_test)