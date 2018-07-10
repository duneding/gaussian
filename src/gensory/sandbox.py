from HTMLParser import HTMLParser 
from monkeylearn import MonkeyLearn
import config

'''
class StreamHTMLParser(HTMLParser):
	def handle_data(self, data):
		self.data = data

	def getData(self):
		return self.data;

parser = StreamHTMLParser()
parser.feed(u'<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>')
test = parser.getData();
print 'test: ' + test
'''

'''
ml = MonkeyLearn('e8eae74a9f2d5f20d01e91ca3bc4bfbfadbe4322')
text_list = ["demoras en el subte", "buen estado del subte"]
module_id = 'cl_9mso8PPo'
'''
ext = 'ext'
dune = 'dune'
api = ext
token = config.value(['monkeylearn', api, 'en', 'token'])
module = config.value(['monkeylearn', api, 'en', 'module'])

ml = MonkeyLearn(token)
text_list = ["@The_BirdsWord: RT @JaredWyand: He spends Memorial Day Weekend...in #Hiroshima"]
module_id = module

res = ml.classifiers.classify(module_id, text_list, sandbox=True)
print "Resultado:"
print res.result[0][0]


