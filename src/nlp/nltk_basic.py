import json
import operator
import re

import nltk
import urllib2
from bs4 import BeautifulSoup
from nltk import UnigramTagger as ut
from nltk.corpus import cess_esp as cess

#tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
#nltk.FreqDist(tags)

# Read the corpus into a list,
# each entry in the list is one sentence.
cess_sents = cess.tagged_sents()

# Train the unigram tagger
uni_tag = ut(cess_sents)

sentence = "Hola , esta foo bar ."

# Tagger reads a list of tokens.
uni_tag.tag(sentence.split(" "))


url = "https://es.wikipedia.org/wiki/J._R._R._Tolkien"
response = urllib2.urlopen(url)
html_raw = response.read().decode('utf8')
#html_raw = response.read()
print 'RAW len: ' + str(len(html_raw))

soup = BeautifulSoup(html_raw, 'html.parser')
html_text = soup.get_text()

tokens = [tok for tok in re.split('\W+', html_text)]
print 'Tokens x100: '
print tokens[:100]
print len(tokens)

freq_distro = nltk.FreqDist(tokens)

print 'Frecuency Distro x100:'
freq_distro_items = sorted(freq_distro.items(), key=operator.itemgetter(1), reverse=True)
for k, v in freq_distro_items[:100]:
    print str(k) + ':' + str(v)

freq_distro.plot(50, cumulative=False)

with open('stop_words_es.json') as json_data:
    stop_words_es = json.load(json_data)

clean_tokens = [tok for tok in tokens if len(tok.lower()) > 1 and (tok.lower() not in stop_words_es)]
freq_distro_cleaned = nltk.FreqDist(clean_tokens)

freq_distro_cleaned.plot(50, cumulative=False)

print 'Tokens cleaned x100: '
print clean_tokens[:100]
print len(clean_tokens)