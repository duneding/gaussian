from nltk.tag.stanford import StanfordNERTagger

path_snlp = '/Users/mdagostino/software/stanford-corenlp/edu/stanford/nlp/models/ner/'
st = StanfordNERTagger(path_snlp + 'spanish.ancora.distsim.s512.crf.ser.gz', path_snlp + 'stanford-ner.jar')
st.tag('Estoy estudiando en la UTN'.split())