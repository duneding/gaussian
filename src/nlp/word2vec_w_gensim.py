# import modules & set up logging
import logging
import gensim
import os

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()


# sentences = MySentences('../../data/nlp/silmarillion.txt')  # a memory-friendly iterator
sentences = MySentences('../../data/nlp/w2v')  # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences, iter=1)

# model.build_vocab(sentences)  # can be a non-repeatable, 1-pass generator
# model.train(sentences)  # can be a non-repeatable, 1-pass generator

print 'most similar: ' + str(model.most_similar(positive=['ring', 'king'], negative=['man'], topn=1))
print 'similarity: ' + str(model.similarity('Ainur', 'man'))
print 'does not match: ' + str(model.doesnt_match('king ring men'.split()))

