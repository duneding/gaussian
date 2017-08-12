import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

results = []
f = open('article.txt', 'r')
#article_content = unicode(f.read(), 'utf-8')
article_content = f.read()
sentences = nltk.sent_tokenize(article_content.decode('utf-8'))
vectorizer = TfidfVectorizer(norm='l2', min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True)
sklearn_binary = vectorizer.fit_transform(sentences)

print vectorizer.get_feature_names()
print sklearn_binary.toarray()

for i in sklearn_binary.toarray():
    results.append(i.sum() / float(len(i.nonzero()[0])))

print 1