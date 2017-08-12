from nltk.tag import RegexpTagger

date_regex = RegexpTagger([(r'(\d{2})[/.-](\d{2})[/.-](\d{4})$', 'DATE'), (r'\$', 'MONEY')])
test_tokens = 'I will be flying on sat 10-02-2014 with around 10M $'.split()
print date_regex.tag(test_tokens)