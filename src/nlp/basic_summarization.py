import nltk

results = []
f = open('article.txt', 'r')
#article_content = unicode(f.read(), 'utf-8')
article_content = f.read()
sentences = nltk.sent_tokenize(article_content.decode('utf-8'))

for sent_no, sentence in enumerate(sentences):
#for sent_no, sentence in enumerate(nltk.sent_tokenize(article_content)):
    no_of_tokens = len(nltk.word_tokenize(sentence))
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    no_of_nouns = len([word for word,pos in tagged if pos in ['NN', 'NNP'] ])
    ners = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)), binary=False)
    no_of_ners = len([chunk for chunk in ners if hasattr(chunk, 'node')])
    score = (no_of_ners + no_of_nouns) / float(no_of_tokens)

    results.append((sent_no, no_of_tokens, no_of_ners, no_of_nouns, score, sentence))

for sent in sorted(results, key=lambda x: x[4], reverse=True):
    print sent[5]