import fasttext

#model = fasttext.skipgram('../data/text_mining/fasttext_data.txt', 'model')
#print model.words

model = fasttext.load_model('model.bin')
print model['anillo']
