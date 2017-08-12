import nltk

#text = "the cat is under the table. the president is going to speak about the medical care reform"
text = "Hoy voy a ver una serie en Netflix. Ayer fui a comer pizza."

sentences = nltk.sent_tokenize(text)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]

for sent in tagged_sentences:
    print nltk.ne_chunk(sent)

