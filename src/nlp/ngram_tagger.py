import nltk
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger
from nltk.tag import BigramTagger
from nltk.tag import TrigramTagger
from nltk.corpus import brown

tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
print nltk.FreqDist(tags)
brown_tagged_sents = brown.tagged_sents(categories='news')
default_tagger = DefaultTagger('NN')
print default_tagger.evaluate(brown_tagged_sents)

train_data = brown_tagged_sents[:int(len(brown_tagged_sents) * 0.9)]
test_data = brown_tagged_sents[int(len(brown_tagged_sents) * 0.9):]
unigram_tagger = UnigramTagger(train_data, backoff=default_tagger)
bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)
trigram_tagger = TrigramTagger(train_data, backoff=bigram_tagger)

print unigram_tagger.evaluate(test_data)
print bigram_tagger.evaluate(test_data)
print trigram_tagger.evaluate(test_data)
